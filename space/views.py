from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from space.serializers import SpaceSerializer
from space import service as space_service


@api_view(["POST"])
def add_space(request):
    space = space_service.add_space(req_dict=request.data)
    serializer = SpaceSerializer(space)
    return serializer.data


@api_view(["GET"])
def get_spaces(request):
    active_only = request.GET.get("active_only", False)
    spaces = space_service.get_spaces(active_only=active_only)
    serializer = SpaceSerializer(spaces, many=True)
    return serializer.data


