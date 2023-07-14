import time
import os

def make_api_call(url):
    start_time = time.time()
    end_time = time.time()
    response_time = end_time - start_time
    return  response_time

if __name__ == '__main__':    
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response_time = make_api_call(api_url)
    print("Response Time:", response_time, "seconds")
