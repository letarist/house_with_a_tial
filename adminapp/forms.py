from django.forms import ModelForm
from mainapp.models import Animal, TypeOfAnimal


class EditAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class CreateAnimal(ModelForm):
    class Meta:
        model = Animal
        fields = ('type', 'name', 'age', 'avatar', 'short_description', 'description')


class CreateType(ModelForm):
    class Meta:
        model = TypeOfAnimal
        fields = '__all__'


