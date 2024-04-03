from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/submit_form', methods=['GET'])
def submit_form():
    data = request.json  # Assuming JSON data is submitted from the frontend
    print(data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
