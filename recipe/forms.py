from django import forms
from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RecipeForm(forms.Form):
    recipe_name = forms.CharField(
        label="Name",
        max_length=100,
        required=True,
    )

    description = forms.CharField(
        label="Description",
        required=True,
    )

    directions = forms.CharField(
        label="Directions",
        required=True,
    )

    image = forms.ImageField(
        label="Image",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-recipeForm'
        self.helper.form_class = 'recipeForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_recipe'

        self.helper.add_input(Submit('submit', 'Submit'))


class IngredientForm(forms.Form):
    name = forms.CharField(
        label="Name",
        required=True,
    )

    quantity = forms.IntegerField(
        label="Quantity",
        required=True,
    )

    state = forms.CharField(
        label="State (chopped, minced, etc.)",
        required=True,
    )

