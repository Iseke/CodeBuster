from django.http import JsonResponse
from django.shortcuts import  render, redirect
from django.contrib.auth.models import User

from main.forms import ExtendUserCreationForm, ReviewerForm

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token as TokenModel
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = TokenModel.objects.get_or_create(user=user)
    return Response({'token': token.key})


@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def logout(request):
    token = TokenModel(request.auth)
    token.delete()
    return Response(status=status.HTTP_200_OK)


@permission_classes((IsAdminUser,))
@api_view(['POST', 'GET'])
def registerReviewer(request):
    if request.method == 'POST':
        form = ExtendUserCreationForm(request.data)
        rev_form  = ReviewerForm(request.data)

        if form.is_valid() and rev_form.is_valid(): # When create a User, automatically create Reviewer with current data
            user = form.save()
            profile = rev_form.save(commit=False)
            profile.user = user
            profile.email = user.email
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.save()
            return Response({'idd': profile.id}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        form = ExtendUserCreationForm()
        rev_form = ReviewerForm()

        args = {'form': form, 'rev_form': rev_form}
        return render(request, 'register.html', args)