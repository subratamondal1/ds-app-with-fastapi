import fastapi
import uvicorn
import pydantic

api = fastapi.FastAPI()

class Numbers(pydantic.BaseModel):
    a: int
    b: int
    c: int = 10


@api.post(path="/api/calculate")
def calculate(numbers:Numbers):
    return {"value": (numbers.a + numbers.b) * numbers.c}


if __name__ == "__main__":
    uvicorn.run(app="main:api", host="127.0.0.1", port=8000, reload=True)
