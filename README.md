# sanic-greeting-api

A beginner-friendly Sanic API that demonstrates **path parameters** — values embedded directly in the URL.

## Endpoints

| Method | URL | Example |
|--------|-----|---------|
| GET | `/greet/<name>` | `/greet/Joel` |
| GET | `/greet/<name>/<language>` | `/greet/Joel/spanish` |

Supported languages: `english`, `spanish`, `french`, `german`, `japanese`, `swahili`.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:8080/greet/Joel` in your browser.

### Live Demo

[![Run on Codely](https://codely.run/python/static/buttons/run-minimal.svg)](https://codely.run/python/project/sanic-greeting-api)