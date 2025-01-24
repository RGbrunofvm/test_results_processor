import os
import logging
import pandas as pd
from typing import List, Dict
from exporters.exporter import Exporter


class ExcelExporter(Exporter):
    """Exports test results to an Excel file."""

    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, test_results: List[Dict]) -> str:
        """Exports test results to an Excel file.

        Args:
            test_results (List[Dict]): List of test result dictionaries.

        Returns:
            str: Path to the exported Excel file.
        """
        logging.info(f"Exporting {len(test_results)} test cases to {self.output_path}")
        os.makedirs(os.path.dirname(os.path.abspath(self.output_path)), exist_ok=True)

        df = pd.DataFrame(test_results)
        df.to_excel(self.output_path, index=False)

        logging.info(f"File successfully written: {self.output_path}")
        return self.output_path
