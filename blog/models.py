from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog.title}"
