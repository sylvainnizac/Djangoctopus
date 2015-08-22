from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

def my_custom_page_not_found_view(request):
    response = render_to_response('errors/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def my_custom_error_view(request):
    response = render_to_response('errors/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def my_custom_permission_denied_view(request):
     return render(request,'errors/403.html')

#def my_custom_bad_request_view(request):
 #    return render(request,'errors/400.html')

def CV(request):
     return render(request,'st_pages/CV.html')