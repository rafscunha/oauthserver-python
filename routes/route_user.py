from fastapi import APIRouter, Body, HTTPException
from models.User import User, UserIn_Pydantic, User_Pydantic
from docs.user import post_create_user
import hashlib
import logging

router = APIRouter()
logger = logging.getLogger("user")

@router.post("/user", status_code=201, response_model=User_Pydantic, responses=post_create_user.EXEMPLE_RESPONSE)
async def create_user(user : UserIn_Pydantic = Body(example=post_create_user.EXEMPLE_REQUEST)):
    user.password = hashlib.md5(user.password.encode()).hexdigest()
    try:
        user_created = await User.create(**user.dict(exclude_unset=True))
    except Exception as e:
        logger.warn(e)
        raise HTTPException(status_code=422)
    return user_created

@router.put("/user")
async def update_user():
    pass

@router.delete("/user")
async def delete_user():
    pass

# @router.path("/user")
# async def give_scope_to_user():
#     pass