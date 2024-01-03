import grpc

import state_pb2
import state_pb2_grpc

def trigger(stub, state):
    
        return stub.trigger(state)

def get_current_state(stub, void):
     
     return stub.getState(void)
 
def client():

    with grpc.insecure_channel("localhost:50051") as channel:
        stub = state_pb2_grpc.StateMachineStub(channel)

        run = state_pb2.TriggerRequest(state='run')
        stop = state_pb2.TriggerRequest(state='stop')
        stopped = state_pb2.TriggerRequest(state='stopped')

        void = state_pb2.VoidRequest()

        current_state = get_current_state(stub, void)
        print(current_state)

        trigger(stub, run)
        current_state = get_current_state(stub, void)
        print(current_state)

        trigger(stub, stop)
        current_state = get_current_state(stub, void)
        print(current_state)
        
        trigger(stub, stopped)

        current_state = get_current_state(stub, void)
        print(current_state)

if __name__ == '__main__':
    client()
