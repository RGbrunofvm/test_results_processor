import unittest
import os
import json
from exporters.csv_exporter import CSVExporter
from exporters.json_exporter import JSONExporter
from exporters.markdown_exporter import MarkdownExporter
from exporters.excel_exporter import ExcelExporter  # Agregar soporte para Excel


class TestExporters(unittest.TestCase):
    """Tests for different export formats."""

    def setUp(self):
        """Setup temporary test output files."""
        self.csv_file = "test_output.csv"
        self.json_file = "test_output.json"
        self.md_file = "test_output.md"
        self.xlsx_file = "test_output.xlsx"

        self.test_results = [
            {"name": "Test 1", "status": "pass", "execution_time": 1.2, "timestamp": "2025-01-24T01:00:00Z"},
            {"name": "Test 2", "status": "fail", "execution_time": 2.5, "timestamp": "2025-01-24T01:10:00Z"}
        ]

    def tearDown(self):
        """Clean up temporary output files safely."""
        for file in [self.csv_file, self.json_file, self.md_file, self.xlsx_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_csv_exporter(self):
        """Test CSVExporter correctly exports test results."""
        exporter = CSVExporter(self.csv_file)
        exporter.export(self.test_results)
        self.assertTrue(os.path.exists(self.csv_file))

    def test_json_exporter(self):
        """Test JSONExporter correctly exports test results."""
        exporter = JSONExporter(self.json_file)
        exporter.export(self.test_results)
        self.assertTrue(os.path.exists(self.json_file))

        with open(self.json_file, "r") as file:
            data = json.load(file)
            self.assertEqual(len(data["test_cases"]), 2)

    def test_markdown_exporter(self):
        """Test MarkdownExporter correctly exports test results."""
        exporter = MarkdownExporter(self.md_file)
        exporter.export(self.test_results)
        self.assertTrue(os.path.exists(self.md_file))

    def test_excel_exporter(self):
        """Test ExcelExporter correctly exports test results."""
        exporter = ExcelExporter(self.xlsx_file)
        exporter.export(self.test_results)
        self.assertTrue(os.path.exists(self.xlsx_file))


if __name__ == "__main__":
    unittest.main()
