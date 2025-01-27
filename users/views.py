from django.shortcuts import render, HttpResponse, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from posts.models import Post
from django.contrib import messages



# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                if not user.profile.is_profile_completed:
                    return redirect('edit')
                return redirect('feed')
            else:
                form.add_error(None, 'Invalid username or password')
                messages.error(request, 'Invalid login credentials')
                return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def index(request):
    current_user = request.user
    posts = Post.objects.filter(user=current_user)
    try:
        profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'users/index.html', {'posts': posts, 'profile': profile})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            # Save the new user without committing to the database yet
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # Check if the user already has a profile before creating
            profile, created = Profile.objects.get_or_create(user=new_user)

            login(request, new_user)

            return redirect('edit')

            #return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'users/register.html', {'user_form': user_form})


@login_required
def edit(request):
    # Ensure the user has an associated Profile object
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.is_profile_completed = True
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('feed')  # Redirect to avoid resubmission
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/edit.html', {'user_form': user_form, 'profile_form': profile_form})



from django.http import HttpResponse

# def test_login(request):
#     return render(request, "socialaccount/login.html")