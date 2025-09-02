from flask import Flask
app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello World from Flask!"

if __name__ == "__main__":
    # Bind to all interfaces, port 8000 (customizable via PORT env)
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
