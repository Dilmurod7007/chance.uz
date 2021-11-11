from django.db import models


# Create your models here.

TOIFA_CHOICES = (
    ('Yuridikt', 'Yuridikt'),
    ('Jismoniy', 'Jismoniy'),
)

HOLATI_CHOICES = (
    ('Yangi', 'Yangi'),
    ('Moderatsiada', 'Moderatsiada'),
    ('Tasdiqlangan', 'Tasdiqlangan'),
    ('Bekor qilingan', 'Bekor qilingan'),
)

TALABA_CHOICES = (
    ('Bakalavr', 'Bakalavr'),
    ('Magister', 'Magister',)
)


SUMMA_CHOICES = (
    ('1 000 000', '1 000 000'),
    ('5 000 000', '5 000 000'),
    ('7 000 000', '7 000 000'),
    ('30 000 000', '30 000 000'),
)



class Homiy(models.Model):
    ismi = models.CharField(max_length=60)
    turi = models.CharField(choices=TOIFA_CHOICES, max_length=50)
    raqami = models.IntegerField(default=9989)
    summa = models.IntegerField(choices=SUMMA_CHOICES, editable=True, default=0)
    tashkilot = models.CharField(max_length=255, blank=True, null=True)
    holati = models.CharField(choices=HOLATI_CHOICES, default='Yangi', max_length=50)
    sarflangan_summa = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Homiylar'

    def __str__(self):
        return self.ismi



class Talaba(models.Model):
    ismi = models.CharField(max_length=50)
    talabalik_turi = models.CharField(choices=TALABA_CHOICES, max_length=50)
    otm = models.CharField(max_length=255)
    kontrakt_summa = models.IntegerField(default=0)
    ajratilgan_summa = models.IntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Talabalar'

    def __str__(self):
        return self.ismi

