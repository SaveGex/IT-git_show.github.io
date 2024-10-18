from django.db import models
from django.utils import timezone
# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=False, blank=True)
    link = models.TextField(null=False,blank=False)
    published_date = models.TimeField(default=timezone.now)
    link_image = models.TextField(null=False, blank=True)
    identifier = models.TextField(default=None, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.identifier:
            self.identifier = f"_UniqueName_{self.name}_{timezone.now()}"
        super().save(*args, **kwargs)
