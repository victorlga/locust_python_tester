from locust import HttpUser, task, between
import os

# Retrieve the endpoint from the environment variable
API_ENDPOINT = os.getenv("API_ENDPOINT")

class ApiUser(HttpUser):
    # Assuming the endpoint is set in the environment variable
    host = API_ENDPOINT
    wait_time = between(1, 5)  # Simulate wait time between tasks

    @task(2)
    def create_user(self):
        # Define a sample user data
        user_data = {"name": "test_user", "email": "test@example.com"}
        self.client.post("/users/", json=user_data)

    @task(1)
    def get_users(self):
        self.client.get("/users/")

    @task(1)
    def update_user(self):
        # Assuming you have some users, you would update one here
        # For simplicity, using a fixed user_id
        user_id = 1
        updated_user_data = {"name": "updated_user", "email": "updated@example.com"}
        self.client.put(f"/users/{user_id}", json=updated_user_data)

    @task(1)
    def delete_user(self):
        # Again, assuming you have users to delete
        # Using a fixed user_id for simplicity
        user_id = 1
        self.client.delete(f"/users/{user_id}")