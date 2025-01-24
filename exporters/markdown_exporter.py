import os
import logging
from typing import List, Dict
from exporters.exporter import Exporter


class MarkdownExporter(Exporter):
    """Exports test results to Markdown format."""

    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, test_results: List[Dict]) -> str:
        """Exports test results to a Markdown file.

        Args:
            test_results (List[Dict]): List of test result dictionaries.

        Returns:
            str: Path to the exported Markdown file.
        """
        logging.info(f"Exporting {len(test_results)} test cases to {self.output_path}")
        os.makedirs(os.path.dirname(os.path.abspath(self.output_path)), exist_ok=True)
        with open(self.output_path, 'w') as file:
            file.write("# Test Results Report\n\n")
            file.write("| Test Case Name | Status | Execution Time | Timestamp |\n")
            file.write("|---------------|--------|---------------|------------|\n")
            for test in test_results:
                file.write(f"| {test.get('name', 'Unknown')} | {test.get('status', 'Unknown')} | "
                           f"{test.get('execution_time', 0)} | {test.get('timestamp', 'N/A')} |\n")
        logging.info(f"File successfully written: {self.output_path}")
        return self.output_path
