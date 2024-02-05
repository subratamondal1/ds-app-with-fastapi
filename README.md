<h1 align="center">Applications with FastAPI</h1>

<h2 align="left">➾ Project Outline</h2>

1. ✅ Initialize the repo with **`Poetry`**.
2. ✅ Automate command execution with **`Makefile`**.
3. ✅ Automate build, code format, code lint with **`Github Actions - Continuous Integration`**.
4. ❌ Containerize the project with **`Docker Containers`**.
5. ❌ Register the project with **`AWS ECR - Elastic Container Registry`**.
6. ❌ Initiate cloud build with **`AWS CodeBuild`**.

<h2 align="left">➾ Bare Minimum FastAPI App</h2>

> **`main.py`**

```python
import fastapi
import uvicorn                           # production server

api = fastapi.FastAPI()                  # fastapi app instantiation

@app.get(path="/api/calculate")          # path operation
def calculate():                         # path operation function
    return {
        "value": 2 * 2
    }

if __name__=="__main__":
    uvicorn.run(app="main:api", host="127.0.0.1", port=8000, reload=True)
    # http://127.0.0.1:8000/api/calculate

# `main` is the file name where the FastAPI() is instantiated
# `api` is the variable to which the FastAPI() is instantiated
```

<h2 align="left">➾ <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods" target="__blank">Know your HTTP request verbs</a></h2>

| Verb         | Meaning                                                                                                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`GET`**    | The GET method requests a representation of the specified resource. It is used to `retrieve data without modifying it`.                                                              |
| **`POST`**   | The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server. It is used to `create new resources` or perform actions. |
| **`DELETE`** | The DELETE method `deletes the specified resource`. It is used to remove resources from the server.                                                                                  |
| **`PUT`**    | The PUT method `replaces all current representations` of the target resource with the request payload. It is used to update existing resources or create new ones.                   |

<hr>

HTTP verbs are what the client is instructing (**`requesting`**) the server to do, but the server has no ability to directly talk back to the client that "yes, it's done", instead the server talks back with HTTP response. HTTP response has three main parts: **`status code, response headers and response body`**.

<hr>

<h2 align="left">➾ <a href="https://httpstatuses.io/" target="__blank">Know your HTTP response status code</a></h2>

| Status Code | Meaning                                                                                                                                                        |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`1xx`**   | **`Informational responses`**. They indicate that the request was received and is being processed.                                                             |
| **`2xx`**   | **`Successful responses`**. They indicate that the request was successfully completed.                                                                         |
| **`3xx`**   | **`Redirection responses`**. They indicate that the client needs to perform additional actions to complete the request, such as following a different URL.     |
| **`4xx`**   | **`Client error responses`**. They indicate that the request contains bad syntax or cannot be fulfilled by the server, due to some error on the client's side. |
| **`5xx`**   | **`Server error responses`**. They indicate that the request could not be completed by the server, due to some error on the server's side.                     |

<h2 align="left">➾ Passing data to the api</h2>

In your example, you have defined a GET endpoint at `/api/calculate` that takes three parameters: `a`, `b`, and `c`. The parameters `a` and `b` are required, while `c` is optional and has a default value of 10. The endpoint returns the value of `(a + b) * c` as a JSON object.

<h3 align="left">➾ <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="__blank">Path Parameters</a></h3>

```python
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get(path="/api/calculate/{a}/{b}/{c=10}")
def calculate(a: int, b: int, c: int = 10):
    return {"value": (a + b) * c}

# url: http://127.0.0.1:8000/api/calculate/2/3/{c=10}?c=10
```

These (`a`, `b`, and `c`) are the variables that are part of the path of the endpoint. They are enclosed in curly braces and can be used to capture dynamic values from the URL. For example, `@api.get(path="/api/calculate/{a}/{b}/{c=10}")` means that the function expects an `a, b and c` as path parameter, where `c` is the default whereas, others are required.

<h3 align="left">➾ <a href="https://fastapi.tiangolo.com/tutorial/query-params/" target="__blank">Query Parameters</a></h3>

```python
import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get(path="/api/calculate")
def calculate(a: int, b: int, c: int = 10):
    return {"value": (a + b) * c}

# url: http://127.0.0.1:8000/api/calculate?a=2&b=3&c=10
```

These (`a`, `b`, and `c`) are the key-value pairs that are appended to the URL after a question mark (`?`). They can be used to pass optional or extra information to the endpoint. For example, `@api.get(path="/api/calculate")` api endpoint can accept a query parameter like `?a=2&b=3&c=10`, where `a,b` are required parameters whereas, `c` is optional parameter.

<h3 align="left">➾ <a href="https://fastapi.tiangolo.com/tutorial/body/" target="__blank">Request Body</a></h3>

```python
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

# url: http://127.0.0.1:8000/api/calculate
```

This is the data that is sent by the client to the endpoint in the HTTP request. It is usually in JSON format and can be used to pass complex or large data to the endpoint. For example, `@api.post(path="/api/calculate")` can accept a request body like `{"a": 2, "b": 3, "c": 10}`.

<h2 align="left">Responding to Requests</h2>

<h3 align="left">Responding to Requests in Basic Way</h3>

```python
import fastapi
import uvicorn
import typing

api = fastapi.FastAPI()


@api.get(path="/api/calculate")
def calculate(a: int, b: int, c: typing.Optional[int] = None):
    result = a + b
    if c == 0:
        return fastapi.Response(
            content="ERROR: 'c' cannot be Zero.",
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            media_type="application/json"
    )   # update
    if c is not None:
        result *= c
    return {"a": a, "b": b, "c": c, "value": result}

# url: http://127.0.0.1:8000/api/calculate?a=2&b=3&c=0
```

<h3 align="left">Responding to Requests in Specialized Way</h3>

```python
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
    )   # update
    if c is not None:
        result *= c
    return {"a": a, "b": b, "c": c, "value": result}

# url: http://127.0.0.1:8000/api/calculate?a=2&b=3&c=0
```
