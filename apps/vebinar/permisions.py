from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.method in ("POST", "DELETE", "GET")
            and request.user.is_authenticated
        ):
            data_user_id = view.kwargs.get(view.lookup_field) or request.data.get('user')
            if data_user_id is not None:
                return request.user.id == data_user_id
        return False
