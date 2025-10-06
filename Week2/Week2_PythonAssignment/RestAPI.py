import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_all_posts():
    """
    Fetch all posts from JSONPlaceholder API
    Returns a list of posts if successful, else returns an empty list
    """
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()  # Raise error for bad status
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching posts:", e)
        return []

def get_post(post_id):
    """
    Fetch a single post by its ID
    Returns a dictionary if found, else None
    """
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching post {post_id}:", e)
        return None

if __name__ == "__main__":
    posts = get_all_posts()
    print(f"Total posts fetched: {len(posts)}\n")

    if posts:
        print("First 5 posts in readable format:\n")
        for post in posts[:5]:
            print(f"ID: {post['id']}")
            print(f"UserID: {post['userId']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}\n")
    
    post = get_post(1)
    if post:
        print("Post with ID 1:\n")
        print(f"ID: {post['id']}")
        print(f"UserID: {post['userId']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
