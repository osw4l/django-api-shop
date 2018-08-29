from django.db import models
from django.contrib.humanize.templatetags.humanize import intcomma
# Create your models here.


class BaseName(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Category(BaseName):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def products_count(self):
        return Product.objects.filter(category=self).count()


class Product(BaseName):
    category = models.ForeignKey(
        Category
    )
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    link_cover = models.URLField()
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_price(self):
        return intcomma(self.price)


class Sale(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User')

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return 'sell # {}, created in {}, by {}'.format(
            self.id,
            self.created,
            self.user
        )

    def total_sale(self):
        return intcomma(
            sum([
                p.calculate() for p in SaleProduct.objects.filter(sale=self)
            ])
        )

    def add_item(self, id_product=None, quantity=None):
        product = Product.objects.get(id=id_product)
        product.stock -= quantity
        product.save()
        SaleProduct.objects.create(
            product_id=id_product,
            quantity=quantity,
            sale=self
        )

    def items(self):
        return SaleProduct.objects.filter(
            sale=self
        ).count()

    def get_date(self):
        return self.created.date()


class SaleProduct(models.Model):
    sale = models.ForeignKey(
        Sale,
        related_name='products'
    )
    product = models.ForeignKey(
        Product
    )
    quantity = models.PositiveIntegerField(
        default=0
    )

    def price_product(self):
        return intcomma(self.product.price)

    def total(self):
        return intcomma(self.calculate())

    def calculate(self):
        return self.product.price * self.quantity



