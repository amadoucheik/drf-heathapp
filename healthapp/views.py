from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import DataSerializer
from .models import Data
from rest_framework import status
from rest_framework.views import APIView
#for generic view
from rest_framework import generics
from rest_framework import mixins
#end generic view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework import viewsets

#generic viewset

class DataViewSet(viewsets.ModelViewSet):

    serializer_class = DataSerializer
    queryset = Data.objects.all()

    

class DataViewSet2(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin
                  ,mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = DataSerializer
    queryset = Data.objects.all()
    
    
# end generic viewset

#viewset
class DataViewSet1(viewsets.ModelViewSet):

    serializer_class = DataSerializer
    queryset = Data.objects.all()


    def list(self, request):
        app = Data.objects.all()
        serializer = DataSerializer(app, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        app = Data.objects.get(id=pk)
        serializer = DataSerializer(app, many=False)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        app = Data.objects.get(id=pk)
        serializer = DataSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
#end viewset

#generic view
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    """
    A generic view for handling CRUD operations on Data model.
    Supports GET (list), POST (create), PUT (update), and DELETE (delete) methods.
    """

    serializer_class = DataSerializer
    queryset = Data.objects.all()

    lookup_field = 'id'

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    #authentification_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.destroy(request, id)
    
#end generic view

    
#dataAPIView
class DataAPIView(APIView):

    def get(self, request):
        app = Data.objects.all()
        serializer = DataSerializer(app, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)  

#APIView Details
class dataDetails(APIView):

    def get_object(self, pk):
        try:
            return Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        app = self.get_object(pk)
        serializer = DataSerializer(app)
        return Response(serializer.data)

    def put(self, request, pk):
        app = self.get_object(pk)
        serializer = DataSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        app = self.get_object(pk)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
@api_view(['GET'])
def getData(request):

    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def data_Details(request, pk):
    
    try:
        app = Data.objects.get(id=pk)
        serializer = DataSerializer(app, many=False)
        return Response(serializer.data)
    
    except Data.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    