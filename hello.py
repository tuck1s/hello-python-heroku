from flask import Flask, request, Response, make_response
import json, requests, os
from pprint import pprint
app = Flask(__name__)
#
# Flask entry points
#
@app.route('/', defaults={'path': ''},  methods = ['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def handle_all(path):
    print(request.method, path)
    try:
        host = os.environ["SPARKPOST_HOST"]
    except:
        host='https://api.sparkpost.com/'
    if not host.endswith('/'):
        host += '/'

    # Copy across selected headers when making the request in to SparkPost.  Content-Length, Host deliberately not copied.
    reqHeaders = {}
    for i in request.headers:
        if i[0] in ['Authorization', 'Content-Type', 'Accept', 'Accept-Encoding', 'Connection', 'Transfer-Encoding']:
            reqHeaders[i[0]] = i[1]
    fullUrl = host + path
    print('SparkPost request:', request.method, fullUrl, end='')
    if request.args:
        print(' Args: ', end='')
        pprint(request.args)
    else:
        print(' ', end='')
    print('body len =', len(request.data))

    sparkyResponse = requests.request(request.method, url=fullUrl, params=request.args, headers=reqHeaders, data=request.data)
    clientResponse = make_response(sparkyResponse.content, sparkyResponse.status_code)
    # Copy back headers from SparkPost response.  Don't copy certain headers that will be set by Flask response handler.
    for k, v in sparkyResponse.headers.items():
        if not k in ['Content-Encoding', 'Content-Length', 'Transfer-Encoding']:
            clientResponse.headers[k] = v
    print('Sending response:', clientResponse.status_code, 'body len =',len(clientResponse.get_data()), 'headers =', len(clientResponse.headers))
    return clientResponse

# Start the app
if __name__ == "__main__":
    app.run(debug=True)