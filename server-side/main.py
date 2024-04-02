from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, origins='*' )

@app.route("/api/users", methods=['GET'])
def users():
    return jsonify(
        {
            "users": [
                'value1',
                'value2', 
                'value3'
            ]
        }
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True, port=8080)


    