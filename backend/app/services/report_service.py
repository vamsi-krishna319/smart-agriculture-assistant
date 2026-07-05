import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


class ReportService:

    REPORT_FOLDER = "reports"

    @staticmethod
    def generate_pdf(
        analysis_id: int,
        report_text: str
    ):

        os.makedirs(
            ReportService.REPORT_FOLDER,
            exist_ok=True
        )

        pdf_path = os.path.join(
            ReportService.REPORT_FOLDER,
            f"analysis_{analysis_id}.pdf"
        )

        document = SimpleDocTemplate(pdf_path)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b>Smart Agriculture Assistant Report</b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph("<br/><br/>", styles["Normal"])
        )

        for line in report_text.split("\n"):

            if line.strip():

                story.append(
                    Paragraph(
                        line,
                        styles["BodyText"]
                    )
                )

        document.build(story)

        return pdf_path