import unittest
import requests
import jsonschema
import json

class TestSuccessResponse(unittest.TestCase):

    def test_validate_response(self):
        # Make a GET request to the URL
        url = "https://jsonplaceholder.typicode.com/todos/1"
        response = requests.request("GET", url)

        # Validate the success response
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code}")

        # Validate the schema response
        schema = {
            "type": "object",
            "properties": {
                "userId": {"type": "integer"},
                "id": {"type": "integer"},
                "title": {"type": "string"},
                "completed": {"type": "boolean"}
            },
            "required": ["userId", "id", "title", "completed"]
        }
        json_data = json.loads(response.text)
        jsonschema.validate(instance=json_data, schema=schema)

if __name__ == '__main__':
    unittest.main()