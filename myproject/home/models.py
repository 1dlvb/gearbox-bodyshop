from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """Home page model"""

    # settings section
    template = 'home/home.html'
    max_count = 1

    banner_title = models.CharField(max_length=200, blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title')
    ]

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'
