from django.http import HttpResponse
from django.template import loader
from .models import User

def users(request):
  allUsers = User.objects.all().values()
  template = loader.get_template('landing-page.html')
  context = {
    'allUsers': allUsers,
  }
  print('++++++++', allUsers)
  return HttpResponse(template.render(context, request))

def addUser(request):
  allUsers = User.objects.all().values()
  template = loader.get_template('landing-page.html')
  context = {
    'allUsers': allUsers,
  }
  return HttpResponse(template.render(context, request))