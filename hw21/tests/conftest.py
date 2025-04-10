import pytest
from loguru import logger
import sys


def pytest_addoption(parser):
    parser.addoption(
        "--custom-log-level",
        action="store",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    )


@pytest.fixture(scope="session", autouse=True)
def setup_logging(request):
    log_level = request.config.getoption("--custom-log-level")
    logger.remove()
    logger.add(sys.stderr, level=log_level)
    logger.info(f"Setting log level to {log_level}")
