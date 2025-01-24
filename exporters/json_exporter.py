import json
import os
import logging
from typing import List, Dict
from exporters.exporter import Exporter


class JSONExporter(Exporter):
    """Exports test results to JSON."""

    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, test_results: List[Dict]) -> str:
        """Exports test results to a JSON file.

        Args:
            test_results (List[Dict]): List of test result dictionaries.

        Returns:
            str: Path to the exported JSON file.
        """
        logging.info(f"Exporting {len(test_results)} test cases to {self.output_path}")
        os.makedirs(os.path.dirname(os.path.abspath(self.output_path)), exist_ok=True)
        with open(self.output_path, 'w') as file:
            json.dump({"test_cases": test_results}, file, indent=4)
        logging.info(f"File successfully written: {self.output_path}")
        return self.output_path
