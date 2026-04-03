from python:3.9

WORKDIR /app

copy . /app

run pip install -r requirements.txt

Expose 8501

CMD [ "streamlit","run","app.py", "--server.port=8501","--server.address=0.0.0.0"]