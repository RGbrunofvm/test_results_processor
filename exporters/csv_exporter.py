import csv
import os
import logging
from typing import List, Dict
from exporters.exporter import Exporter


class CSVExporter(Exporter):
    """Exports test results to CSV."""

    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, test_results: List[Dict]) -> str:
        """Exports test results to a CSV file.

        Args:
            test_results (List[Dict]): List of test result dictionaries.

        Returns:
            str: Path to the exported CSV file.
        """
        logging.info(f"Exporting {len(test_results)} test cases to {self.output_path}")
        os.makedirs(os.path.dirname(os.path.abspath(self.output_path)), exist_ok=True)
        with open(self.output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Test Case Name", "Status", "Execution Time", "Timestamp"])
            for test in test_results:
                writer.writerow([
                    test.get("name", "Unknown"),
                    test.get("status", "Unknown"),
                    test.get("execution_time", 0),
                    test.get("timestamp", "N/A")
                ])
        logging.info(f"File successfully written: {self.output_path}")
        return self.output_path
