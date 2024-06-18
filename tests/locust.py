from locust import HttpUser, TaskSet, task, between


class TaskBehavior(TaskSet):

    @task(1)
    def home(self):
        self.client.get("/")

    @task(2)
    def add_task(self):
        self.client.post("/tasks", json={"task_id": "1", "description": "Test task"})

    @task(3)
    def get_task(self):
        self.client.get("/tasks/1")

    @task(4)
    def remove_task(self):
        self.client.delete("/tasks/1")


class WebsiteUser(HttpUser):
    tasks = [TaskBehavior]
    wait_time = between(1, 5)
