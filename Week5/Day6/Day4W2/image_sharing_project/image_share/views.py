from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Image
from .forms import ProfileForm, ImageForm
from pathlib import Path
# Create your views here.


class ProfileView(DetailView):
    model = Profile
    template_name = 'registration/profile.html'
    context_object_name = 'profile'



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def index_view(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'image_share/home.html', context)


def profile_redirect_view(request):

    user = request.user
    if hasattr(user, 'profile'):
        return redirect('update-profile')



def update_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        filled_form = ProfileForm(request.POST, instance=profile)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('home')
        else:
            errors = filled_form.errors
            print(errors)        

    form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'registration/update-profile.html', context)



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            image.user_upload = profile
            image.save()
            return redirect('home')
    else:
        form = ImageForm()
        context = {'form': form}
    return render(request, 'image_share/upload_image.html', context)



def images_view(request):
    images = Image.objects.all()
    url = Path(__file__).resolve().parent.parent
    context = {'images': images, 'url': url}
    return render(request, 'image_share/view_images.html', context)


def user_images(request):
    profile = Profile.objects.get(user=request.user)
    user_images = Image.objects.filter(user_upload=profile)
    context = {'user_images': user_images, 'profile': profile}
    return render(request, 'image_share/user_images.html', context)
