from core.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_user(self, user_id: int):
        return self.repository.get_user_by_id(user_id)

    def create_user(self, name: str, email: str):
        return self.repository.create_user(name, email)
