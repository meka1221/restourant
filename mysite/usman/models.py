from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ("gold", "gold"),
        ("silver", "silver"),
        ("bronze", "bronze")
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='bronze')


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Food(models.Model):
    resto_name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/', verbose_name='изображение')
    price = models.IntegerField()

    def __str__(self):
        return self.resto_name


class Courier(models.Model):
    courier_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(default=0)
    STATUS_CHOICES = (
        ("car","car"),
        ("bike","bike"),
        ("walk", "walk")
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return self.courier_name


class Order(models.Model):
    order_number = models.PositiveIntegerField()
    resto_name = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    delivery_time = models.DateTimeField(auto_now_add=True)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    STATUS_CHOICES = (
           ("Д","Доставлено"),
           ("Вп","В пути"),
           ("ОП","Ожидает получения")
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Доставка для заказа{self.order}"


class Rating(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], verbose_name="Rating")

    def __str__(self):
        return f"Рейтинг для {self.food} от {self.user}"


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    resto = models.ForeignKey(Food, on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв для {self.resto} от{self.author}"


