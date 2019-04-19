from rest_framework import serializers
from .models import MenuSection

class MenuSectionSerializer(serializers.ModelSerializer): 
	name = serializers.CharField(max_length=200)

	class Meta: 
		model = MenuSection
		fields = ('id', 'name')

	def create(self, validated_data): 
		return MenuSection.objects.create(**validated_data)

	def edit(self, instance, validated_data): 
		instance.name = validated_data.get('name', instance.name)
		instance.save()
		return instance