from django.db import models

class Location(models.Model):
    city = models.CharField(verbose_name="Cidade", max_length=200)
    state = models.CharField(verbose_name="Estado", max_length=200)

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return f"{self.city}/{self.state}"


class Work(models.Model):
    photo = models.ImageField(
        verbose_name="Imagem", upload_to="images/", null=False, blank=False
    )
    location = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name="Local")

    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"


    def __str__(self):
        return f"{self.location}"
