from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Jenkins CI/CD Pipeline!"

if __name__ == "__main__":
    app.run(debug=True)