import requests

def search_photos(query, client_id, per_page=10):
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": per_page,
        "client_id": client_id
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for photo in data['results']:
            print("Photo ID:", photo['id'])
            print("Description:", photo['description'])
            print("URL:", photo['urls']['regular'])
            print("Likes:", photo['likes'])
            print("User:", photo['user']['username'])
            print()
    else:
        print("Failed to fetch photos. Status code:", response.status_code)

# Example usage
query = input("Enter a search query: ")
client_id = "YOUR_ACCESS_KEY"  # Replace 'YOUR_ACCESS_KEY' with your actual Unsplash access key
search_photos(query, client_id)
