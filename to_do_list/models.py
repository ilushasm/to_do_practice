from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")
