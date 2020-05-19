from django.contrib import admin

from .models import Streamer, SocialMediaStreamer, StreamChannel

admin.site.register(Streamer)
admin.site.register(SocialMediaStreamer)
admin.site.register(StreamChannel)
