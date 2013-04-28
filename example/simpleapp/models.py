from django.db import models
from django.conf import settings


class LookupModel(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class SimpleModel(models.Model):
    """
    (SimpleModel description)
    """

    char_field = models.CharField(max_length=255)
    slug_field = models.SlugField(unique=True)
    email_field = models.EmailField()
    text_field = models.TextField()

    biginteger_field = models.BigIntegerField(blank=True)
    integer_field = models.IntegerField(blank=True)
    positiveinteger_field = models.PositiveIntegerField(blank=True, null=True)
    smallinteger_field = models.SmallIntegerField(blank=True, null=True)
    possmallinteger_field = models.PositiveSmallIntegerField(blank=True, null=True)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    float_field = models.FloatField(blank=True, null=True)
    csi_field = models.CommaSeparatedIntegerField(max_length=255, blank=True, null=True)

    boolean_field = models.BooleanField(default=False)
    nullboolean_field = models.NullBooleanField(blank=True, null=True)

    date_field = models.DateField(blank=True, null=True)
    time_field = models.TimeField(blank=True, null=True)
    datetime_field = models.DateTimeField(blank=True, null=True)

    file_field = models.FileField(upload_to="files", blank=True, null=True)
    filepath_field = models.FilePathField(blank=True, path="%s/simpleapp/templates/simpleapp" % settings.PROJ_ROOT, null=True)
    image_field = models.ImageField(upload_to="images", blank=True, null=True)

    ipaddress_field = models.IPAddressField(blank=True, null=True)
    genericipaddress_field = models.GenericIPAddressField(blank=True, null=True)
    url_field = models.URLField(blank=True, null=True)

    foreignkey_field = models.ForeignKey(LookupModel, blank=True, null=True)
    manytomany_horiz = models.ManyToManyField(LookupModel, related_name="h+", blank=True, null=True)
    manytomany_vert = models.ManyToManyField(LookupModel, related_name="v+", blank=True, null=True)

    def __unicode__(self):
        return self.char_field

    @models.permalink
    def get_absolute_url(self):
        return ('simplemodel_detail_view_name', [str(self.id)])


class TabularModel(models.Model):
    parent = models.ForeignKey(SimpleModel)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class StackedModel(models.Model):
    parent = models.ForeignKey(SimpleModel)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class NoInlineModel(models.Model):
    parent = models.ForeignKey(SimpleModel)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
