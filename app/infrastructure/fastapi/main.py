from typing import Optional

import uvicorn
from fastapi import FastAPI

from app.controller.user import signup
from app.infrastructure.database.orm import db, UserModel


def init_db():
    db.connect()
    UserModel.create_table()


def create_app():
    init_db()
    app = FastAPI()
    app.add_api_route(
        path="/user",
        methods=["POST"],
        endpoint=signup
    )
    return app


if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)

