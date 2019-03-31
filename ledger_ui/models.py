from django.contrib.auth.models import User
from django.db import models


class LedgerPath(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    path = models.CharField(max_length=1024)

    def __str__(self):
        return "{}: {}".format(self.user, self.path)