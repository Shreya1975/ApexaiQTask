"""
REST API Interaction Example using the JSONPlaceholder Fake API.

This script demonstrates basic CRUD (Create, Read, Update, Delete) operations 
using the `requests` library in Python. The API used here is a public 
testing API — https://jsonplaceholder.typicode.com — which allows 
you to experiment with REST endpoints.

Functions Included:
- get_user(user_id): Fetch details of a specific user.
- create_post(title, body, user_id): Create a new post for a user.
- update_post(post_id, new_title): Update an existing post.
- delete_post(post_id): Delete a post by ID.

Example Usage:
    python api_example.py
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    """
    Fetch user details by ID from the JSONPlaceholder API.

    Parameters
    ----------
    user_id : int
        The ID of the user to fetch.

    Returns
    -------
    None
        Prints user details if successful, or an error message otherwise.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 200:
        print("✅ User Details:", response.json())
    else:
        print("❌ Failed to fetch user")


def create_post(title, body, user_id):
    """
    Create a new post for a given user.

    Parameters
    ----------
    title : str
        Title of the post.
    body : str
        Content of the post.
    user_id : int
        ID of the user creating the post.

    Returns
    -------
    None
        Prints confirmation and created post data if successful.
    """
    data = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=data)
    if response.status_code == 201:
        print("✅ Post Created:", response.json())
    else:
        print("❌ Failed to create post")


def update_post(post_id, new_title):
    """
    Update the title of an existing post.

    Parameters
    ----------
    post_id : int
        ID of the post to update.
    new_title : str
        New title to assign to the post.

    Returns
    -------
    None
        Prints confirmation and updated post data if successful.
    """
    data = {"title": new_title}
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    if response.status_code == 200:
        print("✅ Post Updated:", response.json())
    else:
        print("❌ Failed to update post")


def delete_post(post_id):
    """
    Delete a post by its ID.

    Parameters
    ----------
    post_id : int
        ID of the post to delete.

    Returns
    -------
    None
        Prints a confirmation message if deletion is successful.
    """
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code in (200, 204):
        print("✅ Post Deleted Successfully")
    else:
        print("❌ Failed to delete post")


# ------------------- Example Usage -------------------
if __name__ == "__main__":
    print("🔹 Fetching user with ID=1")
    get_user(1)

    print("\n🔹 Creating a new post")
    create_post("My First API Post", "This is a test post via REST API.", 1)

    print("\n🔹 Updating post with ID=1")
    update_post(1, "Updated Title from Python API")

    print("\n🔹 Deleting post with ID=1")
    delete_post(1)
