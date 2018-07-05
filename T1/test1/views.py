from rest_framework import viewsets, status, parsers
from rest_framework.response import Response
from test1.models import Project, Doc
from test1.serializers import ProjectSerializer, DocSerializer
from rest_framework.decorators import action, parser_classes


class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class DocViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Doc.objects.all()
    serializer_class = DocSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)

    """def create(self, request, *args, **kwargs):
        serializer = DocSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""


