import grpc
from concurrent import futures
import time
import door_pb2
import door_pb2_grpc
from google.protobuf.empty_pb2 import Empty

# define the state machine states and operations
transitions = {
    'Closed' : {'OP': 'Openning'},
    'Openning': {'OP': "Opened"},
    'Opened': {'CL' : 'Closing'},
    'Closing': {'OP': 'Openning', 'CL': 'Closed'}
}   

# define the messages 
SUCCESS = "State Change Successed"
ERROR = "State Change Failed"

class FiniteStateMachine:
    # Add code to implement the door FSM
    
    # init 
    def __init__(self, transitions, initial_state):
        # states and operations
        self.transitions = transitions
        # current state
        self.current_state = initial_state

    # funtion to change the state
    def trigger(self, event):
        # check the event can be done to current state and change
        if event in self.transitions[self.current_state]:

            # change the current state with respect to a operation
            self.current_state = self.transitions[self.current_state][event]
            return True

        else:
            return False

    # function to get the current state 
    def getCurrentState(self):
        return self.current_state
    

class DoorServicer(door_pb2_grpc.DoorServicer):
    def __init__(self, fsm):
        self.fsm = fsm

    # Add code to implement RPCs
    def ProcessEvent(self, request, context):
        # create Responce
        response = door_pb2.Response(message="")
        
        # if the state transition success
        if (self.fsm.trigger(request.event)):
            response.message = SUCCESS
        else:
        # the state transition fails
            response.message = ERROR

        # return response
        return response

    def GetCurrentState(self, request, context):
        # return current state
        return door_pb2.CurrentStateResponse(current_state = self.fsm.getCurrentState())

def serve():
    fsm = FiniteStateMachine(transitions, 'Closed')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    door_pb2_grpc.add_DoorServicer_to_server(
        DoorServicer(fsm), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started. Listening on port 50051.")
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(None)

if __name__ == '__main__':
    serve()
