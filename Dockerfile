# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# COPY ./config.json /code/config.json
  

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

EXPOSE 8080
# 
# RUN python app/bin/download_model

# CMD uvicorn app.sentiment_analyzer.api:app --host 0.0.0.0 --port 8000

# CMD ["uvicorn", "app.sentiment_analyzer.api:app", "--host", "0.0.0.0", "--port", $PORT]

CMD ["uvicorn", "app.sentiment_analyzer.api:app"]
