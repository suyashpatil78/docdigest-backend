from flask_apscheduler import APScheduler
import os
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def self_ping():
    try:
        url = os.getenv("SELF_URL")
        headers = {"User-Agent": "KeepAliveBot/1.0"}
        if url:
            logger.info(f"Pinging {url}")
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                logger.warning(f"Unexpected status code: {response.status_code}")
        else:
            logger.warning("SELF_URL not set.")
    except Exception as e:
        logger.error(f"Ping failed: {e}")

def init_scheduler(app):
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    scheduler.add_job(
        id='self_ping_job',
        func=self_ping,
        trigger='interval',
        minutes=10
    )
    return scheduler 