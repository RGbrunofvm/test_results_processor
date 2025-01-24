import unittest
import os
import json
from utils.json_loader import JSONLoader


class TestJSONLoader(unittest.TestCase):
    """Tests for the JSONLoader class."""

    def setUp(self):
        """Create a temporary JSON file before running tests."""
        self.valid_json_file = "test_valid.json"
        self.invalid_json_file = "test_invalid.json"

        valid_data = {
            "test_cases": [
                {"name": "Test 1", "status": "pass", "execution_time": 1.2, "timestamp": "2025-01-24T01:00:00Z"},
                {"name": "Test 2", "status": "fail", "execution_time": 2.5, "timestamp": "2025-01-24T01:10:00Z"}
            ]
        }

        with open(self.valid_json_file, "w") as file:
            json.dump(valid_data, file)

        with open(self.invalid_json_file, "w") as file:
            file.write("{invalid_json}")

    def tearDown(self):
        """Clean up temporary JSON files after tests."""
        for file in [self.valid_json_file, self.invalid_json_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_load_valid_json(self):
        """Test loading a valid JSON file."""
        loader = JSONLoader(self.valid_json_file)
        test_cases = loader.load()
        self.assertEqual(len(test_cases), 2)
        self.assertEqual(test_cases[0]["name"], "Test 1")

    def test_load_invalid_json(self):
        """Test handling of invalid JSON file."""
        loader = JSONLoader(self.invalid_json_file)
        test_cases = loader.load()
        self.assertEqual(test_cases, [])


if __name__ == "__main__":
    unittest.main()
