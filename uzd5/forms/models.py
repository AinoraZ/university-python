from django.db import models
from django.contrib.auth.models import User


class MaterialAct(models.Model):
    institution_title = models.CharField(max_length=100)

    seller = models.CharField(max_length=100)
    invoice_series = models.CharField(max_length=10)
    sellers_code = models.CharField(max_length=100)
    date_bought = models.DateTimeField()

    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    commissioners = models.ManyToManyField(User, blank=False)
    location = models.CharField(max_length=100)

    responsible_worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responsible_worker')

    def __str__(self):
        return self.institution_title


class Materials(models.Model):
    material_act = models.ForeignKey(MaterialAct, on_delete=models.CASCADE, related_name="materials")
    name = models.CharField(max_length=100)
    amount_type = models.CharField(
        max_length=5,
        choices=(
            ("PIECE", 'Piece'),
            ("SET", 'Set'),
        ),
        default="PIECE",
    )
    amount = models.IntegerField()
    sum = models.FloatField()
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.name
