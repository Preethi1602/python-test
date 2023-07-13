import requests
import time

def make_api_call(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    return response, response_time

# Example usage
api_url = "https://jsonplaceholder.typicode.com/posts"
response, response_time = make_api_call(api_url)

print("Response Status Code:", response.status_code)
print("Response Time:", response_time, "seconds")
