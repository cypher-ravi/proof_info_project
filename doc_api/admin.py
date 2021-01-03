from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ProofCategories)
class ProofCategoriesAdmin(admin.ModelAdmin):
    pass


class DocumentRequiredForProofInline(admin.StackedInline):
    model = DocumentRequiredForProof
  



class AuthoritySignRequiredForProofInline(admin.StackedInline):
    model = AuthoritySignRequiredForProof



class StepOfProcessInline(admin.StackedInline):
    model = StepOfProcess

@admin.register(ProcessForDoc)
class ProcessForDocAdmin(admin.ModelAdmin):
    inlines = [
        StepOfProcessInline
    ]

 
@admin.register(Proof)
class ProofAdmin(admin.ModelAdmin):
    inlines = [
        DocumentRequiredForProofInline,
        AuthoritySignRequiredForProofInline
    ]


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass

admin.site.register(State)