from enum import Enum
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import logging
import logging.handlers as handlers

#1
class OrderStatus(Enum):
    PENDING = "Заказ ожидает обработки"
    IN_PROGRESS = "Заказ готовится"
    READY = "Заказ готов"
    COMPLETED = "Заказ выдан"
    CANCELLED = "Заказ отменён"

class Order:
    def __init__(self, order_id, status=OrderStatus.PENDING):
        self.order_id = order_id
        self.status = status

    def update_status(self, new_status):
        if isinstance(new_status, OrderStatus):
            self.status = new_status
        else:
            raise ValueError("Неверный статус")

    def display_status(self):
        print(f"Order status {self.order_id}: {self.status.value}")

order = Order('127')
order.display_status()
order.update_status(OrderStatus.IN_PROGRESS)
order.display_status()
order.update_status(OrderStatus.READY)
order.display_status()
order.update_status(OrderStatus.COMPLETED)
order.display_status()
order.update_status(OrderStatus.CANCELLED)
order.display_status()

# 2
date1 = input('Enter first date in format "YYYY-MM-DD": ')
date2 = input('Enter second date in format "YYYY-MM-DD": ')

dt1 = parse(date1)
dt2 = parse(date2)
diff = relativedelta(dt2, dt1)
difference_in_days = (dt2 -dt1).days

print(f"Difference between {dt1.date()} and {dt2.date()} is "
      f"{abs(difference_in_days)} day(s)")

# 3
now = datetime.today()
date3 = input('Enter any date in format "YYYY-MM-DD": ')
date3_conversion = datetime.strptime(date3, "%Y-%m-%d")

if date3_conversion > now:
    print("Entered date is a future date")
elif date3_conversion < now:
    print("Entered date is a date from past")
else:
    print("Entered date is current")

# 4
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

# 5
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

def log_user_action(action: str, level: str = "INFO"):
    if level.upper() == "INFO":
        logger.info(action)
    elif level.upper() == "ERROR":
        logger.error(action)
    elif level.upper() == "WARNING":
        logger.warning(action)
    else:
        logger.debug(action)

log_user_action("User  Log in", "INFO")
log_user_action("Incorrect password during log in", "ERROR")
log_user_action("User  is not in DB", "WARNING")

# 6
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

def log_user_action(action: str, level: str = "INFO"):
    if level.upper() == "INFO":
        logger.info(action)
    elif level.upper() == "ERROR":
        logger.error(action)
    elif level.upper() == "WARNING":
        logger.warning(action)
    else:
        logger.debug(action)

log_user_action("User Log in", "INFO")
log_user_action("Incorrect password during log in", "ERROR")
log_user_action("User is not in DB", "WARNING")