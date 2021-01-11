from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check already made inquery
        if request.user.is_authenticated:
            user_id = request.user.id
            has_inquery = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)

            if has_inquery:
                messages.error(request,"You have already made an inquery for this listing !")
                return redirect('/listing/'+listing_id)

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        #EMAIL send
        send_mail(
            'Property Listing Inquery',
            'There has been an inquery for '+listing+'. Sign into admin panel for more info.',
            'dansakib@gmail.com',
            [realtor_email,'tanvirmahin24@gmail.com'],
            fail_silently=False
        )

        messages.success(request, "Your request is submitted, a realtor will get back to you soon !")

        return redirect('/listing/'+listing_id)
