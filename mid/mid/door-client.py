# E number - E/19/129
# Name - K.H. Gunawardana

import grpc
import door_pb2
import door_pb2_grpc
from google.protobuf.empty_pb2 import Empty


# function for process the event
def process_event(stub, event):
    return stub.ProcessEvent(event)

# funtion for get the current state
def get_current_state(stub):
    return stub.GetCurrentState(Empty())

def run_client(events):
    channel = grpc.insecure_channel('localhost:50051')
    stub = door_pb2_grpc.DoorStub(channel)

    # Add code to call the server
    # create an Event
    eventObj = door_pb2.Event(event="")

    # loop throught the list of state changes
    for i in events:
        eventObj.event = i

        # change the state
        process_event(stub, eventObj)

    # get the final state
    final = get_current_state(stub)

    print("The final state: "+ final.current_state)

if __name__ == '__main__':
    events = ["OP", "OP", "CL", "OP"]
    run_client(events)
