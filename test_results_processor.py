import argparse
import logging

from exporters.excel_exporter import ExcelExporter
from utils.logging_config import configure_logging
from processors.processor import Processor
from exporters.csv_exporter import CSVExporter
from exporters.json_exporter import JSONExporter
from exporters.markdown_exporter import MarkdownExporter

# Configure logging
configure_logging()


def main():
    parser = argparse.ArgumentParser(description="Process test results and export in different formats.")
    parser.add_argument("json_file", help="Path to the input JSON file")
    parser.add_argument("output_file", help="Path to the output file")
    parser.add_argument("--format", choices=["csv", "json", "md", "xlsx"], default="csv", help="Output format (csv, json, md)")
    args = parser.parse_args()

    # Select the correct exporter based on user choice
    exporters = {
        "csv": CSVExporter,
        "json": JSONExporter,
        "md": MarkdownExporter,
        "xlsx": ExcelExporter
    }

    exporter_class = exporters[args.format](args.output_file)

    processor = Processor(args.json_file, args.output_file, exporter_class)
    processor.run()


if __name__ == "__main__":
    main()
