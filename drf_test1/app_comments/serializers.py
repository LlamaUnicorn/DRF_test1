from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Country
        fields = "__all__"


class ManufacturerSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = "__all__"

    def get_comment_count(self, obj):
        return obj.comment_set.count()


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = "__all__"

    def get_comment_count(self, obj):
        return obj.comment_set.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
