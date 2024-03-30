from rest_framework import permissions

#kiểm tra đã chứng thực user chưa, và phải lấy ra đươợc comment , kiểu ai là người comment
class OwnerAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and request.user == obj.user