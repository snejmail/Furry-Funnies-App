from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from Post.models import Post


def letters_only_check(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


def validate_passcode(value):
    if len(value) != 6:
        raise ValidationError("Your passcode must be exactly 6 digits!")


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[MinLengthValidator(4),
                    letters_only_check,],
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(2),
                    letters_only_check,],
        blank=False,
        null=False,
    )
    passcode = models.CharField(
        blank=False,
        null=False,
        validators=[validate_passcode],
        help_text="Your passcode must be a combination of 6 digits",
    )
    pets_number = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )
    info = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def get_profile_picture(self):
        return self.image_url if self.image_url else '/staticfiles/images/default.png'

    @property
    def total_posts(self):
        return Post.objects.filter(author=self).count()

    @property
    def last_updated_post_title(self):
        last_post = Post.objects.filter(author=self).order_by('-updated_at').first()
        return last_post.title if last_post else 'N/A'

