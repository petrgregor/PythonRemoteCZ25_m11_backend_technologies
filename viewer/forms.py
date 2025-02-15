import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, DateField, ModelChoiceField, Textarea, \
    ModelForm, NumberInput

from hollymovies.settings import DEBUG
from viewer.models import Country, Creator


"""
class CreatorForm(Form):
    name = CharField(max_length=32, required=False)
    surname = CharField(max_length=32, required=False)
    alias = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    country = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)
"""


class CreatorModelForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        #fields = ['name', 'alias', 'surname']
        #exclude = ['biography']

        labels = {
            'name': 'Jméno',
            'surname': 'Příjmení',
            'alias': 'Umělecké jméno',
            'date_of_birth': 'Datum narození',
            'date_of_death': 'Datum úmrtí',
            'country': 'Země',
            'biography': 'Biografie'
        }
        help_texts = {
            'biography': 'Zde zadejte biografii tvůrce.'
        }
        error_messages = {
            #
        }

    date_of_birth = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label="Datum narození")
    date_of_death = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label="Datum úmrtí")

    def clean_name(self):
        initial = self.cleaned_data['name']
        #print(f"Initial = '{initial}'")
        result = initial
        if initial:
            result = initial.capitalize()
            #print(f"result = '{result}'")
        return result

    def clean_surname(self):
        initial = self.cleaned_data['surname']
        result = initial
        if initial:
            result = initial.capitalize()
        return result

    def clean_alias(self):
        initial = self.cleaned_data['alias']
        result = initial
        if initial:
            result = initial.capitalize()
        return result

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        if DEBUG:
            print(f"initial date of birth: '{initial}'")
        if initial and initial > date.today():
            raise ValidationError("Datum narození nesmí být v budoucnosti")
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        if DEBUG:
            print(f"initial date of death: '{initial}'")
        if initial and initial > date.today():
            raise ValidationError("Datum úmrtí nesmí být v budoucnosti")
        return initial

    def clean_biography(self):
        initial = self.cleaned_data['biography']
        if DEBUG:
            print(f"initial biography: '{initial}'")
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')  # TODO: Věta může končit i ?!
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        initial_name = cleaned_data['name']
        initial_surname = cleaned_data['surname']
        initial_alias = cleaned_data['alias']
        if DEBUG:
            print(f"initial_name = '{initial_name}', "
                  f"initial_surname = '{initial_surname}', "
                  f"initial_alias = '{initial_alias}'")
        if not initial_surname and not initial_alias:
            raise ValidationError("Je nutné zadat příjmení nebo umělecké jméno (nebo oboje).")

        initial_date_of_birth = cleaned_data['date_of_birth']
        initial_date_of_death = cleaned_data['date_of_death']
        if (initial_date_of_birth
                and initial_date_of_death
                and initial_date_of_death <= initial_date_of_birth):
            raise ValidationError("Datum úmrtí nesmí být dřív, než datum narození.")

        return cleaned_data
