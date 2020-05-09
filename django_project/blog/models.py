from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.class (models.Model):
    tilte = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    

    class Meta:
        verbose_name = _("")
        verbose_name_plura
        tilte = models.CharField(_(""), max_length=50)l = _("s")
        tilte = models.CharField(_(""), max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

tilte = models.CharField(_(""), max_length=50))