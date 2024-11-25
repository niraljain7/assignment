# Setup
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

Place the .env file in app folder

Run - gunicorn -w 2 -k uvicorn.workers.UvicornWorker main:app
