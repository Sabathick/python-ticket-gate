from django.db import models


class RejectList(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)

    def __str__(self):
        return str(self.ip_address)

    def save_to_database(self):
        self.save()

    def delete_from_database(self):
        self.delete()


class AllowList(models.Model):
    ip_address = models.GenericIPAddressField(primary_key=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.ip_address)

    def save_to_database(self):
        self.save()

    def delete_from_database(self):
        self.delete()
