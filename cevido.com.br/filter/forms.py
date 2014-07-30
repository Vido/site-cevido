from django import forms

from filter.models import FilterKind

KINDS = [(fk.pk, fk.title) for fk in FilterKind.objects.all()]

class KindForm(forms.Form):
    which_kind = forms.ChoiceField(
            widget=forms.Select,
            choices=KINDS,
            label="::"
        )

