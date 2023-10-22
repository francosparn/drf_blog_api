from rest_framework.permissions import BasePermission

from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        # If the request is of type GET or POST, the user can continue
        if request.method == 'GET' or request.method == 'POST':
            return True
        # In case the user wants to edit or delete the comment, we validate that the user who wants to do this action is the owner of said comment.
        else:
            # Get the id of the comment the user is trying to edit or delete
            id_comment = view.kwargs['pk']
            # Request to the database to obtain the data of that comment
            comment = Comment.objects.get(pk=id_comment)
            
            # Obtain the id of the user who wants to make a PUT or DELETE request
            id_user = request.user.pk
            
            # Get the id of the user who created the comment
            id_user_comment = comment.user_id
            
            # Validate that the user who is making the request matches the ID of the user who created the comment
            if id_user == id_user_comment:
                return True
            
            return False