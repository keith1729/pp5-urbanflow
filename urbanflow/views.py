from django.shortcuts import render


def custom404(request, exception):
    """ 404 Error Handler """
    
    return render(request, "errors/404.html", status=404)

def custom500(request):
    """ 500 Error Handler """

    return render(request, "errors/500.html", status=500)
