import logging 
logger=logging.getLogger("Security monitor")
logger.setLevel(logging.DEBUG)
logger.propagate=False
stream_handler=logging.StreamHandler()
file_handler=logging.FileHandler("security.log")
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.debug("Checking network configuration")
logger.info("Security monitoring started")
logger.warning("Multiple failed login attempts")
logger.error("Unauthorized access detected")
logger.critical("Critical security breach")