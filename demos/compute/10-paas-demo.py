# Deploys a Flask app to AWS Elastic Beanstalk (eb init & eb deploy required)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Main route returns a simple string response
    return "Hello from Elastic Beanstalk!"

if __name__ == "__main__":
    app.run()