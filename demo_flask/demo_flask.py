from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/install', methods=["POST"])
def post():
    r = request
    request_data = r.get_data()
    print(request_data)
    request_body = r.get_json()
    print(request_body)
    return "hello"


if __name__ == '__main__':
    app.run()