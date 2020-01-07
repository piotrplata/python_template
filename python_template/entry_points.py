from logging_manager import get_logger
import python_template

_logger = get_logger(logger_name=__name__)


def run():
    _logger.info(python_template.VERSION)
    _logger.info("running script")
