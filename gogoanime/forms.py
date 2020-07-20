from django.forms import ModelForm

from gogoanime.models import Link

class SubmitURLForm(ModelForm):
	class Meta:
		model = Link
		fields = '__all__'
		initial = {'site': 'gogoanime', 'host': 'mp4upload'}