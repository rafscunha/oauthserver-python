from fastapi import APIRouter, Header, Request
import base64
from models.Token import Token, TokenRespose
from models.User import User
from datetime import datetime
from models.Exceptions import TokenExpired

router = APIRouter()

@router.post("/auth", response_model=TokenRespose)
async def create_token(request:Request):
    token_basic_authorization = request.headers["Authorization"].split(" ")[1]
    credentials = base64.b64decode(token_basic_authorization).decode('utf-8').split(":")
    user = await User.verify_credential(credentials[0], credentials[1])
    token = await Token.create_token(user)
    return TokenRespose.factory_token_response(user,token)

@router.get("/auth")
async def validate_token(request:Request):
    bearer_token = request.headers["Authorization"].split(" ")[1]
    token = await Token.get(token=bearer_token).select_related("user")
    if token.expires_in.strftime("%Y-%m-%d %H:%M:%S") >= datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
        return TokenRespose.factory_token_response(token.user,token)
    else:
        raise TokenExpired