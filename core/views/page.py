from typing import Any, Dict, List
from django.db.models.query import QuerySet

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from core.mixins import IsSuperuserMixin
from core.models import Page

class PageListView(ListView):
    model = Page
    template_name = 'core/page/list.html'

    def get(self, request: HttpResponse,
        *args: (Any),
        **kwargs: Dict[str, Any]) -> HttpResponse:
        
        """Gets the link to the appropriate view
        Redirects user to the PageListView or if there is
        only one Page object in the QuerySet object,
        redirects to that Page's DetailView
        Saves the user time
        """
        
        queryset = self.get_queryset()
        if queryset and len(queryset) == 1:
            messages.warning(request,
                'This is the only page that matches your search.')
            
            page = queryset.first()
            return HttpResponseRedirect(reverse('core:exploración') + f"?period={page.period}&category={page.category}")

        return super().get(request, *args, **kwargs)

    def get_queryset(self) -> QuerySet:
        """Gets all the Thing objects to be displayed
        Returns only the Thing objects that fit
        the filters in the request's querystring
        """

        search_querysets = []
        if 'search' in self.request.GET:
            query = self.request.GET['search']
            for page in self.model.objects.all():
                for section in page.sections.all():
                    if query in section.content or query in section.title:
                        search_querysets.append(self.model.objects.all().filter(pk=page.pk))
                        break

        if len(search_querysets) == 0:
            return self.model.objects.all();

        queryset = self.combine(search_querysets)
        return queryset

    @staticmethod
    def combine(queryset: List) -> QuerySet:
        """Used to combine QuerySet objects in a list of QuerySet objects"""

        final_queryset = queryset[0]
        for query in queryset[1:]:
            final_queryset |= query

        return final_queryset

class PageDeleteView(IsSuperuserMixin, DeleteView):
    login_url = 'core:user_login'
    model = Page
    success_url = reverse_lazy("core:page_list")
    template_name = 'core/page/confirm_delete.html'

class PageUpdateView(IsSuperuserMixin, UpdateView):
    login_url = 'core:user_login'
    fields = ['map', 'period', 'category']
    model = Page
    template_name = 'core/page/form.html'

class PageCreateView(IsSuperuserMixin, CreateView):
    login_url = 'core:user_login'
    fields = ['map', 'period', 'category']
    model = Page
    template_name = 'core/page/create.html'