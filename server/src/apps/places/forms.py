
from django import forms
from .models import Memory

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'comment']

    def save(self, request):
        new_memory = Memory.objects.create(
            name = self.cleaned_data['name'],
            comment = self.cleaned_data['comment'],
            latitude = request.POST['lat'],
            longitude = request.POST['lng'],
            owner = request.user
            )
        return new_memory
