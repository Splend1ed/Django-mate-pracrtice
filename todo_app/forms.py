from django.forms import (
    CharField, CheckboxSelectMultiple,
    ModelForm,
    ModelMultipleChoiceField,
)

from todo_app.models import Tag, Task
from bootstrap_datepicker_plus.widgets import DateTimePickerInput


class CreateUpdateTaskForm(ModelForm):
    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "deadline": DateTimePickerInput()
        }
