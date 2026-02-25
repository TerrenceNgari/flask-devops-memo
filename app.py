from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps is working!"

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/version")
def version():
    return jsonify({
        "app": "flask-devops-demo",
        "version": "1.0.0"
    })

@app.route("/api/users")
def users():
    return jsonify([
        {"id": 1, "name": "Terrence"},
        {"id": 2, "name": "DevOps Engineer"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)