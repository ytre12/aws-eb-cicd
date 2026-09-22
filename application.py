from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from v7hgdxhd Elastic Beanstalk CI-CD verification-2026092216092011332"

if __name__ == "__main__":
    application.run()
