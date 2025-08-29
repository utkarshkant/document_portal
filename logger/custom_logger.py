import logging
import structlog
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
# Exception logger with streaming handler using structlog for JSON structured logging
class CustomLogger:
    def __init__(self, log_dir = "logs"):
        
        # ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # create timestamped log file name
        log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

    def get_logger(self, name = __file__):
        
        logger_name = os.path.basename(name)

        # configure logger for console & log-file (in JSON format)
        file_handler = logging.FileHandler(self.log_file_path)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter("%(message)s"))
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(logging.Formatter("%(message)s"))

        logging.basicConfig(
            level=logging.INFO,
            format="%(message)s",
            handlers=[file_handler, console_handler],
        )

        # configure structlog for JSON structured logging
        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso", utc=True, key="timestamp"),
                structlog.processors.add_log_level,
                structlog.processors.EventRenamer(to="event"),
                structlog.processors.JSONRenderer()
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            cache_logger_on_first_use=True,
        )

        return structlog.get_logger(logger_name)
    
# Usage example
if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("custom logger initialized with structlog and stream handler .")
