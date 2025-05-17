from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    body = RichTextField(blank=True)
    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + ["body"]
    