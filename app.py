from flask import Flask, render_template
from routes.api import api_bp

app = Flask(__name__)

# Register API blueprint
app.register_blueprint(api_bp, url_prefix="/api")

# Route for main page
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
