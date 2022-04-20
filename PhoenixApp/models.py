from django.db import models
from autoslug import AutoSlugField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


class Review(models.Model):
    review = models.TextField()
    date = models.DateField()


class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=10, default="")
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class PreviousEvent(models.Model):
    title = models.CharField(max_length=50, default="")
    slug = AutoSlugField(populate_from='title')
    desc = models.TextField()
    is_for_result = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class UpComingEvent(models.Model):
    up_event_id = models.AutoField
    title = models.CharField(max_length=50, default="")
    desc = models.TextField()
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(upload_to="upcomingevents/images", default="")

    def __str__(self):
        return self.title


class Result(models.Model):
    eventname = models.ForeignKey(
        PreviousEvent, default="", on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='eventname', default="")
    studentname = models.CharField(max_length=60, default="")
    position = models.CharField(max_length=10, default="")
    year = models.CharField(max_length=10, default="")
    department = models.CharField(max_length=50, default="")
    college = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to="result/images", default="")

    def __str__(self):
        return self.studentname


class Blog(models.Model):
    blogs_id = models.AutoField
    BlogTitle = models.CharField(max_length=80, default="")
    Studentname = models.CharField(max_length=50, default="")
    aboutstudent = models.CharField(max_length=500, default="")
    Date = models.CharField(max_length=20, default="")
    Content = models.TextField()
    image = models.ImageField(upload_to="blogs/blog/images", default="")
    studentimage = models.ImageField(
        upload_to="blogs/student/images", default="")

    def __str__(self):
        return self.BlogTitle


class Gallery(models.Model):
    gallery_id = models.AutoField
    Event_name = models.CharField(max_length=80, default="")
    Event_id = models.CharField(max_length=80, default="")
    image = models.ImageField(upload_to="gallery")

    def __str__(self):
        return self.Event_name


class Card(models.Model):
    card = models.FileField(upload_to="Membership/Card/")
    font = models.FileField(upload_to="Membership/Font/")


class Membership(models.Model):
    member_id = models.AutoField
    name = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150, default="")
    session = models.CharField(max_length=150, default="")
    department = models.CharField(max_length=120, default="")
    contact = models.CharField(max_length=20, default="")
    transaction_id = models.CharField(max_length=30, default="")
    transaction_receipt = models.FileField(upload_to="Membership/Receipt/")
    image = models.FileField(upload_to="Membership/Images/")
    is_verified = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.id:
            self.image = self.compressImage(self.image)
            self.transaction_receipt = self.compressImage(self.transaction_receipt)
        super(Membership, self).save(*args, **kwargs)
    def compressImage(self,image):
        imageTemproary = Image.open(image)
        outputIoStream = BytesIO()
        imageTemproary = imageTemproary.convert('RGB')
        # imageTemproaryResized = imageTemproary.resize( (1020,573) ) 
        imageTemproary.save(outputIoStream , format='JPEG', quality=30)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return image


class ArtCraft(models.Model):
    participant_id = models.AutoField
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=250, default="")
    department = models.CharField(max_length=100, default="")
    year = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    image = models.FileField(upload_to="Creativarty/")
    date = models.DateField()

    def __str__(self):
        return self.name


class quizomania(models.Model):
    participant_id1 = models.AutoField
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name


class Git(models.Model):
    participant_id1 = models.AutoField
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    git = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

class ChooseATechField(models.Model):
    participant_id1 = models.AutoField
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

class gswcpM(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Getting Started with Competitive Coding"

class gswcw(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Getting Started with Technical Content Writing"

class robonixIntro(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Robonix Bootcamp Registration Form"

class appDevelopment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    prior = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Introduction to App Development"

class webDevelopment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    prior = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Introduction to Web Development"

class pythonDevelopment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    prior = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Introduction to Python and Django"

class backendDevelopment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    department = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=100, default="")
    college = models.CharField(max_length=100, default="")
    session = models.CharField(max_length=100, default="")
    prior = models.CharField(max_length=100, default="")
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Getting Started with Backend Development"
