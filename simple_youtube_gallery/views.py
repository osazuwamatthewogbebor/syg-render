from django.shortcuts import render, redirect
from .models import Video
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse, parse_qs

def extract_video_id(youtube_url):
    try:
        # Extract the video ID from the YouTube URL
        parsed_url = urlparse(youtube_url)
        query_params = parse_qs(parsed_url.query)
        video_id = query_params.get('v', [None])[0]
        return video_id
    except Exception as e:
        print(f"Error extracting video ID: {e}")
        return None


@csrf_exempt
def index(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            # Delete action
            video_id = request.POST.get('video_id')
            Video.objects.filter(id=video_id).delete()
        else:
            # Add video action
            title = request.POST.get('title')
            youtube_url = request.POST.get('youtube_url')
            video_id = extract_video_id(youtube_url)

            if title and video_id:
                Video.objects.create(title=title, youtube_url=youtube_url, youtube_id=video_id)

        return redirect('index')

    # GET request - retrieve all videos
    videos = Video.objects.all()
    return render(request, 'simple_youtube_gallery/index.html', {'videos': videos})
