from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Image
        fields = '__all__'
