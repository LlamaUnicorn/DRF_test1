from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTokenAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to only allow authenticated users
    with a valid token to edit and delete objects.
    """

    def has_permission(self, request, view):
        """Allow read-only access to public endpoints."""
        if request.method in SAFE_METHODS:
            return True

        # "Check if the user has a valid token"
        return request.auth is not None
