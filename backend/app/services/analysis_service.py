from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.models.farmer import Farmer
from app.models.report import Report

from app.services.gemini_service import GeminiService
from app.services.weather_service import WeatherService
from app.services.report_service import ReportService

from app.crew.crew import run_agriculture_crew


class AnalysisService:

    @staticmethod
    def analyze_crop(
        analysis_id: int,
        db: Session
    ):

        # ---------------------------------------------------
        # Fetch Analysis
        # ---------------------------------------------------

        analysis = (
            db.query(Analysis)
            .filter(Analysis.id == analysis_id)
            .first()
        )

        if analysis is None:
            raise Exception("Analysis not found.")

        # ---------------------------------------------------
        # Fetch Farmer
        # ---------------------------------------------------

        farmer = (
            db.query(Farmer)
            .filter(Farmer.id == analysis.farmer_id)
            .first()
        )

        if farmer is None:
            raise Exception("Farmer not found.")

        # ---------------------------------------------------
        # Gemini Vision
        # ---------------------------------------------------

        gemini_result = GeminiService.detect_disease(
            image_path=analysis.image_path,
            crop_name=analysis.crop_name
        )

        disease = gemini_result.get("disease", "Unknown")

        confidence = float(
            gemini_result.get("confidence", 0)
        )

        severity = gemini_result.get(
            "severity",
            "Unknown"
        )

        symptoms = gemini_result.get(
            "symptoms",
            []
        )

        # ---------------------------------------------------
        # Weather
        # ---------------------------------------------------

        weather_data = WeatherService.get_weather(
            farmer.location
        )

        # ---------------------------------------------------
        # CrewAI
        # ---------------------------------------------------

        crew_result = run_agriculture_crew(
            crop_name=analysis.crop_name,
            disease_name=disease,
            confidence=confidence,
            location=farmer.location,
            weather_data=weather_data
        )

        # ---------------------------------------------------
        # Update Analysis
        # ---------------------------------------------------

        analysis.disease = disease
        analysis.confidence = confidence
        analysis.severity = severity

        analysis.symptoms = ", ".join(symptoms)

        analysis.weather = crew_result.get(
            "weather_advice",
            ""
        )

        analysis.fertilizer = crew_result.get(
            "fertilizer",
            ""
        )

        analysis.irrigation = crew_result.get(
            "irrigation",
            ""
        )

        analysis.prevention = crew_result.get(
            "prevention",
            ""
        )

        analysis.organic_treatment = crew_result.get(
            "organic_treatment",
            ""
        )

        analysis.chemical_treatment = crew_result.get(
            "chemical_treatment",
            ""
        )

        analysis.soil_recommendation = crew_result.get(
            "soil_recommendation",
            ""
        )

        db.commit()
        db.refresh(analysis)

        # ---------------------------------------------------
        # Generate PDF Report
        # ---------------------------------------------------

        pdf_path = ReportService.generate_pdf(
            analysis_id=analysis.id,
            report_text=crew_result.get(
                "report",
                ""
            )
        )

        # ---------------------------------------------------
        # Save Report
        # ---------------------------------------------------

        report = (
            db.query(Report)
            .filter(Report.analysis_id == analysis.id)
            .first()
        )

        if report is None:

            report = Report(
                analysis_id=analysis.id,
                report_text=crew_result.get(
                    "report",
                    ""
                ),
                pdf_path=pdf_path
            )

            db.add(report)

        else:

            report.report_text = crew_result.get(
                "report",
                ""
            )

            report.pdf_path = pdf_path

        db.commit()
        db.refresh(report)

        # ---------------------------------------------------
        # Final Response
        # ---------------------------------------------------

        return {

            "analysis_id": analysis.id,

            "crop_name": analysis.crop_name,

            "farmer": farmer.name,

            "location": farmer.location,

            "disease": disease,

            "confidence": confidence,

            "severity": severity,

            "symptoms": symptoms,

            "weather": weather_data,

            "weather_advice": crew_result.get(
                "weather_advice",
                ""
            ),

            "soil_recommendation": crew_result.get(
                "soil_recommendation",
                ""
            ),

            "fertilizer": crew_result.get(
                "fertilizer",
                ""
            ),

            "irrigation": crew_result.get(
                "irrigation",
                ""
            ),

            "prevention": crew_result.get(
                "prevention",
                ""
            ),

            "organic_treatment": crew_result.get(
                "organic_treatment",
                ""
            ),

            "chemical_treatment": crew_result.get(
                "chemical_treatment",
                ""
            ),

            "report": crew_result.get(
                "report",
                ""
            ),

            "pdf_path": report.pdf_path

        }