import grpc
import tasks_pb2
import tasks_pb2_grpc

def create_task(stub, task):
    # Implement logic to send a request to create a new task.
    return stub.CreateTask(task)

def get_task(stub, task_id):

    # Implement logic to send a request to retrieve a task by its ID.
    taskId = tasks_pb2.TaskId(id=task_id)

    return stub.GetTask(taskId)

def update_task(stub, task):
    # Implement logic to send a request to update an existing task.
    return stub.UpdateTask(task)

def delete_task(stub, task_id):
    # Implement logic to send a request to delete a task by its ID.

    taskId = tasks_pb2.TaskId(id=task_id)
    
    return stub.DeleteTask(taskId)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tasks_pb2_grpc.TaskServiceStub(channel)

        # Example usage:
        task = tasks_pb2.Task(id="1", title="Task 1", description="Description 1")

        # Create Task
        created_task = create_task(stub, task)
        print("Created Task:", created_task)

        # Get Task
        retrieved_task = get_task(stub, task.id)
        print("Retrieved Task:", retrieved_task)

        # Update Task
        task.description = "Updated Description"
        updated_task = update_task(stub, task)
        print("Updated Task:", updated_task)

        # Delete Task
        delete_response = delete_task(stub, task.id)
        print("Delete Response:", delete_response)

if __name__ == '__main__':
    run()
