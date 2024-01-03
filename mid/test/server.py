import grpc
from concurrent import futures
import helloworld_pb2
import helloworld_pb2_grpc

class Hello(helloworld_pb2_grpc.HelloServicer):

    def __init__(self):
        pass

    def SayHello(self, request, context):

        return helloworld_pb2.HelloResponse(greeting='hello')
    
class Bye(helloworld_pb2_grpc.ByeServicer):

    def __init__(self):
        pass

    def SayBye(self, request, context):

        return helloworld_pb2.HelloResponse(greeting='bye')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    helloworld_pb2_grpc.add_HelloServicer_to_server(Hello(), server)

    helloworld_pb2_grpc.add_ByeServicer_to_server(Bye(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()