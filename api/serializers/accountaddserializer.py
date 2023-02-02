from accounts.models import Accounts
from rest_framework import serializers


class AccountsSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input':'password'},write_only = True)
    class Meta:
        model = Accounts
        fields = ['id','name','email','username','usertype','phone','password','password2']

        extra_kwargs = {'password':{'write_only':True}}

    def save(self):
        register = Accounts(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
            phone = self.validated_data['phone'],
            name = self.validated_data['name'],
            usertype = self.validated_data['usertype'],
        )   

        password = self.validated_data['password']
        password2 = self.validated_data['password2'] 

        if password != password2:
            raise serializers.ValidationError({'password':'Password does not match'})
        
        register.set_password(password)
        register.save()
        return register


