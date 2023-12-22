from django.contrib.auth.models import User
from django.views.generic import CreateView
from api.models import Question
from ..forms import UserForm, ProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView
from ..forms import UserRegisterForm, UserPasswordResetForm
from django.contrib.auth.decorators import login_required
from ..models import Profile, SolverProfile


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        Profile.objects.create(user=user)
        SolverProfile.objects.create(user=user)
        # current_site = get_current_site(self.request)
        # mail_subject = 'Activate your account.'
        # message = render_to_string('custom_regloginapp/activation_email.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'token': user.email_token,
        # })
        # to_email = form.cleaned_data.get('email')
        # email = EmailMessage("Hi", "hi welcome to ACSL Guide", to=[to_email])
        # email.send()
        # send_mail(
        #     'Welcome to our site',
        #     'Hello, thank you for registering on our site.',
        #     settings.EMAIL_HOST_USER,
        #     [user.email],
        #     fail_silently=False,
        # )
        return redirect('homepage')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('homepage')


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = UserPasswordResetForm
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return redirect('homepage')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirect to some success page, for example, back to the profile page.
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'pages/user/edit_profile.html', context)


@login_required
def view_profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'pages/user/profile.html', {'profile': user_profile, 'user': request.user})


def view_user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'pages/user/profile.html', {'profile': profile, 'user': user})

def solver_profile(request):
    user = request.user
    solver_profile = SolverProfile.objects.get(user=user)
    return render(request, 'pages/user/solver_profile.html', {'solver_profile': solver_profile, 'user': user})


def view_user_solver_profile(request, username):
    user = User.objects.get(username=username)
    solver_profile = SolverProfile.objects.get(user=user)
    return render(request, 'pages/user/solver_profile.html', {'solver_profile': solver_profile, 'user': user})
