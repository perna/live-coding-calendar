from django.db import models

SOCIAL_MEDIA_CHOICES = [
    ('github', 'github.com'),
    ('twitter', 'twitter.com'),
    ('instagram', 'instragram.com'),
    ('facebook', 'facebook.com'),
]


class BaseModel(models.Model):
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    class Meta:
        abstract = True


class Streamer(BaseModel):
    name = models.CharField(max_length=255)
    

    class Meta:
        db_table = "stream"
        verbose_name = "Streamer"
        verbose_name_plural = "Streamers"

    def __str__(self):
        return self.name


class SocialMediaStreamer(BaseModel):
    social_media = models.CharField(
        max_length=32,
        choices = SOCIAL_MEDIA_CHOICES,
        default = 'github'
    )
    url = models.URLField(max_length=255)
    streamer = models.ForeignKey(Streamer, on_delete=models.CASCADE)

    class Meta:
        db_table = "social_media"
        verbose_name = "rede social"
        verbose_name_plural = "redes sociais"

    def __str__(self):
        return self.url


class StreamChannel(BaseModel):
    name = models.CharField(max_length=128)
    url = models.URLField(max_length=255)
    streamer = models.OneToOneField(Streamer, on_delete=models.CASCADE, primary_key=True,)

    class Meta:
        db_table = "stream_channel"
        verbose_name = "canal"
        verbose_name_plural = "canais"

    def __str__(self):
        return self.name