from django.forms import ModelForm, Select, CheckboxSelectMultiple
from django.forms import ClearableFileInput, ModelChoiceField
from problem import models


class TcUpload(ModelForm):
    class Meta:
        model = models.UploadTC
        fields = ["name", "testcases"]
        widgets = {
            "testcases" : ClearableFileInput(attrs={"multiple": True}),
        }

        name = ModelChoiceField(queryset = models.Problem.objects.all(), widget = CheckboxSelectMultiple)