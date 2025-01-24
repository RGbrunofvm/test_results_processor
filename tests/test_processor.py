import unittest
import os
import json
from processors.processor import Processor
from exporters.csv_exporter import CSVExporter
from exporters.json_exporter import JSONExporter
from exporters.markdown_exporter import MarkdownExporter
from exporters.excel_exporter import ExcelExporter  # ✅ Se agregó ExcelExporter
from utils.metrics_calculator import MetricsCalculator


class TestProcessor(unittest.TestCase):
    """Tests for the Processor class."""

    def setUp(self):
        """Create temporary JSON test files before running tests."""
        self.json_file = "test_results.json"
        self.csv_output = "results/test_results.csv"
        self.json_output = "results/test_results.json"
        self.md_output = "results/test_results.md"
        self.xlsx_output = "results/test_results.xlsx"

        self.test_data = {
            "test_cases": [
                {"name": "Test 1", "status": "pass", "execution_time": 1.2, "timestamp": "2025-01-24T01:00:00Z"},
                {"name": "Test 2", "status": "fail", "execution_time": 2.5, "timestamp": "2025-01-24T01:10:00Z"}
            ]
        }

        os.makedirs("results", exist_ok=True)

        with open(self.json_file, "w") as file:
            json.dump(self.test_data, file)

    def tearDown(self):
        """Clean up generated files after tests."""
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

        for file in [self.csv_output, self.json_output, self.md_output, self.xlsx_output]:
            if os.path.exists(file):  # ✅ Ahora verifica antes de eliminar
                os.remove(file)

    def test_processor_csv(self):
        """Test Processor correctly processes and exports CSV."""
        processor = Processor(self.json_file, self.csv_output, CSVExporter(self.csv_output))
        processor.run()
        self.assertTrue(os.path.exists(self.csv_output))

    def test_processor_json(self):
        """Test Processor correctly processes and exports JSON."""
        processor = Processor(self.json_file, self.json_output, JSONExporter(self.json_output))
        processor.run()
        self.assertTrue(os.path.exists(self.json_output))

    def test_processor_markdown(self):
        """Test Processor correctly processes and exports Markdown."""
        processor = Processor(self.json_file, self.md_output, MarkdownExporter(self.md_output))
        processor.run()
        self.assertTrue(os.path.exists(self.md_output))

    def test_processor_excel(self):
        """Test Processor correctly processes and exports Excel."""
        processor = Processor(self.json_file, self.xlsx_output, ExcelExporter(self.xlsx_output))
        processor.run()
        self.assertTrue(os.path.exists(self.xlsx_output))

    def test_metrics_calculation(self):
        """Test Processor correctly calculates metrics."""
        processor = Processor(self.json_file, self.json_output, JSONExporter(self.json_output))
        processor.run()

        metrics = MetricsCalculator.calculate(processor.test_results)
        self.assertEqual(metrics["Total Tests"], 2)
        self.assertEqual(metrics["Passed Tests"], 1)
        self.assertEqual(metrics["Failed Tests"], 1)


if __name__ == "__main__":
    unittest.main()
