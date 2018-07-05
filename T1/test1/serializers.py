from rest_framework import serializers
from test1.models import Project, Doc


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'ProjectID')


class DocSerializer(serializers.ModelSerializer):
    DocProject = serializers.SlugRelatedField(slug_field='ProjectID', queryset=Project.objects.all())
    file = serializers.FileField(use_url=True)

    class Meta:
        model = Doc
        fields = '__all__'



