from django.shortcuts import render, redirect


def landing_view(request):
    request.session.flush()
    return render(request, "layouts/layouts-1.html")