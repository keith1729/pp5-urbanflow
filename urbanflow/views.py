from django.shortcuts import render


def custom404(request, exception):
    """ 404 Error Handler """
    
    return render(request, "errors/404.html", status=404)
