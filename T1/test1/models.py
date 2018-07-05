from django.db import models


class Project(models.Model):
    ProjectID = models.CharField(max_length=20)


class Doc(models.Model):
    DocProject = models.ForeignKey("Project", on_delete=models.CASCADE, related_name='Doc')
    DocType = models.CharField(default="CATPart", max_length=20)
    PartNumber = models.CharField(max_length=200)
    file = models.FileField(upload_to='.\sss', blank=True)

