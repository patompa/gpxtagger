from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
  with open("index.html") as f:
    return f.read()

@app.route("/map/<map>")
def get_map(map):
  return send_file(f'maps/{map}.png', mimetype='image/png')

@app.route("/coord/<map>")
def get_coord(map):
  return send_file(f'maps/{map}.json', mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True,port=8081)
