from django.contrib.auth.mixins import UserPassesTestMixin , LoginRequiredMixin


class OnlyLoggedSuperUser(UserPassesTestMixin , LoginRequiredMixin):
    
    def test_func(self):
        return self.request.user.is_superuser