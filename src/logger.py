
import logging
import os
from datetime import datetime

# Create logs folder if it doesn't exist
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file name with date
LOG_FILE = f"log_{datetime.now().strftime('%Y_%m_%d')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

# Logger configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,  # you can change to DEBUG, ERROR etc.
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Create a logger instance
logger = logging.getLogger(__name__)

# Example usage
if __name__ == "__main__":
    logger.info("Logger initialized successfully!")
    try:
        x = 10 / 0
    except Exception as e:
        logger.error(f"Error occurred: {e}")
