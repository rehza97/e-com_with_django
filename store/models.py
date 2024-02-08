
from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField  # Import AutoSlugField from django-autoslug
from category.models import *

class Product(models.Model):
    product_name = models.CharField(_('product name'), max_length=200)
    slug = AutoSlugField(_('slug'), unique=True, populate_from='product_name')  # Use AutoSlugField instead of SlugField
    description = models.TextField(_('description'), blank=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, help_text=_('in USD'))
    image = models.ImageField(_('image'), upload_to='products/')
    stock = models.PositiveIntegerField(_('stock'))
    is_available = models.BooleanField(_('is available'), default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True)
    
    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-created_date']

    def __str__(self):
        return self.product_name

    def is_in_stock(self):
        return self.stock > 0
    is_in_stock.boolean = True
    is_in_stock.short_description = _('in stock')



# import uuid
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from category.models import *
# from django.utils.text import slugify

# class Product(models.Model):
#     product_name = models.CharField(_('product name'), max_length=200)
#     slug = models.SlugField(_('slug'), unique=True, blank=True)
#     description = models.TextField(_('description'), blank=True)
#     price = models.DecimalField(_('price'), max_digits=10, decimal_places=2, help_text=_('in USD'))
#     image = models.ImageField(_('image'), upload_to='products/')
#     stock = models.PositiveIntegerField(_('stock'))
#     is_available = models.BooleanField(_('is available'), default=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('category'))
#     created_date = models.DateTimeField(_('created date'), auto_now_add=True)
#     modified_date = models.DateTimeField(_('modified date'), auto_now=True)
    
#     class Meta:
#         verbose_name = _('product')
#         verbose_name_plural = _('products')
#         ordering = ['-created_date']

#     def __str__(self):
#         return self.product_name

#     def is_in_stock(self):
#         return self.stock > 0
#     is_in_stock.boolean = True
#     is_in_stock.short_description = _('in stock')

#     def save(self, *args, **kwargs):
#             if not self.slug:
#                 self.slug = slugify(self.product_name)
#                 # Check if the generated slug already exists
#                 while Product.objects.filter(slug=self.slug).exists():
#                     # If it does, append a number to make it unique
#                     self.slug = slugify(self.product_name) + '-' + str(uuid.uuid4())[:5]
#             super().save(*args, **kwargs)