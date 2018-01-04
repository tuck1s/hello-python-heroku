from flask import Flask, request, Response, make_response
import json, requests
app = Flask(__name__)
#
# Flask entry points
#
@app.route('/', defaults={'path': ''},  methods = ['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/<path:path>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def handle_all(path):
    print(request.method, path)
    r = {
        'method': request.method,
        'path': path,
        'args': request.args,
        'data': request.data.decode('utf-8'),
        'headers': {}
    }
    # Copy across just those headers needed when making the onward request
    for i in request.headers:
        if i[0] in ['Authorization', 'Content-Type', 'Accept']:
            r['headers'].update({i[0]:i[1]})

    res = requests.request(method=r['method'], url='https://api.sparkpost.com/'+path, params=r['args'], headers=r['headers'], data=r['data'])
    t = res.text
    e = res.status_code
    return make_response(t, e)


# Start the app
if __name__ == "__main__":
    app.run(debug=True)
