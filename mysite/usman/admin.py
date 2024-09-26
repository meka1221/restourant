from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Courier)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Rating)
admin.site.register(Review)


@admin.register(Food)
class FoodAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
