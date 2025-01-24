import logging

def configure_logging():
    """Configures logging for the application."""
    logging.basicConfig(
        filename="test_results.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("🚀 Logging configured successfully.")
