from enum import Enum


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
