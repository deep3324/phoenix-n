from django.core.mail.message import EmailMessage
from PhOeNiX.settings import MEDIA_ROOT
from smtplib import SMTPException
from PIL import Image, ImageFont, ImageDraw


def def_mail(subject, html, receiver_email, name=None):
    subject, from_email, to = subject, 'no-reply@phoenixnsec.in', receiver_email
    msg = EmailMessage(subject, html, from_email, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    if name:
        msg.attach_file(MEDIA_ROOT + "\\converted\\" +str(name).replace(" ","_") + ".png")
    try:
        msg.send()
        status = "Success"
    except SMTPException:
        status = "Failed"
    return {"status": status}


def membership_card_creation(member, card):
        my_image = Image.open(card.card)
        title_font = ImageFont.truetype("arial.ttf", 35)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((630, 312), "PH-21"+str("%03d" % member.id), (0, 0, 0), font=title_font)
        image_editable.text((630, 370), member.name.title(), (0, 0, 0), font=title_font)
        image_editable.text((630, 426), (member.session).replace(" ", ""), (0, 0, 0), font=title_font)
        image_editable.text((630, 484), filter_department(member.department), (0, 0, 0), font=title_font)
        my_image.paste((Image.open(member.image.path)).resize(
            (220, 280), Image.ANTIALIAS), (58, 200))
        my_image.save(MEDIA_ROOT + "\\converted\\" +str(member.name.title()).replace(" ","_") + ".png")


def filter_department(department):
    lower_dept = department.lower()
    data = lower_dept.split(" ")
    if "artificial" in data:
        return "AIML"
    elif "computer" and "systems" in data:
        return "CSBS"
    elif "computer" and "engineering" in data:
        return "CSE"
    elif "information" in data:
        return "IT"
    elif "civil" in data:
        return "CE"
    elif "mechanical" in data:
        return "ME"
    elif "applied" in data:
        return "AEIE"
    elif "communication" in data:
        return "ECE"
    elif "electrical" in data:
        return "EE"
    elif "bio-medical" in data:
        return "BME"
    elif "bio" in data:
        return "BME"
    return department
