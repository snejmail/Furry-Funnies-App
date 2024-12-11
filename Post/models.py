from django.core.validators import MinLengthValidator
from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5),],
        blank=False,
        null=False,
        unique=True,
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?"
        },
    )
    image_url = models.URLField(
        blank=False,
        null=False,
        help_text="Share your funniest furry photo URL!",
    )
    content = models.TextField(
        blank=False,
        null=False,
    )
    updated_at = models.DateTimeField(
        blank=False,
        null=False,
        auto_now=True,
        editable=False,
    )
    author = models.ForeignKey(
        to='Author.Author',
        on_delete=models.CASCADE,
        editable=False,
        related_name='posts',
    )

    def __str__(self):
        return self.title
