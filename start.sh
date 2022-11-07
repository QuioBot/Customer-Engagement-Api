#!/bin/bash
uvicorn code.app.sentiment_analyzer.api:app --host 0.0.0.0 --port $PORT