from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    A form that automatically creates fields
    based on the Product model
    """

    class Meta:
        model = Product              # Use the Product model
        fields = '__all__'            # Include all model fields

    def __init__(self, *args, **kwargs):
        # First, let Django build the default form
        super().__init__(*args, **kwargs)

        # Get all categories from the database
        categories = Category.objects.all()

        # Create a list of (id, friendly_name) tuples
        # This is the format Django expects for dropdown choices
        # c = individual category
        friendly_names = [
            (c.id, c.get_friendly_name())
            for c in categories
        ]

        # Replace the default category dropdown choices
        # with our friendly names
        self.fields['category'].choices = friendly_names

        # Add the same CSS classes to every form field
        # so styling is consistent
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
