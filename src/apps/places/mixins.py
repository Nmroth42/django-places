from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied


class AuthRequiredMixin(object):
    """require that a user is authenticated.

    If the user is not authenticated send them to the login page.
    """
    login_url = settings.LANDING_URL

    def dispatch(self, request, *args, **kwargs):
        """check if the user is authenticated.

        If they are authenticated return the normal dispatch. If not,
        redirect them to login page.
        """
        if not request.user.is_authenticated:
            return redirect_to_login(request.get_full_path(), self.login_url)

        return super(AuthRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class UserAuthorMixinListView(AuthRequiredMixin):
    """Checks that the user is the author of the listView queryset.

    If they are not, return a 403 error
    """

    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated and request.user.id is not self.get_queryset().first().owner.id:
                raise PermissionDenied
        except AttributeError:
            pass

        return super(UserAuthorMixinListView, self).dispatch(
            request, *args, **kwargs)
