from django.shortcuts import render
from exit_ticket.models import views

# Create your views here.

def render_index(request):
    return render(request, 'index.html', {})

def render_exit_ticket_enviado(request):
   exit_ticket_dados = {
        'nome': request.POST.get('nome'),
        'feedback': request.POST.get('feedback'),
        'ocupacao': request.POST.get('ocupacao'),
        'data': request.POST.get('dtcurso'),
        'nota': request.POST.get('nota'),
        'duvidas': request.POST.get('tecnologia')
    }
    exit_ticket = ExitTicket(**exit_ticket_dados)
    exit_ticket.save()

    return render(request, 'exit_ticket_enviado.html',  {'nome': exit_ticket.nome, 'email': exit_ticket.email, 'data': exit_ticket.data})
