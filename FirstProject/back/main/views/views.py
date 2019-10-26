from main.serializers import ReviewerSerializer, CompanySerializer, ReviewSerializer
from main.models import Reviewer, Review, Company

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@permission_classes((IsAuthenticated,))
class GetAllCompany(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class GetAllReviews(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer