import requests

database = {
    1: "Gaurav",
    2: "Mishra",
    3: "Arun",
    4: "Sai",
    5: "Varun"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError

