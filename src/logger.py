'''logger such a file is used for logging events, errors, or debugging information 
in a Python program.'''

import logging
from datetime import datetime
import os

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) ## it create the path of logfile it means inside the logs directory find log file
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
   filename=LOG_FILE_PATH,
   format= "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
   level=logging.INFO,
)

