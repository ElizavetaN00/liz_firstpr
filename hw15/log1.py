import logging


logging.basicConfig(
    filename='user_actions.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def log_user_action(action: str, level: str = "INFO"):
    if level.upper() == "INFO":
        logging.info(action)
    elif level.upper() == "ERROR":
        logging.error(action)
    elif level.upper() == "WARNING":
        logging.warning(action)
    else:
        logging.debug(action)


log_user_action("User Log in", "INFO")
log_user_action("Incorrect password during log in", "ERROR")
log_user_action("User is not in DB", "WARNING")
