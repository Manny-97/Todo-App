from django.shortcuts import render

def handle_not_found(request, exception):
    return render(request, 'not-found.html')

def hamdle_server_error(request, exception):
    return render(request, 'server-error.html')