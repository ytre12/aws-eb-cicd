from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from v7hgdxhd Elastic Beanstalk CI-CD"

if __name__ == "__main__":
    application.run()
