from fastapi import HTTPException, status, JSONResponse, Request


class PinCodeNotFoundError(HTTPException):
    def __init__(self, pincode: str):
        self.pincode = pincode


class InvalidPinCodeError(HTTPException):
    def __init__(self, pincode: str, reason: str = "Invalid format"):
        self.pincode = pincode
        self.reason = reason


# Custom handler


async def pincode_not_found_handler(request: Request, exc: PinCodeNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "Pincode not found",
            "pincode": exc.pincode,
            "message": f"The provided {exc.pincode} pincode was not found.",
        },
    )


async def invalid_pincode_handler(request: Request, exc: InvalidPinCodeError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": "Invalid pincode",
            "pincode": exc.pincode,
            "message": f"The provided {exc.pincode} pincode is invalid. {exc.reason}",
        },
    )
