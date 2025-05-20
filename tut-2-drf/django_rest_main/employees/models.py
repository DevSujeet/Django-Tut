from django.db import models
import uuid

# Create your models here.
class Employee(models.Model):
    emp_id = emp_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name