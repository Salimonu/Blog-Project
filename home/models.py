from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page



class HomePage(Page):
    image = models.ForeignKey("wagtailimages.Image",
                              null=True, blank=True, on_delete=models.SET_NULL,
                              related_name="+", help_text="Homepage Image",
                              )
    hero_text = models.CharField(
        blank=True, max_length=255, help_text="Write an introduction for the site."
    )
    hero_cta = models.CharField(
        blank=True, verbose_name="Hero CTA", max_length=255,
        help_text="Text to display on call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page", 
        null=True, blank=True, on_delete=models.SET_NULL,
        related_name="+", verbose_name="Hero CTA Link",
        help_text="Choose a page to link to for the Call to Action.",
    )

    body = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ], heading = "Hero section",
        ),
        FieldPanel("body"),
    ]
    