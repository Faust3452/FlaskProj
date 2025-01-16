from flask import Flask
app = Flask('TEST')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, port=12588)