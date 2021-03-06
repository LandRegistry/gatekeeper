import unittest
import requests
import json

from gatekeeper.main import app


class TestHealthRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app

    def test_health_service_check(self):
        test_health_check = requests.get(app.config["DEED_API_URL"] + "/health/service-check")
        test_health_list = json.loads(test_health_check.text)

        self.assertEqual(test_health_check.status_code, 200)

        # Assert that there is a minimum of 4 service responses
        # Which are: register/title adapter, esec-client and postgres
        self.assertEqual(True, True) if len(test_health_list["services"]) >= 4 else self.assertEqual(False, True)

        # Assert that there is only one "services" tag; which is essentially a tag
        # that has an array of services as a value
        self.assertEqual(len(test_health_list), 1)

        # Test that certain tags/values are present
        self.assertIn("service_from", str(test_health_list["services"]))
        self.assertIn("service_to", str(test_health_list["services"]))
        self.assertIn("status_code", str(test_health_list["services"]))
        self.assertIn("service_message", str(test_health_list["services"]))

        # Test that the return json is not empty
        self.assertIsNotNone(test_health_list)

        # Test that the returned json is converted to a dictionary correctly
        self.assertIsInstance(test_health_list, dict)
