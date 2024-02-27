import requests
import os

def search_and_download_photos(query, client_id, download_path, per_page=10):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": per_page,
        "client_id": client_id
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for index, photo in enumerate(data['results']):
            image_url = photo['urls']['regular']
            image_file_path = os.path.join(download_path, f"{query}_{index+1}.jpg")
            download_image(image_url, image_file_path)
    else:
        print("Failed to fetch photos. Status code:", response.status_code)

def download_image(image_url, image_file_path):
    response = requests.get(image_url)

    if response.status_code == 200:
        with open(image_file_path, 'wb') as f:
            f.write(response.content)
        print("Image saved successfully:", image_file_path)
    else:
        print("Failed to download image:", image_url)

# Example usage
query = input("Enter a search query: ")
client_id = "YOUR_ACCESS_KEY"  # Replace 'YOUR_ACCESS_KEY' with your actual Unsplash access key
download_path = "Directory"  # Directory to save downloaded images
if not os.path.exists(download_path):
    os.makedirs(download_path)
search_and_download_photos(query, client_id, download_path)
