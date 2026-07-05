import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BACKEND_URL")


class APIClient:

    @staticmethod
    def register_farmer(
        name,
        location
    ):

        response = requests.post(
            f"{BASE_URL}/farmers/",
            json={
                "name": name,
                "location": location
            }
        )

        return response.json()

    @staticmethod
    def analyze_crop(
        farmer_id,
        crop_name,
        image_path
    ):

        with open(image_path, "rb") as image:

            response = requests.post(
                f"{BASE_URL}/analysis/",
                data={
                    "farmer_id": farmer_id,
                    "crop_name": crop_name
                },
                files={
                    "image": image
                }
            )

        return response.json()

    @staticmethod
    def download_report(
        analysis_id
    ):

        response = requests.get(
            f"{BASE_URL}/reports/{analysis_id}"
        )

        return response