from rest_framework.permissions import BasePermission


# 오직 나만 수정 가능
class IsMe(BasePermission):
    def has_object_permission(self, request, view, question):
        return question.username == request.user
