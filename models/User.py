from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
import datetime
import hashlib
from models.Exceptions import UserDoesNotExist, InvalidCredentials

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=128)
    email = fields.CharField(max_length=128, index=True)
    username = fields.CharField(max_length=64, index=True)
    password = fields.CharField(max_length=255)
    scopes = fields.TextField(default="")
    flag_deleted = fields.BooleanField(default=False)
    data_create = fields.DateField(default=datetime.datetime.now().date())

    # class PydanticMeta:
    #     exclude = 

    @staticmethod
    async def verify_credential(username, password):
        try:
            self = await User.get(username=username, flag_deleted=0)
        except Exception as e:
            raise UserDoesNotExist
        password = hashlib.md5(password.encode()).hexdigest()
        if password == self.password:
            return self
        else:
            raise InvalidCredentials
    

User_Pydantic = pydantic_model_creator(User, name="UserOut", exclude=["password", "flag_deleted", "data_create", "name", "email"])
UserIn_Pydantic = pydantic_model_creator(User,name="UserIn", exclude=["data_create", "flag_deleted", "id"])
