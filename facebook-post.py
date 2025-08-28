import requests

page_access_token = "your_page_access_token"
page_id = "your_page_id"
message = "Hello Facebook from Python!"

url = f"https://graph.facebook.com/{page_id}/feed"
params = {"message": message, "access_token": page_access_token}

response = requests.post(url, params=params)
print("Post ID:", response.json().get("id"))
