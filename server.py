import time
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def make_api_call(url):
    start_time = time.time()
    end_time = time.time()
    response_time = end_time - start_time
    return  response_time

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    
    api_url = "https://jsonplaceholder.typicode.com/posts"
    response_time = make_api_call(api_url)
    print("Response Time:", response_time, "seconds")
    with Configurator() as config:
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
