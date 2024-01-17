import requests

url = 'http://127.0.0.1:5000/api/completion'
data = {'text': 'can you hear me?.'}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print("Input Text:", result['input_text'])
    print("Output Text:", result['output_text'])
else:
    print("Error:", response.text)
