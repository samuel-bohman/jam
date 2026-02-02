import requests
import json
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

API_KEY = "your_api_key_here"
BASE_URL = "base_url_here"
MODEL="openai/gpt-oss-20b"

message_content = "Suggest a short recipe for american pancakes"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

response=requests.post(
    url=BASE_URL,
    json={"model": MODEL,"messages":[{"content":message_content,"role":"user"}],"stream":True},
    headers=headers,
    verify=False,
    stream=True)

# Process the streamed response
for line in response.iter_lines():
    if line:
        line_str = line.decode('utf-8')
        if line_str.startswith('data: '):
            data_str = line_str[6:]  # Remove 'data: ' prefix
            if data_str.strip() != '[DONE]':
                try:
                    chunk = json.loads(data_str)
                    content = chunk['choices'][0]['delta'].get('content', '')
                    if content:
                        print(content, end='', flush=True)
                except json.JSONDecodeError:
                    pass

# from datetime import datetime
# start_time = datetime.now()
# for line in response.iter_lines():
#     if line:
#         line_str = line.decode('utf-8')
#         if line_str.startswith('data: '):
#             data_str = line_str[6:]
#             if data_str.strip() != '[DONE]':
#                 try:
#                     chunk = json.loads(data_str)
#                     content = chunk['choices'][0]['delta'].get('content', '')
#                     if content:
#                         elapsed = (datetime.now() - start_time).total_seconds()
#                         print(f"\n[{elapsed:.2f}s] {content}", end='', flush=True)
#                 except json.JSONDecodeError:
#                     pass
