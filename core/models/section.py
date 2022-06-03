
from django.urls import reverse
from django.db.models import Model, CASCADE
from django.db.models.fields import CharField, TextField, IntegerField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

class Section(Model):
    title = CharField(max_length=64)
    content = TextField(max_length=8192)
    image = ImageField(upload_to='section_pics')
    order = IntegerField(unique=True)

    page = ForeignKey('Page', on_delete=CASCADE, related_name="sections")

    def get_absolute_url(self):
        return reverse("core:exploración") + f"?period={self.page.period}&category={self.page.category}"