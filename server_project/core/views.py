from core.models import CustomUsers
from django.http import JsonResponse
from django.views import View
from core.services import UserService
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class UsersViewSet(View):
    queryset = CustomUsers.objects.all()
    service = UserService()

    def get(self, request, user_id):
        
        user = self.service.get_user_by_id(user_id)
        if user:
            return JsonResponse(
                {
                    "id": user.id,
                    "name": user.username,
                    "email": user.email
                })
        return JsonResponse({"error": "User not found"}, status=404)
    @method_decorator(csrf_exempt)
    def post(self, request):
        data = request.data
        user = self.service.create_user(
            data["name"],
            data["email"],
            data["password"]
        )
        return JsonResponse({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
