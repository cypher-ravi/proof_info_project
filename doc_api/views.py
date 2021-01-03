from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import generics
from rest_framework import filters

from .models import *
from .serializers import *
# Create your views here.
from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer,BrowsableAPIRenderer

class ListOfCategoriesView(generics.ListAPIView):
    queryset = ProofCategories.objects.all()
    serializer_class = ProofCategoriesSerializer
  

class ListOfProofsView(generics.ListAPIView):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer
  
    def get(self,request, *args, **kwargs):
        proofs = Proof.objects.filter(belonging_state__belonging_state=kwargs['state'])
        print(proofs)
        if proofs.exists():
            serializer = ProofSerializer(proofs,many=True)
            return Response(serializer.data)
        return Response({'detail':'no proof from this state'})
    

class ProofDetailAPIView(generics.RetrieveAPIView):
    serializer_class = StepSerialzier
    queryset = ProcessForDoc.objects.all()

    def get(self, request, *args, **kwargs):
        proof = Proof.objects.filter(id=kwargs['pk'])
        if not proof:
            return Response({'proof not exists'})
        process_of_proof = ProcessForDoc.objects.get(proof = proof[0])
        steps = StepOfProcess.objects.filter(process=process_of_proof)
        serialize_steps = StepSerialzier(steps,many=True)

        doc_required = DocumentRequiredForProof.objects.filter(proof=proof[0])
        serialize_docs = DocumentRequiredSerialzier(doc_required,many=True)

        authority_required = AuthoritySignRequiredForProof.objects.filter(proof=proof[0])
        serialize_authority = AuthorityRequiredSerialzier(authority_required,many=True)

        return Response({'steps':serialize_steps.data,'documents_required':serialize_docs.data,'authority_required':serialize_authority.data})


class FeedbackAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ProofSearchAPIView(generics.ListAPIView):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']