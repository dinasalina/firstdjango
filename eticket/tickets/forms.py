from django import forms
from lookups.models import Category, Department

class CreateTicketForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True,
        label="Title",
        min_length=5
    )
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Explain the issue in detail..."}),
        required=True,
        label="Description",
        min_length=10,
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Category",
        empty_label="Select Category",
        required=True,
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        label="Department",
        empty_label="Select Department",
        required=True,
    )
