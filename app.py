from flask import flask
import os
app = Flask(__name__)
@app.route("/")
def home():
  version = os.getenv9("APP_VERSION"."v1.0)
  return f"<h1>Hello Students! Running Container Build:{version}</h1>
  if __name__ == "__main__":
  app.run(host="0.0.0.0",port=50000)
