from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_categories'


class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'shop_brands'


color = [
    ('Черный', 'Черный'),
    ('Белый', 'Белый'),
    ('Синий', 'Синий'),
    ('Коричневый', 'Коричневый'),
    ('Зеленый', 'Зеленый'),
    ('Красный', 'Красный'),
    ('Желтый', 'Желтый'),
    ('Розвый', 'Розвый'),
    ('Фиолетовый', 'Фиолетовый'),
    ('Оранжевый', 'Оранжевый'),
]


# size = (
#     ('X', 'X'),
#     ('S', 'S'),
#     ('M', 'M'),
#     ('L', 'L'),
#     ('XL', 'XL'),
#     ('XXL', 'XXL'),
#     ('XXXL', 'XXXL'),
#     ('XXXXL', 'XXXXL'),
# )


class Cloth(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    size = models.IntegerField(null=True)
    size2 = models.CharField(max_length=255, choices=(
        ('X', 'X'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        ('XXXXL', 'XXXXL'),
    ), null=True, blank=True)
    color = models.CharField(max_length=255, choices=color, null=True)
    image = models.ImageField(blank=True, null=True,)
    available = models.BooleanField(default=True)
    gender = models.CharField(max_length=255, choices=(
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Unisex', 'Unisex'),
    ), null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'shop_clothes'


class Slide(models.Model):
    image = models.ImageField(default='slide.jpg')


RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Bad'),
    (3, '3 - Ok'),
    (4, '4 - Good'),
    (5, '5 - Perfect')
]


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return self.user.username


class Image(models.Model):
    product = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='cloth')
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)
    image4 = models.ImageField(blank=True)

    def str(self):
        return str(self.product)
