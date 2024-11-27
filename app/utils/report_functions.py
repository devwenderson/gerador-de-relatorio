# OK/
def calcular_media_geracao(fatura):
    data = dict()
    fatura = float(fatura)
    media_mensal = fatura*0.95
    media_anual = media_mensal * 12

    data['media_mensal'] = media_mensal
    data['media_anual'] = media_anual
    return data

# OK
def calcular_quantidade_de_paineis(media_mensal):
    qtd_paineis = media_mensal/((30*0.72*4.98*560)/1000)
    return round(qtd_paineis)

# OK
def calcular_economia_potencial(fatura):
    data = dict()
    fatura = float(fatura)
    reais_mensais = fatura
    reais_anuais = reais_mensais * 12

    data['reais_mensais'] = reais_mensais
    data['reais_anuais'] = reais_anuais

    return data

def calcular_tempo_de_retorno(valor_projeto, reais_mensais):
    tempo_retorno = valor_projeto/reais_mensais
    return round(tempo_retorno)

def calcular_valor_do_projeto(qtd_paineis):
    valor_projeto = 0
    if (0 < qtd_paineis <= 5):
        valor_projeto = qtd_paineis * 4000

    elif (5 < qtd_paineis <= 10):
        valor_projeto = qtd_paineis * 3500

    elif (10 < qtd_paineis <= 30):
        valor_projeto = qtd_paineis * 3000
        
    elif (30 < qtd_paineis <= 40):
        valor_projeto = qtd_paineis * 2500

    elif (40 < qtd_paineis <= 50):
        valor_projeto = qtd_paineis * 2000
    
    return valor_projeto

def calcular_potencia_gerador(qtd_paineis):
    potencia_gerador = (560*qtd_paineis)/1000

    return potencia_gerador


