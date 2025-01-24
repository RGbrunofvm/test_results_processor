import unittest
from utils.metrics_calculator import MetricsCalculator


class TestMetricsCalculator(unittest.TestCase):
    """Tests for the MetricsCalculator class."""

    def test_calculate_metrics(self):
        """Test correct calculation of metrics from test results."""
        test_results = [
            {"name": "Test 1", "status": "pass", "execution_time": 1.2, "timestamp": "2025-01-24T01:00:00Z"},
            {"name": "Test 2", "status": "fail", "execution_time": 2.5, "timestamp": "2025-01-24T01:10:00Z"},
            {"name": "Test 3", "status": "pass", "execution_time": 1.0, "timestamp": "2025-01-24T01:20:00Z"}
        ]

        metrics = MetricsCalculator.calculate(test_results)
        self.assertEqual(metrics["Total Tests"], 3)
        self.assertEqual(metrics["Passed Tests"], 2)
        self.assertEqual(metrics["Failed Tests"], 1)
        self.assertAlmostEqual(metrics["Average Execution Time"], 1.566, places=2)
        self.assertEqual(metrics["Min Execution Time"], 1.0)
        self.assertEqual(metrics["Max Execution Time"], 2.5)


if __name__ == "__main__":
    unittest.main()
