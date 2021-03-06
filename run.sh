export FLASK_APP=gatekeeper
export FLASK_DEBUG=1
# For Python
export PYTHONUNBUFFERED=yes
# For gunicorn
export PORT=9050
# For app's config.py
export LOG_LEVEL=DEBUG
export COMMIT=LOCAL

# Run the app
flask run --host 0.0.0.0 --port 9050
