from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from django.contrib import messages
from .models import AboutMe, Education, Skill, Project, SocialMedia, Interest
from recruiters.forms import RecruiterContactForm


class HomeListView(ListView):

    queryset = AboutMe.objects.all()
    template_name = 'credentials/index.html'

    def get_context_data(self, request, *args, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['education'] = Education.objects.all()
        context['skills'] = Skill.objects.order_by('-skill', '-percentage')
        context['project'] = Project.objects.all()
        context['socials'] = SocialMedia.objects.all()
        if request.method == 'POST':
            context['form'] = RecruiterContactForm(request.POST)
            if context['form'].is_valid():
                contact = context['form'].save()
                contact.save()
                messages.success(request, 'Your contact information has been successfully received!')
                return redirect('home')
        else:
            context['form'] = RecruiterContactForm()
        return context


def home(request):
    object_list = AboutMe.objects.all()
    # contact form for the page
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
        project = Project.objects.all()
        socials = SocialMedia.objects.all()
        description = AboutMe.objects.first()
        interest = Interest.objects.all()

        # returns context in the database for the portfolio
        context = {'education': education, 'form': form, 'skills': skills,
                   'project': project, 'socials': socials, 'interest':interest,
                   'object_list': object_list, 'description': description}
        return render(request, 'credentials/index.html', context)


class UnderConstruction(TemplateView):

    template_name = 'credentials/construction.html'

