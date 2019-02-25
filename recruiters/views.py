from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Recruiter
from .forms import RecruiterContactForm

# Create your views here.


def home(request):

    if request.method == 'POST':
        form = RecruiterContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact.save()
            messages.success(request, 'Your contact information has been successfully received!')
            return redirect('home')
    else:
        form = RecruiterContactForm()
        education = Education.objects.all()
        skills = Skill.objects.order_by('-skill', '-percentage')
        project= Project.objects.all()
        socials= SocialMedia.objects.all()

        context = {'education': education, 'form':form, 'skills': skills,
                   'project': project, 'socials': socials}
        return render(request, 'recruiters/contact-form.html', context)

