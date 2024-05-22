from django.http import HttpResponse
from django.template import loader
from .models import User
from datetime import datetime
from django.contrib import messages
from .addUser import UserForm
from django.shortcuts import redirect

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

# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             # Process the valid data here (save to database)
#             return redirect('user_list')  # Redirect to the user list page
#     else:
#         form = UserForm()

#     return render(request, 'add_user.html', {'form': form})