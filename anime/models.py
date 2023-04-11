from django.db import models

# Create your models here.

from wagtail.api import APIField

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class AnimePage(Page):
    # page_description = "New anime listing"
    anime_banner_img = models.ImageField()
    anime_title = models.CharField(max_length=300, blank=False)
    anime_description = RichTextField(blank=True)
    # tags = models.Choices([("COMEDY",
    #                        "DRAMA",
    #                         "SHONEN",
    #                         "ACTION",
    #                         "ADVENTURE",
    #                         "SUPERNATURAL",)])

    content_panels = Page.content_panels + [
        FieldPanel('anime_banner_img'),
        FieldPanel('anime_title'),
        FieldPanel('anime_description'),
        # FieldPanel('tags', classname="full"),
    ]

    api_fields = [
        APIField("anime_banner_img"),
        APIField("anime_title"),
        APIField("anime_description"),
    ]
