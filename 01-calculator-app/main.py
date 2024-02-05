import fastapi
import uvicorn
import typing

api = fastapi.FastAPI()


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