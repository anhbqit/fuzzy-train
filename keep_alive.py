from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    # This is what you'll see when you visit your Render URL
    return "Hermes Agent is online and listening!"

def run():
    # Render assigns a dynamic port via the PORT environment variable.
    # We default to 10000 for local testing.
    port = int(os.environ.get("PORT", 10000))
    # Must bind to 0.0.0.0 so Render can route external traffic to it
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    """Starts the Flask server on a separate thread so it doesn't block the bot."""
    server = Thread(target=run)
    server.start()
