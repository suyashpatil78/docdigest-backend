from flask import Flask, jsonify, request
from routes.summarize import summarize_bp
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
from utils.scheduler import init_scheduler
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri=os.getenv("REDIS_URI"),
    default_limits=["15 per minute"]
)

@limiter.request_filter
def exempt_options():
    return request.method == "OPTIONS"

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "error": "Rate limit exceeded",
        "message": "You have exceeded the allowed number of requests. Please try again later.",
        "retry_after": e.description
    }), 429

# Hack to keep the app alive
scheduler = init_scheduler(app)

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})

app.register_blueprint(summarize_bp, url_prefix='/api/summarize')

if __name__ == '__main__':
    app.run(debug=True)
