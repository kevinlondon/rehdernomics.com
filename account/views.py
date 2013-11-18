from django.shortcuts import render


def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {
        'user': user,
    })

