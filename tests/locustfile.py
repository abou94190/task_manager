from locust import HttpUser, task, between


class TaskManagerUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_home_page(self):
        self.client.get("/")

    @task
    def create_task(self):
        self.client.post("/tasks", json={"title": "New Task", "description": "Task description"})

    @task
    def get_tasks(self):
        self.client.get("/tasks")

    @task
    def update_task(self):
        self.client.put("/tasks/1", json={"title": "Updated Task", "description": "Updated description"})

    @task
    def delete_task(self):
        self.client.delete("/tasks/1")
