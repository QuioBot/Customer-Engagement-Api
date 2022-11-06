
# FROM python:3.9
# WORKDIR /code
# COPY ./requirements.txt /code/requirements.txt
# COPY ./config.json /code/config.json
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app
# RUN python app/bin/download_model
# CMD ["uvicorn", "app.sentiment_analyzer.api:app", "--host", "0.0.0.0", "--port", "80"]


FROM python:3.9
COPY ./requirements.txt /requirements.txt
COPY ./start.sh /start.sh
COPY ./download_model /download_model
COPY ./config.json /code/config.json
RUN pip install -r /requirements.txt
RUN python /download_model
RUN chmod +x /start.sh
COPY ./app /app
CMD ["./start.sh"]