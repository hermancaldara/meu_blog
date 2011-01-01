from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import ContatoForm


def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar()
            contato_realizado = 'Contato enviado!'
    else:
        form = ContatoForm()
        
    return render_to_response(
        'contato.html',
        locals(),
        context_instance=RequestContext(request)
    )
            
