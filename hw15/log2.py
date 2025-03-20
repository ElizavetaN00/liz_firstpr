import logging
import logging.handlers as handlers


logger = logging.getLogger('My Logger')
logger.setLevel(logging.DEBUG)
logHandler = (handlers.TimedRotatingFileHandler
              ('user_actions_7.log', when='midnight',
               interval=1, backupCount=7))
logHandler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s '
                              '- %(message)s', datefmt='%Y-%m-%d '
                                                       '%H:%M:%S')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)


def log_user_action1(action: str, level: str = "INFO"):
    if level.upper() == "INFO":
        logger.info(action)
    elif level.upper() == "ERROR":
        logger.error(action)
    elif level.upper() == "WARNING":
        logger.warning(action)
    else:
        logger.debug(action)


log_user_action1("User  Log in", "INFO")
log_user_action1("Incorrect password during log in", "ERROR")
log_user_action1("User  is not in DB", "WARNING")
