import datetime

from django.db import models

# Model: Product
# Description: To store all the products you buy in the
# supermarket and that you want to track.
class Product(models.Model):
    name = models.CharField('Nombre', max_length=150)
    exp_date = models.DateField('Fecha de caducidad')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField('Cantidad', default=1)

    def __str__(self):
        return self.name

    @property
    def expired(self):
        return self.exp_date < datetime.date.today()

# Model: ProductComment
# Description: To add additional comments or information to a
# product.
class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text
