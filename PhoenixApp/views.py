import time
from django.http.response import HttpResponse
from PhoenixApp import def_mail, membership_card_creation
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect
from PhoenixApp.models import Card, Git, Membership, Review, Contact, PreviousEvent, UpComingEvent, Result, Blog, Gallery, ChooseATechField, backendDevelopment, gswcpM, gswcw, pythonDevelopment, robonixIntro,appDevelopment, webDevelopment
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import *
# Create your views here.


def index(request):
    return render(request, 'index.html')

def git_mail(request):
    emails = Git.objects.all()
    subject = render_to_string('email/git_mail.html')
    for email in emails:
        def_mail("GIT Session | PHOENIX", subject, email.email)
        time.sleep(5)
    return HttpResponse("pass")


def create_card(request):
    members = Membership.objects.all()
    cards = Card.objects.all()[0]
    for member in members:
        # time.sleep(7)
        if member.is_verified and member.is_sent == False:
            membership_card_creation(member, cards)
            print(member)
            subject = render_to_string('email/membership.html', {'name': member.name.title()})
            mes = def_mail("Membership Card | PHOENIX", subject, member.email,  member.name.title())
            print(member)
            if mes["status"] == "Success":
                member.is_sent = True
                member.save()
    return HttpResponse("pass")


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def home(request):
    context = {"home_page": "active"}
    return render(request, 'home.html', context)


def clubs(request):
    context = {"clubs_page": "active"}
    return render(request, 'club.html', context)


def events(request):
    prevevents = PreviousEvent.objects.all()
    upevn = UpComingEvent.objects.all()
    context = {
        "events_page": "active",
        'product': prevevents,
        'upcomingevents': upevn,
    }
    return render(request, 'events.html', context)


def result(request, slug):
    results = Result.objects.filter(slug=slug)
    return render(request, 'result.html', {"results": results})


def blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs_page": "active",
        "blog": blogs,
    }
    return render(request, 'blogs.html', context)


def blog(request, myid):
    blog = Blog.objects.filter(id=myid)
    contents = Blog.objects.all()
    return render(request, "blog.html", {'blog': blog, "contents": contents})


def gallery(request):
    gallery = Gallery.objects.all()
    context = {"gallery_page": "active", "contents": gallery}
    return render(request, "gallery.html", context)


def webteam(request):
    context = {"webteam_page": "active"}
    return render(request, 'webteam.html', context)


def core2020_21(request):
    context = {"core_page": "active"}
    return render(request, 'core2020-21.html', context)


