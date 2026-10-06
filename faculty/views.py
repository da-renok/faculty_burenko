from django.shortcuts import render, get_object_or_404
from .models import HomePage, Department, Program, ExchangeProgram


def home(request):
    return render(request, 'faculty/home.html', {'info': HomePage.objects.first()})


def program_list(request):
    programs = Program.objects.select_related('department')
    return render(request, 'faculty/program_list.html', {'programs': programs})


def program_detail(request, id):
    program = get_object_or_404(Program, id=id)
    return render(request, 'faculty/program_detail.html', {'program': program})


def department_list(request):
    departments = Department.objects.prefetch_related('programs')
    return render(request, 'faculty/department_list.html', {'departments': departments})


def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    return render(request, 'faculty/department_detail.html', {'department': department})


def exchange_list(request):
    programs = ExchangeProgram.objects.order_by('deadline')
    country = request.GET.get('country')
    if country:
        programs = programs.filter(country=country)
    countries = (ExchangeProgram.objects.order_by('country')
                 .values_list('country', flat=True).distinct())
    return render(request, 'faculty/exchange_list.html',
                  {'programs': programs, 'countries': countries, 'current': country})