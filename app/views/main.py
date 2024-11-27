from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from app.utils.report_functions import (
    calcular_economia_potencial,
    calcular_media_geracao,
    calcular_quantidade_de_paineis,
    calcular_tempo_de_retorno,
    calcular_valor_do_projeto,
    calcular_potencia_gerador,
)
from app.utils.functions import render_to_pdf, send_email_with_attachment
from babel.numbers import format_currency
from datetime import date
from django.conf import settings

def index(request):
    template_name = "index.html"
    return render(request, template_name)

def get_report(request):
    if request.method == "POST":
        data = dict()

        # Dados da request
        nome = request.POST["nome"]
        fatura = request.POST["fatura"].replace(".", "").replace(",", ".")
        recipient = request.POST["recipient"]

        # Calcula a média da geração mensal e anual
        media_mensal = calcular_media_geracao(fatura)["media_mensal"]
        media_anual = calcular_media_geracao(fatura)["media_anual"]

        # Quantidade de painéis
        qtd_paineis = calcular_quantidade_de_paineis(media_mensal)

        # Economia potencial
        reais_mensais = calcular_economia_potencial(fatura)["reais_mensais"]
        reais_anuais = calcular_economia_potencial(fatura)["reais_anuais"]

        # Valor do projeto
        valor_projeto = calcular_valor_do_projeto(qtd_paineis)

        # Calcular tempo de retorno
        tempo_retorno = calcular_tempo_de_retorno(valor_projeto, reais_mensais)

        # Calcular potência do gerador
        potencia_gerador = calcular_potencia_gerador(qtd_paineis)

        data["nome"] = nome
        data["media_mensal"] = f"{media_mensal:_.2f}".replace(".", ",").replace("_", ".")
        data["media_anual"] = f"{media_anual:_.2f}".replace(".", ",").replace("_", ".")
        data["qtd_paineis"] = qtd_paineis
        data["reais_mensais"] = format_currency(reais_mensais, "BRL", locale="pt_BR")
        data["reais_anuais"] = format_currency(reais_anuais, "BRL", locale="pt_BR")
        data["valor_projeto"] = format_currency(valor_projeto, "BRL", locale="pt_BR")
        data["tempo_retorno"] = tempo_retorno
        data["potencia_gerador"] = f"{potencia_gerador:_.2f}".replace(".", ",").replace("_", ".")
        data["data_hoje"] = date.today()
        data["STATIC_URL"] = request.build_absolute_uri(settings.STATIC_URL)

        pdf = render_to_pdf("pdf/report.html", data)
        response = HttpResponse(pdf, content_type="application/pdf")

        # subject = "Seu orçamento"
        # message = f"Olá, {nome}! Seu orçamento está logo abaixo!"
        # recipient_list = [recipient]
        # send_email_with_attachment(subject, message, recipient_list, response)

        messages.success(request, "Seu orçamento foi enviado no seu email")
        # return redirect('get-report')
        return response

    template_name = "report_form.html"

    return render(request, template_name)

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