def contact(request):
    context = {"contact_page": "active"}
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        subject = render_to_string('email/contactus.html', {'name': name})
        contact = Contact(name=name, year=year, email=email,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(
            request, "Your Contact Request has been Submitted. We'll Contact you soon.")
        def_mail("Contact Request | PHOENIX", subject, email)
    return render(request, 'contact.html', context)


def avenir(request):
    context = {"events_page": "active"}
    return render(request, 'avenir.html', context)


def brainstormer(request):
    context = {"events_page": "active"}
    return render(request, 'brainstormer.html', context)


def aavahan(request):
    context = {"events_page": "active"}
    return render(request, 'aavahan.html', context)


def cybernix(request):
    context = {"clubs_page": "active"}
    return render(request, 'cybernix.html', context)


def eloquense(request):
    context = {"clubs_page": "active"}
    return render(request, 'eloquense.html', context)


def robonix(request):
    context = {"clubs_page": "active"}
    return render(request, 'robonix.html', context)


def lensified(request):
    context = {"clubs_page": "active"}
    return render(request, 'lensified.html', context)


def nirmaan(request):
    context = {"clubs_page": "active"}
    return render(request, 'nirmaan.html', context)


def review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        subject = 'We got the following review about Phoenix : \n' + review
        review = Review(review=review, date=datetime.today())
        review.save()
        messages.success(
            request, "Your Review has been submitted, We'll soon start work on your review")
        send_mail('Review form', subject, settings.EMAIL_HOST_USER,
                  ['core@phoenixnsec.in'])
    return redirect('/home')


def membership(request):
    if request.method == 'POST' and request.FILES:
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        session = request.POST.get('session')
        department = request.POST.get('department')
        transaction_id = request.POST.get('transaction_id')
        transaction_receipt = request.FILES['transaction_receipt']
        image = request.FILES['images']
        subject = render_to_string(
            'email/confirmation_member.html', {'name': name})
        member = Membership(name=name, session=session, email=email, department=department, contact=contact,
                            transaction_id=transaction_id, transaction_receipt=transaction_receipt, image=image, date=datetime.today())
        members = Membership.objects.all()
        for i in members:
            if member.email == i.email:
                messages.warning(
                    request, "Your Form has been Already Submitted.")
                return redirect('/membership')
        if ((image.name.split(".")[-1] not in ["jpeg", "jpg", "png", "gif"]) or (transaction_receipt.name.split(".")[-1] not in ["jpeg", "jpg", "png", "gif"])):
            messages.warning(
                request, "Please upload appropriate image format")
        else:
            member.save()
            messages.success(
                request, "Your One-time Membership Request has been Submitted. We'll Contact you soon.")
            def_mail("Membership | PHOENIX", subject, email)
    return render(request, 'membership.html')


def Creativarty(request):
    return render(request, 'artcraft.html')


def Quizomania(request):
    return render(request, 'events/quizomania.html')

def chooseATechField(request):
    return render(request, 'events/chooseATechField.html')


def git(request):
    return render(request, 'events/git.html')


def gswcp(request):
    return render(request, 'events/gswcp.html')

def gswcwv(request):
    return render(request, 'events/getting-started-with-content-writing.html')


# def confirmation(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         department = request.POST.get('department')
#         session = request.POST.get('session')
#         college = request.POST.get('college')
#         subject = render_to_string('email/confirmation.html', {'name': name})
#         abc = gswcw(name=name, email=email, contact=contact, department=department,
#                   college=college, session=session, date=datetime.today())
#         abcd = gswcw.objects.all()
#         for i in abcd:
#             if abc.email == i.email:
#                 messages.warning(
#                     request, "Your Form has been Already Submitted.")
#                 return redirect('/events/getting-started-with-content-writing')
#         else:
#             abc.save()
#         messages.success(
#             request, "Your Form Has Been Submitted. Be alert for further notice. Don't miss this amazing Opportunity.")
#         def_mail(
#             "Getting Started with Technical Content Writing | PHOENIX", subject, email)
#     return render(request, 'events/confirmation.html')
    
# def robonixintro(request):
#     return render(request, 'events/robonix-bootcamp-registration.html')


# def robonixintroconfirmation(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         department = request.POST.get('department')
#         session = request.POST.get('session')
#         college = request.POST.get('college')
#         subject = render_to_string('email/robonixconfirmation.html', {'name': name})
#         abc = robonixIntro(name=name, email=email, contact=contact, department=department,
#                   college=college, session=session, date=datetime.today())
#         abcd = robonixIntro.objects.all()
#         for i in abcd:
#             if abc.email == i.email:
#                 messages.warning(
#                     request, "Your Form has been Already Submitted.")
#                 return redirect('/events/robonix-bootcamp-registration')
#         else:
#             abc.save()
#         messages.success(
#             request, "Your Form Has Been Submitted. Be alert for further notice. Don't miss this amazing Opportunity.")
#         def_mail(
#             "Robonix Bootcamp Registration | PHOENIX", subject, email)
#     return render(request, 'events/robonix-bootcamp-registration-confirmation.html')

# def iad(request):
#     return render(request, 'events/introduction-to-app-development.html')


# def iadconfirmation(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         department = request.POST.get('department')
#         session = request.POST.get('session')
#         college = request.POST.get('college')
#         prior = request.POST.get('prior')
#         subject = render_to_string('email/confirmation.html', {'name': name})
#         abc = appDevelopment(name=name, email=email, contact=contact, department=department,
#                   college=college, prior=prior, session=session, date=datetime.today())
#         abcd = appDevelopment.objects.all()
#         for i in abcd:
#             if abc.email == i.email:
#                 messages.warning(
#                     request, "Your Form has been Already Submitted.")
#                 return redirect('/events/introduction-to-app-development')
#         else:
#             abc.save()
#         messages.success(
#             request, "Your Form Has Been Submitted. Be alert for further notice. Don't miss this amazing Opportunity.")
#         def_mail(
#             "Introduction to App Development | PHOENIX", subject, email)
#     return render(request, 'events/introduction-to-app-development-confirmation.html')

# def iwd(request):
#     return render(request, 'events/introduction-to-web-development.html')


# def iwdconfirmation(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         department = request.POST.get('department')
#         session = request.POST.get('session')
#         college = request.POST.get('college')
#         prior = request.POST.get('prior')
#         subject = render_to_string('email/confirmation.html', {'name': name})
#         abc = webDevelopment(name=name, email=email, contact=contact, department=department,
#                   college=college, prior=prior, session=session, date=datetime.today())
#         abcd = webDevelopment.objects.all()
#         for i in abcd:
#             if abc.email == i.email:
#                 messages.warning(
#                     request, "Your Form has been Already Submitted.")
#                 return redirect('/events/introduction-to-web-development')
#         else:
#             abc.save()
#         messages.success(
#             request, "Your Form Has Been Submitted. Be alert for further notice. Don't miss this amazing Opportunity.")
#         def_mail(
#             "Introduction to Web Development | PHOENIX", subject, email)
#     return render(request, 'events/introduction-to-web-development-confirmation.html')

# def ipd(request):
#     return render(request, 'events/introduction-to-python-and-django.html')


# def ipdconfirmation(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         department = request.POST.get('department')
#         session = request.POST.get('session')
#         college = request.POST.get('college')
#         prior = request.POST.get('prior')
#         subject = render_to_string('email/confirmation.html', {'name': name})
#         abc = pythonDevelopment(name=name, email=email, contact=contact, department=department,
#                   college=college, prior=prior, session=session, date=datetime.today())
#         abcd = pythonDevelopment.objects.all()
#         for i in abcd:
#             if abc.email == i.email:
#                 messages.warning(
#                     request, "Your Form has been Already Submitted.")
#                 return redirect('/events/introduction-to-python-and-django')
#         else:
#             abc.save()
#         messages.success(
#             request, "Your Form Has Been Submitted. Be alert for further notice. Don't miss this amazing Opportunity.")
#         def_mail(
#             "Introduction to Web Development | PHOENIX", subject, email)
#     return render(request, 'events/introduction-to-python-and-django-confirmation.html')


def gswbd(request):
    return render(request, 'events/getting-started-with-backend-development.html')


def gswbdconfirmation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        department = request.POST.get('department')
        session = request.POST.get('session')
        college = request.POST.get('college')
        prior = request.POST.get('prior')
        subject = render_to_string('email/confirmation.html', {'name': name})
        abc = backendDevelopment(name=name, email=email, contact=contact, department=department,
                  college=college, prior=prior, session=session, date=datetime.today())
        abcd = backendDevelopment.objects.all()
        for i in abcd:
            if abc.email == i.email:
                messages.warning(
                    request, "Your Form has been Already Submitted.")
                return redirect('/events/getting-started-with-backend-development')
        else:
            abc.save()
        messages.success(
            request, "Your Form Has Been Submitted. Be alert for further notice. Don't miss this amazing Opportunity.")
        def_mail(
            "Getting Started with Backend Development | PHOENIX", subject, email)
    return render(request, 'events/getting-started-with-backend-development-confirmation.html')
