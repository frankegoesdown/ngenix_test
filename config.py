import os
import logging
import tempfile

# logger
logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# constants
ROOT_PATH = os.path.abspath(os.curdir)
COUNT_ZIPS = 50
COUNT_XMLS = 100
ZIP_DIR = os.path.join(tempfile.gettempdir(), 'zips')
CSV_DIR = os.path.join(tempfile.gettempdir(), 'csvs')
LEVELS_CSV = '{}/{}'.format(CSV_DIR, 'levels.csv')
OBJECTS_CSV = '{}/{}'.format(CSV_DIR, 'objects.csv')
