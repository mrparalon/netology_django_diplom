from django.shortcuts import render, HttpResponse


def show_user_profile(request):
    if request.user.is_authenticated:
        user = request.user
    print(user)
    return HttpResponse(f'{user}')