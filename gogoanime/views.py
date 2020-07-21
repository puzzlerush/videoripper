import urllib

from django.shortcuts import render
from gogoanime.models import Site, Host, Link
from django.http import HttpResponseRedirect
from django.urls import reverse

from gogoanime.forms import SubmitURLForm
from crawler.gogodl import GogoanimeDownloader
# Create your views here.

def index(request):
	"""View function for home page of site"""

	if request.method == 'POST':
		form = SubmitURLForm(request.POST)

		if form.is_valid():
			data = form.cleaned_data
			new_link = Link(video_url=data['video_url'], site=data['site'], host=data['host'])
			new_link.save()
			downloader = GogoanimeDownloader()
			if new_link.site.name == 'gogoanime' and new_link.host.name == 'mp4upload':
				raw_video_link = downloader.get_raw_video_link_mp4(new_link.video_url) 
			downloader.stop()
			return HttpResponseRedirect(reverse('watch_video', args=[urllib.parse.quote(raw_video_link, safe='')]))
	else:
		form  = SubmitURLForm()

	context = {
		'form': form,
	}


	return render(request, 'index.html', context)

def watch_video(request, raw_url):
	"""View function to watch ripped video"""

	context = {
		'raw_url': urllib.parse.unquote(raw_url),
	}

	return render(request, 'watch_video.html', context)