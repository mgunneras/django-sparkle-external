from django.utils.timezone import now
from django.db import models


class VersionManager(models.Manager):

    use_for_related_fields = True

    def active(self):
        return self.get_queryset().filter(publish_at__lte=now())
