# 
FROM python:3.9

# 
# WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

COPY ./config.json /code/config.json

COPY ./start.sh /code/start.sh
  
RUN chmod +x /code/start.sh

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
#RUN python app/bin/download_model


# CMD ["uvicorn", "app.sentiment_analyzer.api:app", "--host", "0.0.0.0", "--port", "8007"]

CMD ["./start.sh"]