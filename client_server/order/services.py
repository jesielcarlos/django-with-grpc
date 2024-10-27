from order.repositories.order_repository import OrderRepository
from order.protos.client_grpc import UserGrpcClient

class OrderService:
    def __init__(self):
        self.repository = OrderRepository()
        self.user_client = UserGrpcClient()

    def create_order(self, user_id: int, items: list):
        user = self.user_client.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        return self.repository.create(user_id, items)

    def get_order(self, order_id: int):
        order = self.repository.get_by_id(order_id)
        if not order:
            raise ValueError("Order not found")
        return self.repository.get_by_id(order_id)
