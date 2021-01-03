from rest_framework import serializers
from .models import *

class ProofCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofCategories
        fields = '__all__'


class ProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proof
        exclude = ['belonging_state']

class ProcessForDocSerialzier(serializers.ModelSerializer):
    class Meta:
        model = ProcessForDoc
        fields = '__all__'

class StepSerialzier(serializers.ModelSerializer):
    class Meta:
        model = StepOfProcess
        fields = '__all__'

class DocumentRequiredSerialzier(serializers.ModelSerializer):
    class Meta:
        model = DocumentRequiredForProof
        fields = '__all__'


class AuthorityRequiredSerialzier(serializers.ModelSerializer):
    class Meta:
        model = AuthoritySignRequiredForProof
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'