from django.db import models
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.
class Book(models.Model):
	title           = models.CharField(max_length = 30,default = '')
	author          = models.CharField(max_length = 20,default ='')
	publication     = models.CharField(max_length = 30,default = '')
	name            = models.CharField(max_length = 15,default = '')
	phone_no        = PhoneNumberField(default = '+91 ')
	email           = models.EmailField(default = '')
	image           = models.ImageField()

	def save(self):
		im = Image.open(self.image)
		output = BytesIO()
		if (self.image.name).split('.')[-1] in ' PNG png ':
			im = im.convert('RGB')
		im = im.resize( (300,300) )
		im.save(output, format='jpeg', quality=100)
		output.seek(0)
		self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		super(Book,self).save()