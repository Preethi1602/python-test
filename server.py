import requests
import time
from wsgiref.simple_server import make_server

def make_api_call(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    response_time = end_time - start_time
    return response, response_time

if __name__ == '__main__':    
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response, response_time = make_api_call(api_url)

    print("Response Time:", response_time, "seconds")
