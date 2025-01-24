import logging
from typing import List, Dict


class MetricsCalculator:
    """Calculates various test metrics from test results."""

    @staticmethod
    def calculate(test_results: List[Dict]) -> Dict[str, int]:
        """Calculates and returns test execution metrics.

        Args:
            test_results (List[Dict]): List of test result dictionaries.

        Returns:
            Dict[str, int]: A dictionary containing various test execution metrics.
        """
        total_tests = len(test_results)
        passed_tests = sum(1 for test in test_results if test.get("status") == "pass")
        failed_tests = sum(1 for test in test_results if test.get("status") == "fail")
        execution_times = [test.get("execution_time", 0) for test in test_results]

        metrics = {
            "Total Tests": total_tests,
            "Passed Tests": passed_tests,
            "Failed Tests": failed_tests,
            "Average Execution Time": sum(execution_times) / total_tests if total_tests else 0,
            "Min Execution Time": min(execution_times, default=0),
            "Max Execution Time": max(execution_times, default=0)
        }

        logging.info("📊 Calculated test metrics:")
        for key, value in metrics.items():
            logging.info(f"{key}: {value}")

        return metrics
