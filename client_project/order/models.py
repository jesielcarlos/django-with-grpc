from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    items = models.JSONField()

    def __str__(self):
        return f"Order {self.id} for user {self.user_id}"
