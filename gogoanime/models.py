from django.db import models

# Create your models here.
class Site(models.Model):
	"""Model representing the site being linked to (e.g. gogoanime)"""

	SITE_CHOICES = (
		('gogoanime', 'gogoanime'),
	)

	name = models.CharField(max_length=30, choices=SITE_CHOICES, default='gogoanime')

	def __str__(self):
		return self.name

class Host(models.Model):
	"""Model representing the video hosting site used (e.g. mp4upload)"""
	
	HOST_CHOICES = (
		('mp4upload', 'mp4upload'),
	)

	name = models.CharField(max_length=30, choices=HOST_CHOICES, default='mp4upload')

	def __str__(self):
		return self.name

class Link(models.Model):
	"""Model representing a URL of a submitted video"""

	video_url = models.URLField('Video URL', max_length=300, help_text='Enter video URL')
	site = models.ForeignKey('Site', on_delete=models.SET_NULL, null=True)
	host = models.ForeignKey('Host', on_delete=models.SET_NULL, null=True)
	time_requested = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.video_url

	def get_absolute_url(self):
		return reverse('link-detail', args=[str(self.id)])