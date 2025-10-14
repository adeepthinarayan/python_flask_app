from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>Hello, World!</p>"

@app.route("/services")
def services():
    return "<p>Version 1</p>"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)