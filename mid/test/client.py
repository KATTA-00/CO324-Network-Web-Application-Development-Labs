import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def say_hello(stub, hello):

    return stub.SayHello(hello)


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.HelloStub(channel)

        response = say_hello(stub, helloworld_pb2.HelloRequest(name='you'))
    
    print("Greeter client received: " + response.greeting)



if __name__ == '__main__':
    run()