import grpc

import state_pb2
import state_pb2_grpc

def trigger(stub, state):
    
        return stub.trigger(state)
 
def client():

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = state_pb2_grpc.StateMachineStub(channel)

        run = state_pb2.TriggerRequest(state='run')
        stop = state_pb2.TriggerRequest(state='stop')
        stopped = state_pb2.TriggerRequest(state='stopped')

        trigger(stub, run)
        trigger(stub, stop)
        trigger(stub, stopped)

if __name__ == '__main__':
    client()