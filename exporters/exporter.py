from typing import Protocol, List, Dict


class Exporter(Protocol):
    """Interface for different export formats."""

    def export(self, test_results: List[Dict]) -> str:
        """Exports test results and returns the output file path.

        Args:
            test_results (List[Dict]): List of test result dictionaries.

        Returns:
            str: Path to the exported file.
        """
        ...
