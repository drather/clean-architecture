from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.controller.product import find_product, find_product_all
from app.controller.user import signup
from app.infrastructure.database.orm import db, UserModel, ProductModel


def init_db():
    db.init(database="database.db")
    db.connect()
    UserModel.create_table()
    ProductModel.create_table()


def create_app(initialize_db=False):
    app = FastAPI()

    app.add_api_route(path="/user", methods=["POST"], endpoint=signup)
    app.add_api_route(path="/products", methods=["POST"], endpoint=find_product)
    app.add_api_route(path="/products", methods=["GET"], endpoint=find_product_all)

    if initialize_db:
        init_db()

    return app


app = create_app(initialize_db=True)


if __name__ == '__main__':
    uvicorn.run("app.infrastructure.fastapi.main:app", host="0.0.0.0", port=8000, reload=True)

