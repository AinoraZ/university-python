from django.forms import ModelForm
from forms.models import MaterialAct, Materials


class MaterialActForm(ModelForm):
    class Meta:
        model = MaterialAct
        fields = ("institution_title", "seller", "invoice_series", "commissioners",
                  "sellers_code", "date_bought", "location", "responsible_worker")


class MaterialsForm(ModelForm):
    class Meta:
        model = Materials
        fields = ("name", "amount_type", "amount", "sum", "reason")
