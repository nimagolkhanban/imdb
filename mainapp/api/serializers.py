from rest_framework import serializers
from mainapp.models import WatchList, StreamPlatform


def name_valid(data):
    if data == "admin":
        raise serializers.ValidationError("name should not be admin")
    else:
        return data
    
class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        fields = "__all__"
        
    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("name and description should be diffrent")
    #     else:
    #         return data
        
    # def validate_name(self, value):
    #     if len(value) < 2 :
    #         raise serializers.ValidationError("name is to short")
    #     else:
    #         return value   
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length
         
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        models = StreamPlatform
        fields = "__all__"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_valid])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance
        
#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("name and description should be diffrent")
#         else:
#             return data
        
#     def validate_name(self, value):
#         if len(value) < 2 :
#             raise serializers.ValidationError("name is to short")
#         else:
#             return value
        