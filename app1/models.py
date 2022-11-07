# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DtsjOld(models.Model):
    class Meta:
        managed = True
        db_table = "dtsj_old"

    id = models.IntegerField(primary_key=True, blank=True)
    bxhm = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    jfrq = models.DateField(blank=True, null=True)
    qsrq = models.DateField(blank=True, null=True)
    zzrq = models.DateField(blank=True, null=True)
    jfjs = models.FloatField(blank=True, null=True)
    jfbl = models.IntegerField(blank=True, null=True)
    jfje = models.FloatField(blank=True, null=True)
    lixi = models.FloatField(blank=True, null=True)
    znj = models.FloatField(blank=True, null=True)
    heji = models.FloatField(blank=True, null=True)
    jtzz = models.CharField(max_length=50, blank=True, null=True)
    lxdh = models.CharField(max_length=20, blank=True, null=True)


class JbxxXin(models.Model):
    class Meta:
        managed = True
        db_table = "jbxx_dt"

    id = models.IntegerField(primary_key=True, blank=True)
    sfhm = models.CharField(max_length=18, blank=True, null=True)
    bxhm = models.CharField(max_length=9, blank=True, null=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    scjz = models.DateField(blank=True, null=True)


class GrzhXin(models.Model):
    class Meta:
        managed = True
        db_table = "grzh_xin"

    GRZH_ID = models.IntegerField(primary_key=True, blank=True)
    JBXX_ID = models.IntegerField(primary_key=False, blank=True)
    sfhm_xin = models.CharField(max_length=18, blank=True, null=True)
    jznd = models.CharField(max_length=4, blank=True, null=True)
    jfjs = models.FloatField(blank=True, null=True)
    dnjfy = models.CharField(max_length=5, blank=True, null=True)
    jfrq = models.DateField(blank=True, null=True)


class JbxxZl(models.Model):
    class Meta:
        managed = True
        db_table = "jbxx_zl"

    JBXXZL_ID = models.IntegerField(primary_key=True, blank=True)
    sfhm_zl = models.CharField(max_length=18, blank=True, null=True)
    bxhm_zl = models.CharField(max_length=9, blank=True, null=True)
    name_zl = models.CharField(max_length=10, blank=True, null=True)
    jzsj_zl = models.DateField(blank=True, null=True)


class GrzhZl(models.Model):
    class Meta:
        managed = True
        db_table = "grzh_zl"

    GRZH_ID = models.IntegerField(primary_key=True, blank=True)
    JBXX_ID = models.IntegerField(primary_key=False, blank=True)
    sfhm_grzl = models.CharField(max_length=18, blank=True, null=True)
    jznd_grzl = models.CharField(max_length=4, blank=True, null=True)
    jfjs_grzl = models.FloatField(blank=True, null=True)
    jfyf_grzl = models.CharField(max_length=5, blank=True, null=True)
    jfrq_grzl = models.DateField(blank=True, null=True)
    rksj_grzl = models.CharField(max_length=6, blank=True, null=True)
