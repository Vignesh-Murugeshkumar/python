import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')   
logger = logging.getLogger(__name__)
logger.info('This is an info message from helper.py')

stream_handler=logging.StreamHandler()
file_handler=logging.FileHandler('app.log')

stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning message from helper.py')
logger.error('This is an error message from helper.py')
