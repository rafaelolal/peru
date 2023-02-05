"""Views associated with Place objects"""

from django.forms import Form
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Page, Place
from core.mixins import IsSuperuserMixin

class PlaceCreateView(IsSuperuserMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['name', 'description', 'image']
    model = Place
    template_name = 'core/place/form.html'

    def form_valid(self, form: Form) -> HttpResponse:
        """Manually sets the page for a place
        Page comes from the request
        """

        page = Page.objects.get(pk=int(self.kwargs['page_pk']))        
        form.instance.page = page
        return super().form_valid(form)

class PlaceUpdateView(IsSuperuserMixin, UpdateView):
    login_url = 'core:user_login'
    fields = ['name', 'description', 'image']
    model = Place
    template_name = 'core/place/form.html'

class PlaceDeleteView(IsSuperuserMixin, DeleteView):
    login_url = 'core:user_login'
    model = Place
    template_name = 'core/place/confirm_delete.html'

    def get_success_url(self) -> HttpResponse:
        """Redirects the user back to the Page's detail view they deleted the place from"""

        page = self.get_object().page
        return reverse_lazy(f"core:exploración") + f"?period={page.period}&category={page.category}"