from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/geminipage")
def geminipage():
    return render_template("geminipage.html")

if __name__ == "__main__":
    app.run(debug=True)
