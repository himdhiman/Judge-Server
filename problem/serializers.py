from rest_framework import serializers
from problem import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"

class ProblemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True, read_only = True)
    class Meta:
        model = models.Problem
        fields = "__all__"