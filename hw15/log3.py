import logging


logger = logging.getLogger('My Logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('user_actions.log')
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - '
                              '%(levelname)s - %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


def log_user_action2(action: str, level: str = "INFO"):
    if level.upper() == "INFO":
        logger.info(action)
    elif level.upper() == "ERROR":
        logger.error(action)
    elif level.upper() == "WARNING":
        logger.warning(action)
    else:
        logger.debug(action)


log_user_action2("User Log in", "INFO")
log_user_action2("Incorrect password during log in", "ERROR")
log_user_action2("User is not in DB", "WARNING")
