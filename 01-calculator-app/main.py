import fastapi
import uvicorn
import typing

api = fastapi.FastAPI()

@api.get(path="/", response_class=fastapi.responses.HTMLResponse)
def homepage():
    body = """
    <html>
        <head>
            <style>
                h1 {
                    text-align: center;
                }
                a {
                    display: block;
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to superfast Calculator API</h1>
            <a href="http://127.0.0.1:8000/api/calculate?a=2&b=3&c=10">Try me</a>
        </body>
    </html>
    """
    return fastapi.responses.HTMLResponse(content=body)


@api.get(path="/api/calculate")
def calculate(a: int, b: int, c: typing.Optional[int] = None):
    result = a + b
    if c == 0:
        return fastapi.responses.JSONResponse(
            content={"error" : "'c' cannot be Zero."},
            status_code=fastapi.status.HTTP_400_BAD_REQUEST
    )
    if c is not None:
        result *= c
    return {"a": a, "b": b, "c": c, "value": result}


if __name__ == "__main__":
    uvicorn.run(app="main:api", host="127.0.0.1", port=8000, reload=True)