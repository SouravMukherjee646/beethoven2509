# pip install requests
import requests
baseUrl = 'https://jsonplaceholder.typicode.com'
posts_response = requests.get(f'{baseUrl}/posts')
posts = posts_response.json()
print(posts)