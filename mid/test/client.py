import grpc
import helloworld_pb2
import helloworld_pb2_grpc


def say_hello(stub, hello):

    return stub.SayHello(hello)

def say_bye(stub, hello):

    return stub.SayBye(hello)


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub_hello = helloworld_pb2_grpc.HelloStub(channel)
        stub_bye = helloworld_pb2_grpc.ByeStub(channel)


        response = say_hello(stub_hello, helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client hello: " + response.greeting)

        response = say_bye(stub_bye, helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client bye: " + response.greeting)
    



if __name__ == '__main__':
    run()