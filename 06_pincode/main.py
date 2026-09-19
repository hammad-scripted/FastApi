from fastapi import FastAPI

from exceptions import (
    pincode_not_found_handler,
    invalid_pincode_handler,
    PinCodeNotFoundError,
    InvalidPinCodeError
)

from models import BulkRequest, BulkResponse, LocationResponse
from data import pincode_db


app = FastAPI(
    title="Pincode API",
    description="Auto fill city and state from Indian pincode during checkout",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)


# Register custom exception handlers
app.add_exception_handler(
    PinCodeNotFoundError,
    pincode_not_found_handler
)

app.add_exception_handler(
    InvalidPinCodeError,
    invalid_pincode_handler
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Pincode API"
    }


@app.get("/pincode/{code}", response_model=LocationResponse)
def lookup(code: str):

    # Validate format first
    if len(code) != 6 or not code.isdigit():
        raise InvalidPinCodeError(
            pincode=code,
            reason="Pincode must be exactly 6 digits"
        )

    # Check database
    if code not in pincode_db:
        raise PinCodeNotFoundError(
            pincode=code
        )

    return LocationResponse(
        pincode=code,
        city=pincode_db[code]["city"],
        state=pincode_db[code]["state"],
        district=pincode_db[code]["district"]
    )


@app.post("/pincode/bulk", response_model=BulkResponse)
def bulk_lookup(request: BulkRequest):

    results = []
    missing = []

    for code in request.pincodes:

        if code not in pincode_db:
            missing.append(code)
        else:
            results.append(pincode_db[code])

    return BulkResponse(
        status="success",
        found=len(results),
        not_found=len(missing),
        locations=results,
        missing=missing
    )