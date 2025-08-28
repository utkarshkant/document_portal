import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir = 'logs'):

        # ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # create timestamped log file name
        LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
        LOG_FILE_PATH = os.path.join(self.logs_dir, LOG_FILE)

        # configure logging
        logging.basicConfig(
            filename=LOG_FILE_PATH,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )

    def get_logger(self, name:__file__):
        return logging.getLogger(os.path.basename(name))
    

if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("second log for testing")