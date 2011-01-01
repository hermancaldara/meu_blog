from django import forms
from django.core.mail import send_mail


class ContatoForm(forms.Form):

    nome = forms.CharField(max_length=100)
    email = forms.CharField(max_length=150)
    menssagem = forms.Field(widget=forms.Textarea)
    
    def enviar(self):
        titulo = 'Mensagem de contato pelo site'
        destino = 'hermancaldara@gmail.com'
        texto = """
            Nome: %(nome)s
            E-mail: %(email)s
            Mensagem:
            %(menssagem)s
        """ % self.cleaned_data
        
        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
        )
