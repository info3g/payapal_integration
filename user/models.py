from django.db import models


RESELLER_TYPE = (
    ('taxi', 'taxi'),
    ('hostel', 'hostel'),
)

class User(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=20,
                            choices=RESELLER_TYPE
                            )
    email = models.EmailField()
    

    def __str__(self):
        return self.name
