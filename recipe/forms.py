from django import forms
from django.forms.formsets import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RecipeForm(forms.Form):
    recipe_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'name_field'}),
        label="Recipe Name",
        max_length=100,
        required=True,
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class':'description_field'}),
        label="Description",
        required=True,
    )

    directions = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'direction_field'}),
        label="Recipe Directions",
        required=True,
    )

    image = forms.ImageField(
        label="Image",
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-recipe_form'
        self.helper.form_tag = False
        self.helper.form_class = 'recipe_form'


class IngredientForm(forms.Form):
    name = forms.CharField(
        label="Name",
        required=False,
    )

    quantity = forms.CharField(
        label="Quantity",
        required=False,
    )

    state = forms.CharField(
        label="State (chopped, minced, etc.)",
        required=False,
    )


class IngredientFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(IngredientFormSetHelper, self).__init__(*args, **kwargs)
        self.form_class = "ingredient_form"
        self.render_required_fields = True
        self.form_tag = False
        self.template = 'bootstrap/table_inline_formset.html'


