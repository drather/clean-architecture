from peewee import *
import datetime

# DB 의 경로를 동적ㅈ으로 처리해줄 수 있음.
db = SqliteDatabase(None, thread_safe=True)


class BaseModel(Model):
    class Meta:
        database = db


class UserModel(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = "users"


class ProductModel(BaseModel):
    name = CharField(null=False)
    price = IntegerField(null=False)

    class Meta:
        table_name = "products"
