"""Views associated with Section objects"""

from django.forms import Form
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from core.models import Page, Section
from core.mixins import IsSuperuserMixin

class SectionCreateView(IsSuperuserMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['title', 'content', 'image', 'order']
    model = Section
    template_name = 'core/section/form.html'

    def form_valid(self, form: Form) -> HttpResponse:
        """Manually sets the page for a section
        Page comes from the request
        """

        page = Page.objects.get(pk=int(self.kwargs['page_pk']))        
        form.instance.page = page
        return super().form_valid(form)

class SectionUpdateView(IsSuperuserMixin, UpdateView):
    login_url = 'core:user_login'
    fields = ['title', 'content', 'image', 'order']
    model = Section
    template_name = 'core/section/form.html'

class SectionDeleteView(IsSuperuserMixin, DeleteView):
    login_url = 'core:user_login'
    model = Section
    template_name = 'core/section/confirm_delete.html'

    def get_success_url(self) -> HttpResponse:
        """Redirects the user back to the Page's detail view they deleted the section from"""

        page = self.get_object().page
        return reverse_lazy(f"core:exploración") + f"?period={page.period}&category={page.category}"