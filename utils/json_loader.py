import json
import os
import logging
from typing import List, Dict


class JSONLoader:
    """Handles loading test results from a JSON file."""

    def __init__(self, json_file: str):
        self.json_file = json_file

    def load(self) -> List[Dict]:
        """Loads the test results from a JSON file.

        Returns:
            List[Dict]: List of test result dictionaries.
        """
        if not os.path.exists(self.json_file):
            logging.error(f"❌ JSON file '{self.json_file}' does not exist.")
            return []
        try:
            with open(self.json_file, 'r') as file:
                data = json.load(file)
                logging.info(f"📂 Loaded {len(data.get('test_cases', []))} test cases from JSON.")
                return data.get("test_cases", [])
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logging.error(f"❌ Error loading JSON: {e}")
            return []
