from python_template.logging_manager import get_logger
import python_template

_logger = get_logger(logger_name=__name__)


def run():
    _logger.info(python_template.__version__)
    _logger.info("running script")
