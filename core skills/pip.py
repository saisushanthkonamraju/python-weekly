# Using external libraries installed with pip

# Command to install requests:
# pip install requests

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # 1. Simple GET request
    response = requests.get(url, timeout=5)
    print("Status code:", response.status_code)
    
    if response.status_code == 200:
        data = response.json()
        print("Post Title:", data.get("title"))

    # 2. Simple POST request
    payload = {"title": "Python Practice", "body": "Testing API", "userId": 1}
    post_res = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, timeout=5)
    print("Created ID:", post_res.json().get("id"))

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
