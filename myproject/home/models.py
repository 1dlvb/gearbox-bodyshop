from .forms import ContactForm
from django.db import models
from django.shortcuts import render

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
    thankyou_page_title = models.CharField(max_length=150, blank=False, null=True)

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
        FieldPanel('thankyou_page_title'),

        FieldPanel("certificate1_title"),
        ImageChooserPanel("certificate1_image"),

        FieldPanel("certificate2_title"),
        ImageChooserPanel("certificate2_image"),
    ]

    def serve(self, request):

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                flavour = form.save()
                context = {
                    'page': self,

                }
                return render(request, 'home/we_got_your_message.html', context)
        else:
            form = ContactForm()
        context = {
            'page': self,
            'form': form,
        }
        return render(request, 'home/home.html', context=context)

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'



