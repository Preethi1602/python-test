import urllib
import time
from wsgiref.simple_server import make_server


API_ENDPOINTS = [
    'https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/albums',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/photos'
]
def make_api_call(url):
    start_time = time.time()
    response = urllib.request.urlopen(url)
    end_time = time.time()
    response_time = end_time - start_time
    return response, response_time

if __name__ == '__main__':    
    response_time = {}
    for endpoint in API_ENDPOINTS:
        response_time[endpoint] = make_api_call(endpoint)

    print("Response Time:", response_time, "seconds")
