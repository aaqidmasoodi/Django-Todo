from django import forms
from todos.models import Todo

# REST FORM --->> SERIALZER 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            "title",
            "description"
        ]


    # check if title contain patrick
    def clean_title(self):
        title = self.cleaned_data['title']

        if "patrick" not in title:
            raise forms.ValidationError("Oops! it does not contain patrick")


        return title


