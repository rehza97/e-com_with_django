from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200,unique = True)
    slug = models.SlugField(unique = True)
    description = models.TextField()
    cat_image = models.ImageField(upload_to='MEDIA/categories',blank=True)
    
    class Meta:
        verbose_name  = 'Category'
        verbose_name_plural = 'Catgories'
    

    
    def __str__(self) -> str:
        return self.category_name