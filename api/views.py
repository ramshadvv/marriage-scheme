from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers.tokenobtainserializer import MyTokenObtainPairSerializer
from api.serializers.accountaddserializer import AccountsSerializer
from accounts.models import Accounts
from rest_framework import status, permissions, generics
from api.permissionclass.permission import IsR1User
from datetime import date


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/token',
        '/token/refresh',
    ]
    return Response(routes)

class Register(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsR1User,)
    def post(self,request):
        self.serializer_class = AccountsSerializer(data=request.data)
        if self.serializer_class.is_valid():
            self.serializer_class.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            print(self.serializer_class.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST) 

class getUser(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Accounts.object.filter(is_admin = False)
    serializer_class = AccountsSerializer

    def get(self, request):
        self.queryset = Accounts.object.get(username = request.user)
        self.serializer_class = AccountsSerializer(self.queryset)
        return Response(self.serializer_class.data, status=status.HTTP_200_OK)
    