from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_data={
  "jan":"This Works for january!",
  "feb":"This Works for february!",
  "march":None,
}

# Create your views here.

# def january(request):
#   return HttpResponse("This Works for january!")

# def feb(request):
#   return HttpResponse("This Work for february!")

def index(request):
   
   months=list(monthly_data.keys())
   
   return render(request,"challenges/index.html",{
      "months":months
   })

def challenges_check_by_number(request,month):
  months=list(monthly_data.keys())

  if month>len(months):
      return HttpResponseNotFound("Invalid Month!")
    
  redirect_data=months[month-1]
  redirect_path=reverse("check",args=[redirect_data])
  return HttpResponseRedirect(redirect_path)

# def challenges_check(reques,month):
#   text=None
#   if month=="jan":
#     text="This Works for january!"
#   elif month=="feb":
#     text="This Works for february!"
#   else:
#     return HttpResponseNotFound("This month not found!")
#   return HttpResponse(text)

def challenges_check(request,month):
    try:
        text=monthly_data[month] 
           
        return render(request,"challenges/challenge.html",{
           "text":text,
           "month_name":month
        })
    except:
      #  respose_data=render_to_string("404.html")
      #  return HttpResponseNotFound(respose_data)
      raise Http404()

