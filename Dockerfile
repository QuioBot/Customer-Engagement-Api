# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

COPY ./config.json /code/config.json
  

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
RUN python app/bin/download_model


# CMD ["uvicorn", "app.sentiment_analyzer.api:app", "--host", "0.0.0.0", "--port", "80"]


EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app.sentiment_analyzer.api:app