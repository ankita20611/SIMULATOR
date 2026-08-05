from django.shortcuts import render
from accounts.forms import SignupForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def signup_view(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully.")
            return redirect('admin:index')  # Redirect to the admin index page after successful signup
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})
    