from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  """Example route for the React app."""
  return jsonify({'message': 'Hello from Flask!'})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
