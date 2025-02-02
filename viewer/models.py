from django.db.models import Model, CharField, ManyToManyField, IntegerField, \
    TextField, DateField, DateTimeField


class Genre(Model):
    #__tablename__ = "genre"
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    countries = ManyToManyField("Country", blank=True, related_name='movies')
    length = IntegerField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    released_date = DateField(null=True, blank=True)
    released_year = IntegerField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title_orig']

    def __repr__(self):
        return f"Movie({self.title_orig})"

    def __str__(self):
        return f"{self.title_orig} ({self.released_year})"


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    def __repr__(self):
        return f"Country(name={self.name})"

    def __str__(self):
        return f"{self.name}"
