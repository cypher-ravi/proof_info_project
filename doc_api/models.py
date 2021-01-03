from django.db import models

VALID_STATE_CHOICES = (
    ("1", "Please Select"),
    ("Andhara Pradesh", "Andhra Pradesh"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chhattisgarh", "Chhattisgarh"),
    ("Chandigarh", "Chandigarh"),
    ("Dadar and Nagar Haveli", "Dadar and Nagar Haveli"),
    ("Daman and Diu", "Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Jharkhand", "Jharkhand"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Lakshadeep", "Lakshadeep"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Orissa", "Orissa"),
    ("Punjab", "Punjab"),
    ("Pondicherry", "Pondicherry"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telagana", "Telagana"),
    ("Tripura", "Tripura"),
    ("Uttaranchal", "Uttaranchal"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("West Bengal", "West Bengal"),
    ("Andaman and Nicobar Island", "Andaman and Nicobar Island"),

)
VALID_STATUS_CHOICES = (
    ("National", "National"),
    ("State", "State"),
)

# Create your models here.
class ProofCategories(models.Model):
    name = models.CharField(max_length=220,default='')
    published_date = models.DateTimeField(auto_now_add=True)    
     

    class Meta:
        verbose_name = ("ProofCategories")
        verbose_name_plural = ("Proof Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProofCategories_detail", kwargs={"pk": self.pk})

class State(models.Model):
    belonging_state = models.CharField(max_length=255,default='',choices=VALID_STATE_CHOICES)

    def __str__(self):
        return self.belonging_state

class Proof(models.Model):
    name = models.CharField(max_length=225,default='')
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='documents/img')
    belonging_state = models.ManyToManyField(State,blank=True)
    status = models.CharField(max_length=255,default='',choices=VALID_STATUS_CHOICES,blank=True, null=True)
   

    
    class Meta:
        verbose_name = ("Proof")
        verbose_name_plural = ("Proofs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Proof_detail", kwargs={"pk": self.pk})


class DocumentRequiredForProof(models.Model):
    name = models.CharField(max_length=225,default='')
    proof = models.ForeignKey(Proof,on_delete=models.CASCADE,blank=True,null=True)


    class Meta:
        verbose_name = ("DocumentRequiredForProof")
        verbose_name_plural = ("List of document required for proofs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DocumentRequiredForProof_detail", kwargs={"pk": self.pk})


class AuthoritySignRequiredForProof(models.Model):
    name = models.CharField(max_length=225,default='')
    address_of_authority_for_sign = models.CharField(max_length=500,default='')
    proof = models.ForeignKey(Proof,on_delete=models.CASCADE,blank=True,null=True)
    

    class Meta:
        verbose_name = ("AuthoritySignRequiredForProof")
        verbose_name_plural = ("Authority Signs Required For Proofs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("AuthorityRequiredForProof_detail", kwargs={"pk": self.pk})



class ProcessForDoc(models.Model):
    name = models.CharField(max_length=225,default='',help_text="for eg. adhaar card doc process")
    proof = models.ForeignKey(Proof,on_delete=models.CASCADE,blank=True,null=True)
    
    

    class Meta:
        verbose_name = ("ProcessForDoc")
        verbose_name_plural = ("Process for documents")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProcessForDoc_detail", kwargs={"pk": self.pk})

class StepOfProcess(models.Model):
    step_desc = models.TextField()
    process = models.ForeignKey(ProcessForDoc,on_delete=models.CASCADE,blank=True,null=True)
    

    class Meta:
        verbose_name = ("StepOfProcess")
        verbose_name_plural = ("Step of Processs")

    def __str__(self):
        return self.step_desc

    def get_absolute_url(self):
        return reverse("StepOfProcess_detail", kwargs={"pk": self.pk})

class Feedback(models.Model):
    title = models.CharField(max_length=225,default='')
    description = models.TextField()    
    

    class Meta:
        verbose_name = ("Feedback")
        verbose_name_plural = ("Feedbacks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Feedback_detail", kwargs={"pk": self.pk})
