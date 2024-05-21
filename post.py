import requests

headers = {
    'accept': 'application/json',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'uploaded_file': ('9.jpg', open('9.jpg', 'rb'), 'image/jpeg'),
}

response = requests.post('http://127.0.0.1:8000/upload', headers=headers, files=files)
print(response.json())

