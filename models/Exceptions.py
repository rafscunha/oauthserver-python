from fastapi.exceptions import HTTPException

class UserDoesNotExist(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail="user does not exist")

class InvalidCredentials(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="wrong password")

class TokenExpired(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="token expired")