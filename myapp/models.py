from django.db import models



PERSONAL_CHOICES = (
    ('Juridical', 'Juridical'),
    ('Physical', 'Physical'),
)

STATUS_CHOICES = (
    ('New', 'New'),
    ('Moderated', 'Moderated'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),
)

STUDENT_CHOICES = (
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master',)
)

PAYMENT_CHOICES = (
    ('CASH', 'Cash'),
    ('PAYME', 'Pay me'),
    ('CLICK', 'Click'),
    ('ENUMERATION', 'Enumeration')
)


class University(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name



class Sponsor(models.Model):
    name = models.CharField(max_length=60)
    personal = models.CharField(choices=PERSONAL_CHOICES, default='Physical', max_length=50)
    phone = models.CharField(default='9989', null=True, max_length=100)
    amount = models.IntegerField(null=True, default=1000000)
    company = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='New', max_length=50)
    paid = models.IntegerField(default=0)
    payment_method = models.CharField(choices=PAYMENT_CHOICES, default='CASH', max_length=100)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class Student(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(default='9989', null=True, max_length=100)
    degree = models.CharField(choices=STUDENT_CHOICES, max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    money_needed = models.IntegerField(default=0)
    money_gained = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name



class Contract(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    money = models.IntegerField()


    def __str__(self):
        return (str(self.sponsor) + " -> " + str(self.student))


