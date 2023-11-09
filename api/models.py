
from django.db import models

class Category(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    cat_id = models.IntegerField(blank=True, null=True)
    cat_name_bn = models.TextField(blank=True, null=True)
    cat_name_en = models.TextField(blank=True, null=True)
    no_of_subcat = models.IntegerField(blank=True, null=True)
    no_of_dua = models.IntegerField(blank=True, null=True)
    cat_icon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

class SubCategory(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    cat_id = models.IntegerField(blank=True, null=True)
    subcat_id = models.IntegerField(blank=True, null=True)
    subcat_name_bn = models.TextField(blank=True, null=True)
    subcat_name_en = models.TextField(blank=True, null=True)
    no_of_dua = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_category'


class Dua(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    cat_id = models.IntegerField(blank=True, null=True)
    subcat_id = models.IntegerField(blank=True, null=True)
    dua_id = models.IntegerField(blank=True, null=True)
    dua_name_bn = models.TextField(blank=True, null=True)
    dua_name_en = models.TextField(blank=True, null=True)
    top_bn = models.TextField(blank=True, null=True)
    top_en = models.TextField(blank=True, null=True)
    dua_arabic = models.TextField(blank=True, null=True)
    dua_indopak = models.TextField(blank=True, null=True)
    clean_arabic = models.TextField(blank=True, null=True)
    transliteration_bn = models.TextField(blank=True, null=True)
    transliteration_en = models.TextField(blank=True, null=True)
    translation_bn = models.TextField(blank=True, null=True)
    translation_en = models.TextField(blank=True, null=True)
    bottom_bn = models.TextField(blank=True, null=True)
    bottom_en = models.TextField(blank=True, null=True)
    refference_bn = models.TextField(blank=True, null=True)
    refference_en = models.TextField(blank=True, null=True)
    audio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dua'
