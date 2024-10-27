from order.models import Order

class OrderRepository:
    def get_by_id(self, order_id: int):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    def create(self, user_id: int, items: list):
        order = Order(user_id=user_id, items=items)
        order.save()
        return order
