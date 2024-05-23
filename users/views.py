from django.http import HttpResponse
from django.template import loader
from .models import User
from datetime import datetime
from django.contrib import messages
from .addUser import UserForm
from django.shortcuts import redirect, get_object_or_404

def change_date(date_str):
    """
    Formats a date string in the format "YYYY-MM-DD" to "Month DD, YYYY".
    
    Args:
        date_str (str): A date string in the format "YYYY-MM-DD".
    
    Returns:
        str: The formatted date string in the format "Month DD, YYYY".
    """
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%B %d, %Y")


def users(request):
  allUsers = User.objects.all().values().order_by('-id')
  template = loader.get_template('landing-page.html')
  context = {
    'allUsers': allUsers,
  }
  return HttpResponse(template.render(context, request))

def addUser(request):
    if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        phone = request.POST['phone']
        joined_date = request.POST['joined_date']

        User.objects.create(firstname=firstname, lastname=lastname, phone=phone, joined_date=joined_date)
        messages.success(request, "User created successfully.")
        return redirect('addUser')
    else:
      form = UserForm()

    template = loader.get_template('add-user.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def addUser(request):
    if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        phone = request.POST['phone']
        joined_date = request.POST['joined_date']

        User.objects.create(firstname=firstname, lastname=lastname, phone=phone, joined_date=joined_date)
        messages.success(request, "User created successfully.")
        return redirect('addUser')
    else:
      form = UserForm()
      
    template = loader.get_template('add-user.html')
    context = {
       'form': form,
       'user_url': "/users/add/"
      }
    return HttpResponse(template.render(context, request))

def editUser(request, user_id=None):
    user = None
    form = UserForm()
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            form = UserForm(instance=user)
        except User.DoesNotExist:
            messages.error(request, "The user you are trying to edit does not exist.")

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            joined_date = form.cleaned_data['joined_date']

            if user:
                # Update existing user
                user.firstname = firstname
                user.lastname = lastname
                user.phone = phone
                user.joined_date = joined_date
                user.save()
                messages.success(request, 'User updated successfully.')
    
    template = loader.get_template('add-user.html')
    context = {
       'form': form,
       'is_edit_mode': user_id is not None,
       'user_url': f"/users/edit/{user_id}/"
    }
    return HttpResponse(template.render(context, request))