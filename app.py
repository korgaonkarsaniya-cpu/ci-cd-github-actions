from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Dockerized Web Application</title>
        </head>
        <body>
            <h1>Hello! 👋</h1>
            <h2>This is my CI/CD GitHub Actions Application</h2>
            <p>Project created for my internship.</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)