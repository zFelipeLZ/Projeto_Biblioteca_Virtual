from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Locacao, Livro

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['nome', 'cpf', 'livro', 'data_devolucao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # MOSTRA APENAS LIVROS DISPONÍVEIS
        self.fields['livro'].queryset = Livro.objects.filter(status='D')

    def clean(self):
        cleaned_data = super().clean()
        data_devolucao = cleaned_data.get('data_devolucao')

        if data_devolucao:
            hoje = timezone.now().date()
            limite = hoje + timedelta(days=7)

            # NÃO PODE SER ANTES DE HOJE
            if data_devolucao < hoje:
                self.add_error(
                    'data_devolucao',
                    'A data de devolução não pode ser anterior à data atual.'
                )

            # NÃO PODE PASSAR DE 7 DIAS
            if data_devolucao > limite:
                self.add_error(
                    'data_devolucao',
                    'A data de devolução não pode ultrapassar 7 dias.'
                )

        return cleaned_data

    
class FiltroLivroForm(forms.Form):
    area = forms.CharField(required=False)
    autor = forms.CharField(required=False)