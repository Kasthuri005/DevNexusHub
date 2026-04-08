from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(default=5)  # Rating out of 10
    video_url = models.URLField(blank=True, null=True)  # YouTube Embed Link
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_embed_url(self):
        
        if "youtube.com" in self.video_url:
            return self.video_url.replace("watch?v=", "embed/")
        elif "youtu.be" in self.video_url:
            return self.video_url.replace("youtu.be/", "youtube.com/embed/")
        elif "vimeo.com" in self.video_url:
            return self.video_url.replace("vimeo.com", "player.vimeo.com/video")
        return self.video_url       
