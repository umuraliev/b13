from django.forms import CharField, EmailField, ModelForm, Textarea, ValidationError, Form
from .models import Product, Comment


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'slug')

    def clean(self):
        slug = self.cleaned_data.get('name').lower().replace(" ", '-')
        if Product.objects.filter(slug=slug).exists():
            raise ValidationError('Product with such name already exists!')
        return self.cleaned_data

class EmailPostForm(Form):
    name = CharField(max_length=25)
    email = EmailField()
    to = EmailField()
    comments = CharField(required=False,
                               widget=Textarea)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('created', 'updated', 'active', 'product', )
