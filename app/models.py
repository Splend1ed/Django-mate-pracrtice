from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True, null=True, default=None)

    class Meta:
        ordering = ("status", )

    def __str__(self):
        return f"{self.content} ({self.created_date.strftime('%Y-%m-%d | %H:%M:%S')})"
