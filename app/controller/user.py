from app.application.services.user import create_user


def signup():
    user = create_user(user_name="grab")
    return user