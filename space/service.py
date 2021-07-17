from rest_framework.exceptions import ValidationError

from space.models import Space
from space.serializers import SpaceSerializer


def add_space(req_dict: dict):
    serializer = SpaceSerializer(data=req_dict)
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)

    validated_data = serializer.validated_data
    return Space.objects.create(**validated_data)


def get_spaces(active_only: bool = True):
    if active_only:
        return Space.objects.filter(activate=True)

    return Space.objects.all()







