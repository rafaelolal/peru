from django.urls import reverse
from django.db.models import Model
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class Page(Model):
    map = ImageField(upload_to='section_pics')

    periods = ['Incas', 'Colonial', 'Monarquía del Perú', 'Independencia', 'Presente']
    tuple_periods = [(c, c) for c in periods]
    period = CharField(max_length=64, choices=tuple_periods)
    
    categories = ['Historia', 'Costumbres', 'Lugares']
    tuple_categories = [(c, c) for c in categories]
    category = CharField(max_length=64, choices=tuple_categories)

    def get_absolute_url(self):
        return reverse(f"core:exploración") + f"?period={self.period}&category={self.category}"