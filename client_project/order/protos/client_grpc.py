import grpc
from order.protos import user_pb2, user_pb2_grpc


class UserGrpcClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = user_pb2_grpc.UserServiceStub(self.channel)

    def get_user_by_id(self, user_id: int):
        request = user_pb2.UserIdRequest(user_id=user_id)
        return self.stub.GetUserById(request)
