from aiogram.types import User as UserType

from database.db import Session
from database.models import User


class UserService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def create_or_update_user(self, user: UserType):
        current_user = self.session.get(User, user.id)

        if not current_user:
            current_user = User(id=user.id,
                            full_name=user.full_name,
                            nickname=user.username if user.username else None)
            self.session.add(current_user)
            self.session.commit()

        if current_user.nickname != user.username:
            current_user.nickname = user.username

        if current_user.full_name != user.full_name:
            current_user.full_name = user.full_name

        self.session.commit()


user_service = UserService()