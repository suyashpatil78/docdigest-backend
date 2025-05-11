from flask import Flask, jsonify, request
from routes.summarize import summarize_bp
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

limiter = Limiter(
    get_remote_address,
    app=app, 
    storage_uri=os.getenv("REDIS_URI"), 
    default_limits=["50 per hour"],
    # Skip OPTIONS requests for CORS preflight
    application_limits=[],
    default_limits_exempt_when=lambda: request.method == 'OPTIONS'
)

# Custom error handler for 429 errors
@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        "error": "Rate limit exceeded",
        "message": "You have exceeded the allowed number of requests. Please try again later.",
        "retry_after": e.description
    }), 429

app.register_blueprint(summarize_bp, url_prefix='/api/summarize')

if __name__ == '__main__':
    app.run(debug=True)