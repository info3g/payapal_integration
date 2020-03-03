from django.db import models


PAYMENT_OPTION = (
    ('online', 'online'),
    ('offline', 'offline'),
    ('both', 'both'),
)


class Packages(models.Model):
    name = models.CharField(max_length=40,
                            unique=True
                            )
    slug = models.SlugField(max_length=40,
                            unique=True, default=None, null=True, blank=True
                            )
    description = models.TextField()
    option_1 = models.CharField(max_length=120, default=None, null=True, blank=True)
    option_2 = models.CharField(max_length=120, default=None, null=True, blank=True)
    option_3 = models.CharField(max_length=120, default=None, null=True, blank=True)
    option_4 = models.CharField(max_length=120, default=None, null=True, blank=True)
    static_img_route = models.CharField(max_length=120, default=None, null=True, blank=True)
    starting_point = models.TextField(default=None, blank=True, null=True)
    minimum_attendants = models.IntegerField(default=None, blank=True, null=True)
    occurence = models.TextField(default=None, blank=True, null=True)
    price = models.FloatField()
    discount_price = models.FloatField()
    payment_option = models.CharField(max_length=20,
                                     choices=PAYMENT_OPTION
                                     )


    def __str__(self):
        return self.name


class Gallery(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(default='index.jpg')

    def __str__(self):
        return self.name
