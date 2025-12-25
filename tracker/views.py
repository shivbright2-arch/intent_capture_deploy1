from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#def members(request):
 #   return HttpResponse("Hello world!, This is for Google capture")

#def members(request):
 #   template = loader.get_template('printed_vest.html')
  #  return HttpResponse(template.render())


import uuid
from django.shortcuts import render
from .models import IntentVisitor
from django.http import JsonResponse


def printed_vest(request):
  session_id = request.COOKIES.get('intent_id', str(uuid.uuid4()))

  keyword = request.GET.get('utm_term', 'printed vest for men')
  source = request.GET.get('utm_source', 'google')

  intent_level = 'HIGH' if 'flipkart' in keyword.lower() else 'MEDIUM'

  IntentVisitor.objects.create(
  session_id=session_id,
  keyword=keyword,
  source=source,
  page_url=request.path,
  ip_address=request.META.get('REMOTE_ADDR'),
  user_agent=request.META.get('HTTP_USER_AGENT'),
  intent_level=intent_level
  )

  response = render(request, 'printed_vest.html')
  response.set_cookie('intent_id', session_id, max_age=60*60*24*30)
  return response




def track_flipkart_click(request):
  session_id = request.COOKIES.get('intent_id')
  if session_id:
    IntentVisitor.objects.filter(session_id=session_id).update(
    flipkart_clicked=True,
    intent_level='HIGH'
    )
  return JsonResponse({'status': 'ok'})