from tortoise.models import Model
from tortoise import fields
from datetime import datetime, timedelta
from pydantic import BaseModel
import uuid
import os
import hashlib
from models import User


class Token(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="user")
    token = fields.CharField(max_length=512, index=True, unique=True)
    expires_in = fields.DatetimeField()
    datetime_create = fields.DatetimeField(default=datetime.now())
    flag_deleted = fields.BooleanField(default=False)

    @staticmethod
    async def create_token(user):
        await Token.filter(user=user).delete()
        access_token = hashlib.sha256(str(uuid.uuid1()).encode()).hexdigest()
        self = await Token.create(
                user=user, 
                token=access_token,
                expires_in=datetime.now()+timedelta(seconds=int(os.getenv("VALIDE_TOKEN")))
        )
        return self
    
class TokenRespose(BaseModel):
    user_id:int
    expires_in:str
    token:str
    scopes:str

    @staticmethod
    def factory_token_response(user:User, token:Token):
        return TokenRespose(
            token=token.token,
            expires_in=token.expires_in.strftime("%Y-%m-%d %H:%M:%S"),
            user_id=user.id,
            scopes=user.scopes
        )
