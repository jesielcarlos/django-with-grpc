from concurrent import futures
import grpc
from threading import Thread
from core.grpc import user_pb2_grpc, user_pb2
from core.models import CustonUsers


class UserServiceServicer(user_pb2_grpc.UserServiceServicer):
    def GetUserById(self, request, context):
        try:
            print("REQUEST=", request.user_id)
            user = CustonUsers.objects.get(id=request.user_id)
            print("USER=", user)
            return user_pb2.UserResponse(
                user_id=user.id,
                name=user.name,
                email=user.email
            )
        except CustonUsers.DoesNotExist:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.UserResponse()


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()



