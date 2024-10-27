from core.models import CustonUsers


class UserRepository:
    def get_user_by_id(self, user_id: int):
        user = CustonUsers.objects.filter(user_id=user_id).first()

        return user
    
    def get_all_users(self):
        users = CustonUsers.objects.filter(is_active=True)

        return users

    def create_user(self, name: str, email: str, password: str):
        user = CustonUsers.objects.create(
            username=name,
            email=email
        )
        user.set_password(password)
        user.save()

        return user
