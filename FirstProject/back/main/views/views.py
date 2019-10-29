from main.serializers import ReviewerSerializer, CompanySerializer, ReviewSerializer
from main.models import Reviewer, Review, Company

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@permission_classes((IsAdminUser,))
class GetAllReviews(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@permission_classes((IsAuthenticated,))
class GetMyReview(APIView):
    def get(self, request):
        print(request.user)
        reviews = Review.objects.filter(reviewer__user=request.user)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
class PostReview(APIView):
    def post(self, request):
        comp_id = request.data.pop('company')
        usr = request.user
        cur_company = Company.objects.get(id=comp_id)
        cur_reviewer = Reviewer.objects.get(user=usr)
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(reviewer=cur_reviewer, company=cur_company)
        return Response(serializer.data, status=status.HTTP_200_OK)
