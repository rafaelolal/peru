from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class IsSuperuserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is a superuser
    Will redirect the user to a view's login_url attribute if they are not logged in
    """

    def test_func(self) -> bool:
        return self.request.user.is_superuser

class IsTheUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Checks if a user is logged in and is associated with the view
    Will redirect the user to a view's login_url attribute if they are not logged in
    """
    
    def test_func(self) -> bool:
        return self.request.user.pk == int(self.kwargs['pk'])