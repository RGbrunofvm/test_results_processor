import logging
from exporters.exporter import Exporter
from utils.json_loader import JSONLoader
from utils.logging_config import configure_logging
from utils.metrics_calculator import MetricsCalculator


class Processor:
    """Orchestrates the loading, processing, and exporting of test results."""

    def __init__(self, json_file: str, output_path: str, exporter: Exporter, include_metrics: bool = True):
        """Initializes the processor with a dynamic exporter.

        Args:
            json_file (str): Path to the JSON file containing test results.
            output_path (str): Path to the output file.
            exporter (Exporter): Exporter instance (CSV, JSON, Markdown).
            include_metrics (bool, optional): Whether to calculate and log test metrics. Defaults to True.
        """
        configure_logging()  # Configure logging at startup
        self.loader = JSONLoader(json_file)
        self.exporter = exporter
        self.include_metrics = include_metrics
        self.test_results = self.loader.load()

    def run(self):
        """Executes the full process: loads test results, exports them, and calculates metrics."""
        if not self.test_results:
            logging.warning("No test results to process. Exiting.")
            return

        export_path = self.exporter.export(self.test_results)
        logging.info(f"Test results exported to: {export_path}")

        if self.include_metrics:
            metrics = MetricsCalculator.calculate(self.test_results)
            logging.info("Metrics Summary:")
            for key, value in metrics.items():
                logging.info(f"{key}: {value}")
