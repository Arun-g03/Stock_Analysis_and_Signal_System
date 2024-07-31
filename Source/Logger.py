# logger.py

import logging
from config.config import LOG_PATH

class System_Log:
    @staticmethod
    def setup_logger(name, log_file, level=logging.INFO):
        """
        Setup a logger with the specified name and log file.
        """
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

# Example usage:
# system_logger = System_Log.setup_logger('main_logger', LOG_PATH)
# system_logger.info('This is an informational message')
# system_logger.error('This is an error message')
