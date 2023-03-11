import re
from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country']


# class CountrySerializer(serializers.ModelSerializer):
#     manufacturers = ManufacturerSerializer(many=True, read_only=True)

#     class Meta:
#         model = Country
#         fields = ['id', 'name', 'manufacturers']


# class CarSerializer(serializers.ModelSerializer):
#     manufacturer = ManufacturerSerializer()
#     comment_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Car
#         fields = "__all__"

#     def get_comment_count(self, obj):
#         return obj.comment_set.count()


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'email', 'car', 'comment', 'created_at']

#     def validate_car(self, value):
#         """
#         Check that the car object exists.
#         """
#         if not Car.objects.filter(id=value.id).exists():
#             raise serializers.ValidationError("Invalid car ID")
#         return value

#     def validate(self, data):
#         """
#         Check that the email field is valid.
#         """
#         email = data.get('email', None)
#         if not email:
#             raise serializers.ValidationError("Email is required")
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise serializers.ValidationError("Invalid email format")
#         return data


# class ManufacturerDetailSerializer(serializers.ModelSerializer):
#     country = CountrySerializer()
#     cars = CarSerializer(many=True, read_only=True)
#     comment_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Manufacturer
#         fields = ['id', 'name', 'country', 'cars', 'comment_count']

#     def get_comment_count(self, obj):
#         return Comment.objects.filter(car__manufacturer=obj).count()


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'manufacturers']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['manufacturers'] = ManufacturerSerializer(instance.manufacturers.all(), many=True).data
        return representation


class CarSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'manufacturer', 'start_year', 'end_year', 'comment_count']

    def get_comment_count(self, obj):
        return obj.comment_set.count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['manufacturer'] = ManufacturerSerializer(instance.manufacturer).data
        representation['comment_count'] = self.get_comment_count(instance)
        return representation
    
    def create(self, validated_data):
        manufacturer_data = validated_data.pop('manufacturer')
        manufacturer = Manufacturer.objects.get_or_create(**manufacturer_data)[0]
        car = Car.objects.create(manufacturer=manufacturer, **validated_data)
        return car
    

class ManufacturerDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    cars = CarSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'cars', 'comment_count']

    def get_comment_count(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['country'] = CountrySerializer(instance.country).data
        representation['cars'] = CarSerializer(instance.cars.all(), many=True).data
        representation['comment_count'] = self.get_comment_count(instance)
        return representation





class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Comment
        fields = ['id', 'email', 'car', 'comment', 'created_at']

    def validate_car(self, value):
        """
        Check that the car object exists.
        """
        if not Car.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Invalid car ID")
        return value

    def validate(self, data):
        """
        Check that the email field is valid.
        """
        email = data.get('email', None)
        if not email:
            raise serializers.ValidationError("Email is required")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise serializers.ValidationError("Invalid email format")
        return data

