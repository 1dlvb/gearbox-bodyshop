from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    """Home page model"""

    # settings section
    template = 'home/home.html'
    max_count = 1

    # banner_title = models.CharField(max_length=200, blank=False, null=True)
    # banner_subtitle = RichTextField(features=['bold', 'italic'])
    working_time = models.CharField(max_length=50, blank=False, null=False)

    certificate1_title = models.CharField(max_length=50, blank=False, null=True)
    certificate1_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    certificate2_title = models.CharField(max_length=50, blank=False, null=True)
    certificate2_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel('working_time'),

        FieldPanel("certificate1_title"),
        ImageChooserPanel("certificate1_image"),

        FieldPanel("certificate2_title"),
        ImageChooserPanel("certificate2_image"),
    ]

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'
