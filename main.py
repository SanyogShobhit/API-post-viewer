import requests

print(" Fetching posts from API...\n")

user_id = int(input("Enter user ID (1-10): "))

url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": user_id}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    print(f"\n✅ Posts by User {user_id}:\n")
    
    for post in data:
        print(" ID:", post["id"])
        print(" Title:", post["title"])
        print(" Body:", post["body"])
        print("-" * 40)
else:
    print(" Failed to fetch data")