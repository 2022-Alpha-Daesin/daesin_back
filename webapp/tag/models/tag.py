from django.db import models


class Tag(models.Model):
    class Meta:
        db_table = 'tags'
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    content = models.CharField(
        max_length=100,
        verbose_name='태그',
        unique=True
    )
    parent = models.ForeignKey(
        'self',
        on_delete= models.CASCADE, 
        null=True,blank=True,
        related_name='children',
        verbose_name='상위태그'
        )
    
    
