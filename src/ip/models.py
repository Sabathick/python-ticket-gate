from django.db import models


class RejectList(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)

    def __str__(self):
        return str(self.ip_address)


class AllowList(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.ip_address)
