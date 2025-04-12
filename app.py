from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello user, CI/CD!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT isn't set
    app.run(host='0.0.0.0', port=port)
