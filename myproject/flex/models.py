""" Flexible page """
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel


class FlexPage(Page):

    template = 'flex/flex_page.html'

    subtitle = models.CharField(max_length=150, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]

    class Meta:
        verbose_name = 'Flex Page'
        verbose_name_plural = 'Flex Pages'