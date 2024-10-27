from core.models import CustomUsers


class UserRepository:
    def get_user_by_id(self, user_id: int):
        user = CustomUsers.objects.filter(user_id=user_id).first()

        return user
    
    def get_all_users(self):
        users = CustomUsers.objects.filter(is_active=True)

        return users

    def create_user(self, name: str, email: str, password: str):
        user = CustomUsers.objects.create(
            username=name,
            email=email
        )
        user.set_password(password)
        user.save()

        return user
