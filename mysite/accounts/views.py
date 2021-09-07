from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import GeneralUser
from .serializers import GeneralUserSerializer
from .utils import get_tokens_for_user

from django.contrib.auth.hashers import check_password

from .permissions import IsRider, IsDriver

# Create your views here.

class UserCreateView(APIView):
    def post(self, request):
        data = {}
        print('Getting POST data: ', request.data)

        serializer_data = {}
        serializer_data['first_name'] = request.data['firstName']
        serializer_data['last_name'] = request.data['lastName']
        serializer_data['username'] = request.data['username']
        serializer_data['email'] = request.data['email']
        serializer_data['password'] = request.data['password']
        serializer_data['user_type'] = request.data['userType']
        print('serializer_data: ', serializer_data)
        serializer = GeneralUserSerializer(data=serializer_data)
        print('serializer: ', serializer)

        print('Checking validity:')
        if serializer.is_valid():
            print('Valid!')
            generaluser = serializer.save()
            data['response'] = 'User created successfully.'
            data['id'] = generaluser.id
            data['user_type'] = generaluser.user_type

            return Response(data)
            
        print('Invalid!')
        data = serializer.errors
        print(data)

        return Response(data)

class UserTokensView(APIView):
    def post(self, request):
        print('request.data: ', request.data)
        
        username = request.data['username']
        password = request.data['password']
        print('username: ', username)
        print('password: ', password)

        try:
            generaluser = GeneralUser.objects.get(username=username)
        except:
            return Response({'message': 'User does not exist.'})

        if generaluser.is_activated and check_password(password, generaluser.password):
            return Response(get_tokens_for_user(generaluser))
        
        return Response({'message:' : 'Invalid password or account not active!'})

# class BecomeRider(APIView):
#     permission_classes = [IsAuthenticated,]

#     def post(self, request):
#         generaluser = request.user
#         if not generaluser.is_rider:
#             generaluser.is_rider = True
#             generaluser.save()
#             return Response({'message': 'You are now a rider.'})
        
#         return Response({'message': 'You are already a rider.'})

# class BecomeDriver(APIView):
#     permission_classes = [IsAuthenticated,]

#     def post(self, request):
#         generaluser = request.user
#         if not generaluser.is_driver:
#             driver = Driver(generaluser=generaluser, license_credentials=request.data['licenseCredentials'])
#             driver.save()
#             generaluser.is_driver = True
#             generaluser.save()
#             return Response({'message': 'You are now a driver.'})
        
#         return Response({'message': 'You are already a driver.'})

class OnlySpecificType(APIView):
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        data = {
            'id': request.user.id,
            'user_type': request.user.user_type,
            'access_token': token
        }
        return Response(data)

class OnlyRider(OnlySpecificType):
    permission_classes = [IsAuthenticated, IsRider]

class OnlyDriver(OnlySpecificType):
    permission_classes = [IsAuthenticated, IsDriver]

# cURL commands for testing

# POST create user by providing the necessary fields
# curl -X POST -H "Content-Type: application/json" -d "{\"firstName\": \"Kamruzzaman\", \"lastName\": \"Tauhid\", \"username\": \"tauhid\", \"email\": \"17201114@uap-bd.edu\", \"password\": \"eastwestnets\", \"userType\": 1}" http://127.0.0.1:8000/accounts/user_create_view/

# POST obtain jwt token pair using username and password
# curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"tauhid\", \"password\": \"eastwestnets\"}" "http://localhost:8000/accounts/user_tokens_view/"

# POST obtain new access token using refresh token
# curl -X POST -H "Content-Type: application/json" -d "{\"refresh\":\"MY_REFRESH_TOKEN\"}" http://localhost:8000/accounts/api/token/refresh/

# POST become a rider
# curl -X POST -H "Authorization: Bearer MY_ACCESS_TOKEN" -H "Content-Type: application/json" -d "{\"licenseCredentials\": \"MYCREDENTIALS\"}" http://localhost:8000/accounts/become_rider/

# POST become a driver by providing license credentials
# curl -X POST -H "Authorization: Bearer MY_ACCESS_TOKEN" -H "Content-Type: application/json" -d "{\"licenseCredentials\": \"MYCREDENTIALS\"}" http://localhost:8000/accounts/become_driver/

# GET access protected view for only riders
# curl -H "Authorization: Bearer MY_ACCESS_TOKEN" http://localhost:8000/accounts/only_rider/

# GET access protected view for only drivers
# curl -H "Authorization: Bearer MY_ACCESS_TOKEN" http://localhost:8000/accounts/only_driver/

# simplejwt documentation

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html
#                                         --------------------

# Django multiple user guide
# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
#                                         --------------------

# cURL command guide
# https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
#                                         --------------------

# StackOverflow random
# https://stackoverflow.com/questions/63046840/getting-user-details-from-access-token-in-django-rest-framework-simple-jwt
#                                         --------------------