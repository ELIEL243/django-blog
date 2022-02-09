from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify
from django.urls import reverse

User = get_user_model()


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publie")
    content = models.TextField(blank=True, verbose_name="Contenu")
    image = models.ImageField(blank=True, upload_to='blog')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Post"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail-post", kwargs={"pk": self.pk})


