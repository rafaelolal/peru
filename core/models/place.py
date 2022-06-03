
from django.urls import reverse
from django.db.models import Model, CASCADE
from django.db.models.fields import CharField, TextField, IntegerField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

class Place(Model):
    name = CharField(max_length=64)
    description = TextField(max_length=8192)
    image = ImageField(upload_to='place_pics')
    likes = IntegerField(default=0)

    page = ForeignKey('Page', on_delete=CASCADE, related_name="places")

    def get_absolute_url(self):
        return reverse("core:exploración") + f"?period={self.page.period}&category={self.page.category}"