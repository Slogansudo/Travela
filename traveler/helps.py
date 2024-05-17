import uuid
from django.db import models


class EmployeStatus(models.TextChoices):
    translator = "Translator", "Translator"
    manager = "Manager", "Manager"
    pilot = "Pilot", "Pilot"
    accountant = "Accountant", "Accountant"
    pioneer = "Pioneer", "Pioneer"
    other = "Other", "Other"


class PriceType(models.TextChoices):
    usa = '$', "$"
    rus = "rubl", 'rubl'
    uzb = 'sum', 'sum'


class SaveMediafile(object):
    def save_employe_image(instance, filename):
        image_ext = filename.split('.')[-1]
        return f'employes/{uuid.uuid4()}.{image_ext}'

    def save_gallery_media(instance, filename):
        image_ext = filename.split('.')[-1]
        return f'galleries/{uuid.uuid4()}.{image_ext}'

    def save_travel_media(instance, filename):
        image_ext = filename.split('.')[-1]
        return f'travel/{uuid.uuid4()}.{image_ext}'

    def save_about_us_media(instance, filename):
        image_ext = filename.split('.')[-1]
        return f'about/{uuid.uuid4()}.{image_ext}'

    def save_city_media(instance, filename):
        image_ext = filename.split('.')[-1]
        return f'city/{uuid.uuid4()}.{image_ext}'

    def save_tour_category_media(instance, filename):
        image_ext = filename.split('.')[-1]
        return f'tour/{uuid.uuid4()}.{image_ext}'

