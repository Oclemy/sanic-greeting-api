from sanic import Sanic
from sanic.response import json

app = Sanic("greeting-api")


# Path parameter: /greet/<name>
# <name> is a placeholder — Sanic fills it in from the URL
@app.get("/greet/<name>")
async def greet(request, name: str):
    return json({"message": f"Hello, {name}!"})


# Two path parameters: /greet/<name>/<language>
@app.get("/greet/<name>/<language>")
async def greet_in_language(request, name: str, language: str):
    greetings = {
        "english": "Hello",
        "spanish": "Hola",
        "french": "Bonjour",
        "german": "Hallo",
        "japanese": "Konnichiwa",
        "swahili": "Habari",
    }
    # .get() returns "Hello" if the language isn't in our dict
    greeting = greetings.get(language.lower(), "Hello")
    return json({"message": f"{greeting}, {name}!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
