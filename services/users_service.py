from aiogram.types import User as UserType

from database.db import Session
from database.models import User


class UserService:
    def __init__(self, session: Session = Session()):
        self.session = session

    def create_new_user(self, user: UserType) -> User:
        new_user = User(id=user.id,
                        full_name=user.full_name,
                        nickname=user.username if user.username else None)
        self.session.add(new_user)
        self.session.commit()

        return new_user

    def get_user(self, user_id: int) -> User:
        current_user = self.session.get(User, user_id)
        return current_user

    def update_user(self, user: UserType) -> User:
        user_to_update = self.get_user(user.id)
        user_to_update.nickname = user.username
        user_to_update.full_name = user.full_name
        self.session.commit()

        return user_to_update

    def create_or_update_current_user(self, user: UserType) -> None:
        current_user = self.get_user(user_id=user.id)

        if not current_user:
            current_user = self.create_new_user(user=user)

        if current_user.nickname != user.username or current_user.full_name != user.full_name:
            self.update_user(user=user)


user_service = UserService()