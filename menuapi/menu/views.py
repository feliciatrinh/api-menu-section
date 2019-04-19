from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import MenuSection
from .serializers import MenuSectionSerializer

class MenuView(APIView): 
	"""
	get: 
	Return a list of all existing menu sections. 

	post: 
	Create a new MenuSection instance. 
	"""
	def get(self, request): 
		sections = MenuSection.objects.all()
		serializer = MenuSectionSerializer(sections, many=True)
		return Response({"sections": serializer.data})	

	def post(self, request): 
		section = request.data.get('section')
		serializer = MenuSectionSerializer(data=section)
		if serializer.is_valid(raise_exception=True): 
			section_saved = serializer.save()
		return Response({"success": "Menu section '{}' created successfully.".format(section_saved.name)})

class MenuSectionView(APIView): 
	"""
	get: 
	Return the menu section matching the input id. 

	put: 
	Edit an existing menu section with the given id. 

	delete: 
	Delete an existing menu section with the given id. 
	"""
	def get(self, request, pk): 
		section = get_object_or_404(MenuSection.objects.all(), pk=pk)
		serializer = MenuSectionSerializer(section)
		return Response({"section": serializer.data})

	def put(self, request, pk): 
		saved_section = get_object_or_404(MenuSection.objects.all(), pk=pk)
		data = request.data.get('section')
		serializer = MenuSectionSerializer(instance=saved_section, data=data, partial=True)
		if serializer.is_valid(raise_exception=True): 
			section_saved = serializer.save()
		return Response({"success": "Menu section '{}' edited successfully.".format(section_saved.name)})


	def delete(self, request, pk): 
		section = get_object_or_404(MenuSection.objects.all(), pk=pk)
		section.delete()
		return Response({"success": "Menu section {} deleted.".format(pk)}, status=204)



