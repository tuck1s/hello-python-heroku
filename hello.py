from flask import Flask, Response
app = Flask(__name__)
#
# Flask entry points
#
@app.route('/')
def hello_world():
    print('Got a request')
    return 'Hello, World!'


# Start the app
if __name__ == "__main__":
    app.run(debug=True)
