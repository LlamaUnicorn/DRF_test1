from rest_framework import serializers
from .models import Country, Manufacturer, Car, Comment


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name']


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'name', 'manufacturers']


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


class ManufacturerDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    cars = CarSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'country', 'cars', 'comment_count']

    def get_comment_count(self, obj):
        return Comment.objects.filter(car__manufacturer=obj).count()


# Allows for single country creation without specifying the manufacturer

# class CountrySerializer(serializers.ModelSerializer):
#     id = serializers.ReadOnlyField()

#     class Meta:
#         model = Country
#         fields = '__all__'


# class ManufacturerSerializer(serializers.ModelSerializer):
#     country = serializers.StringRelatedField()
#     comment_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Manufacturer
#         fields = "__all__"

#     def get_comment_count(self, obj):
#         return obj.comment_set.count()


# -----------------------------------------------------
# class ManufacturerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Manufacturer
#         fields = ['id', 'name']

# class CountrySerializer(serializers.ModelSerializer):
#     manufacturers = ManufacturerSerializer(many=True)

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
