#/bin/sh
uvicorn app.sentiment_analyzer.api:app --host 0.0.0.0 --port $PORT