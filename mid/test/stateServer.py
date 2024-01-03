import grpc
from concurrent import futures

import state_pb2
import state_pb2_grpc

transitions = {

    'start': {'run': 'running'},

    'running': {'stop': 'stopping'},

    'stopping': {'stop': 'stopping', 'stopped': 'start'}

}

class StateMachine(state_pb2_grpc.StateMachineServicer):

    def __init__(self, transitions, initial_state):

        self.transitions = transitions

        self.current_state = initial_state

    def trigger(self, request, context):
        print(self.current_state, end=' ')
        
        if request.state in self.transitions[self.current_state]:

            self.current_state = self.transitions[self.current_state][request.state]

            print(self.current_state)
            return state_pb2.TriggerResponse(success=True)

        else:
            print(self.current_state)
            return state_pb2.TriggerResponse(success=False)
        

    def getState(self, request, context):
        return state_pb2.StateResponse(state=self.current_state)
        

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    state_pb2_grpc.add_StateMachineServicer_to_server(StateMachine(transitions, 'start'), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started on port 50051...')
    server.wait_for_termination()

if __name__ == '__main__':
    server()
