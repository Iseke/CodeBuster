from rest_framework import serializers

from django.contrib.auth.models import User

from main.models import Reviewer, Company, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ReviewerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Reviewer
        fields = ['id', 'user', 'first_name', 'last_name', 'email']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name', 'address', 'about_info', 'email']


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = ReviewerSerializer(required=False)
    company = CompanySerializer(required=False)

    class Meta:
        model = Review
        fields = ['reviewer', 'company', 'title', 'rating', 'summary', 'ip_address','date']


