import logging
import os
from datetime import datetime

# class CustomLogger:
#     def __init__(self, log_dir = 'logs'):

#         # ensure logs directory exists
#         self.logs_dir = os.path.join(os.getcwd(), log_dir)
#         os.makedirs(self.logs_dir, exist_ok=True)

#         # create timestamped log file name
#         LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
#         LOG_FILE_PATH = os.path.join(self.logs_dir, LOG_FILE)

#         # configure logging
#         logging.basicConfig(
#             filename=LOG_FILE_PATH,
#             format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
#             level=logging.INFO,
#         )

#     def get_logger(self, name:__file__):
#         return logging.getLogger(os.path.basename(name))
    
##################################################################################################
# Exception logger with streaming handler
class CustomLogger:
    def __init__(self, log_dir = "logs"):
        
        # ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # create timestamped log file name
        log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name = __file__):
        """
        Returns a logger instance with file + console handlers.
        Default name is the current file name (without path).
        """
        logger_name = os.path.basename(name)
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)

        # formatter for both handlers
        file_formatter = logging.Formatter("[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s")
        console_formatter = logging.Formatter("[ %(levelname)s ] %(message)s")

        # file handler (logs saved to file)
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setFormatter(file_formatter)

        # console handler (logs printed to console)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(console_formatter)

        # Avoid duplicate handlers if logger is reused
        if not logger.hasHandlers():
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
    
# Usage example
if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("custom logger initialized with stream handler.")
