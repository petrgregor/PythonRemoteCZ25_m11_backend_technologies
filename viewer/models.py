from datetime import datetime, date

from django.db.models import Model, CharField, ManyToManyField, IntegerField, \
    TextField, DateField, DateTimeField, ForeignKey, SET_NULL


class Genre(Model):
    #__tablename__ = "genre"
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Genre(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    alias = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country = ForeignKey("Country", null=True, blank=True, on_delete=SET_NULL, related_name='creators')
    biography = TextField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['surname', 'name']

    def __repr__(self):
        return f"Creator(name={self.name}, surname={self.surname})"

    def __str__(self):
        return f"{self.name} {self.surname} ({self.date_of_birth.year})"

    def age(self):
        if self.date_of_birth:
            end_date = self.date_of_death or date.today()
            return end_date.year - self.date_of_birth.year - ((end_date.month, end_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    countries = ManyToManyField("Country", blank=True, related_name='movies')
    directors = ManyToManyField(Creator, blank=True, related_name="directing")
    actors = ManyToManyField(Creator, blank=True, related_name="acting")
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

    def released_date_cz(self):
        if self.released_date:
            return datetime.strftime(self.released_date, "%d. %m. %Y")
        return None

    def length_format(self):
        # převést délku filmu z minut na formít h:mm
        # 142 -> 2:22
        # 122 -> 2:02
        if self.length:
            hours = self.length // 60
            minutes = self.length % 60
            if minutes < 10:
                minutes = f"0{minutes}"
            return f"{hours}:{minutes}"
        return None


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    def __repr__(self):
        return f"Country(name={self.name})"

    def __str__(self):
        return f"{self.name}"
