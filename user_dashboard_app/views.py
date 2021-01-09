from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home_page.html')

def sign_in_page(request):
    return render(request, 'sign_in_page.html')

def register_page(request):
    return render(request, 'register_page.html')

def user_info_page(request):
    return render(request, 'user_info.html')

def user_dashboard_page(request):
    return render(request, 'user_dashboard.html')

def edit_profile_page(request):
    return render(request, 'edit_profile_page.html')

def admin_dashboard_page(request):
    return render(request, 'admin_dashboard_page.html')