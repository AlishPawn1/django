from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # print("Request :",request)
    return render(request, "index.html", 
                  context={
                    #   "name":"Alish Pawn",
                    #   "names": ["rem", "ram", "Shyam"],
                    "list": [1,2,3],
                      "information": [
                          {"name": "ram", "rank":1, "first": True, "grade": 85.025},
                          {"name": "shyam", "rank":2, "first": False, "grade": 65.025},
                          {"name": "hari", "rank":3, "first": False, "grade": 55.025},
                      ],
                      "show": True,
                      "sorted": True,
                  },
                  )
    
def calculation_view(request):
    print("request method: ", request.method)
    if request.method == 'GET':
      return render(request, "calc.html")
    else:
      print("form datas: ", request.POST)
      result = int(request.POST.get('num1')) + int(request.POST.get('num2'))
      return render(request, "calc.html", context={"result": result})

from home.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact_view(request):
  if request.method == 'GET':
    form = ContactForm()
    return render(request, "contact.html", {"form": form})
  else:
    form = ContactForm(data = request.POST)
    if form.is_valid():
      send_mail(
        from_email = settings.DEFAULT_FROM_EMAIL,
        subject="Contact Email from Application",
        message= form.cleaned_data.get('message'),
        recipient_list=[form.cleaned_data.get('email')],
        fail_silently=False
      )
      return render(request, "contact.html", {'form': form, 'message': 'sent'})
    return render(request, "contact.html", {'form': form})
    
