import grpc
from concurrent import futures
import tasks_pb2
import tasks_pb2_grpc

class TaskService(tasks_pb2_grpc.TaskServiceServicer):
    def __init__(self):
        self.tasks = []

    def CreateTask(self, request, context):
        # Generate a unique ID (you might use a library like UUID in a real-world scenario)
        new_id = str(len(self.tasks) + 1)
        request.id = new_id

        # Add the new task to the list
        self.tasks.append(request)

        # Return the created task
        return request

    def GetTask(self, request, context):
        # Implement logic to retrieve a task by its ID and return it.
        for i in self.tasks:
            if i.id == request.id:
                # Return the found task
                return i

        return None

    def UpdateTask(self, request, context):
        # Implement logic to update an existing task and return the updated task.
        for i in range(len(self.tasks)):
            if self.tasks[i].id == request.id:
                # Update task title and description
                self.tasks[i].title = request.title
                self.tasks[i].description = request.description
                # Return the updated task
                return self.tasks[i]

        # If task with the given ID not found, return the original request
        return request

    def DeleteTask(self, request, context):
        # Implement logic to delete a task by its ID and return the result.
        for i in range(len(self.tasks)):
            if self.tasks[i].id == request.id:
                # Delete the task from the list
                del self.tasks[i]
                # Return a success response
                return tasks_pb2.DeleteTaskResponse(success=True)

        # If task with the given ID not found, return a failure response
        return tasks_pb2.DeleteTaskResponse(success=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tasks_pb2_grpc.add_TaskServiceServicer_to_server(TaskService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
