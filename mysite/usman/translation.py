from .models import Food
from modeltranslation.translator import TranslationOptions, register


@register(Food)
class FoodTranlationOptions(TranslationOptions):
    fields = ['resto_name', 'description']
