from fastapi import FastAPI, Request,Response

app = FastAPI(
    title="My First API",
    description="This is my first API",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
async def root( response: Response):
    response.status_code = 200
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["X-Developer"] = "Hammad"
    response.set_cookie(key="my_cookie", value="cookie_value")
    return {"message": "Hello World"}


@app.get("/about")
async def about(response: Response):
     response.status_code = 200
     response.headers["Content-Type"] = "application/json"
     response.headers["Access-Control-Allow-Origin"] = "*"
     response.headers["X-Developer"] = "Hammad"
     response.set_cookie(key="my_cookie", value="cookie_value")
     return {"message": "About", "version": "1.0.0", "author": "John Doe"}


@app.get("/request")
async def request_info(request: Request):
    return {
        # Basic request information
        "method": request.method,
        "url": str(request.url),
        "base_url": str(request.base_url),
        "path": request.url.path,
        "query_string": request.url.query,
        # Headers
        "headers": dict(request.headers),
        # Client information
        "client": {
            "host": request.client.host if request.client else None,
            "port": request.client.port if request.client else None,
        },
        # Request parameters
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
        # Cookies
        "cookies": dict(request.cookies),
        # Application information
        "app": str(request.app),
        # HTTP scheme
        "scheme": request.url.scheme,
        # HTTP version
        "http_version": request.scope.get("http_version"),
        # Server information
        "server": request.scope.get("server"),
        # Raw ASGI scope information
        "scope": {
            "type": request.scope.get("type"),
            "method": request.scope.get("method"),
            "path": request.scope.get("path"),
            "query_string": request.scope.get("query_string").decode(),
            "scheme": request.scope.get("scheme"),
        },
    }


@app.get(
    "/orders/active",
    summary="Get active orders",
    description="Returns a list of active orders or an empty list if there are no active orders.",
    tags=["Orders"],
    response_description="A list of active orders",
)
def get_active_orders():
    """Returns a list of active orders or an empty list if there are no active orders."""
    return [{"id": 1, "name": "Order 1"}, {"id": 2, "name": "Order 2"}]
