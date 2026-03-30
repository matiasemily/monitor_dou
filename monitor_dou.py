import requests
import smtplib
import os
import urllib.parse
from email.mime.text import MIMEText

# Variáveis do GitHub Secrets
NOME_BUSCA = os.environ.get('NOME_BUSCA')
EMAIL_DESTINO = os.environ.get('EMAIL_DESTINO')
EMAIL_USER = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

# Função para query da URL dinâmica
def gerar_url(nome):
    # Adiciona aspas para realizar busca exata
    query_aspirada = f'"{nome}"'
    params = {
        'q': query_aspirada,
        's': 'todos',
        'exactDate': 'all',
        'sortType': '0'
    }
    base_url = "https://www.in.gov.br/consulta/-/buscar/dou"
    return f"{base_url}?{urllib.parse.urlencode(params)}"

# Função de notificação por e-mail
def enviar_email(url_encontrada):
    corpo = f"Meu nome '{NOME_BUSCA}' foi finalmente localizado no Diário Oficial!!\nÓ aqui: {url_encontrada}"
    msg = MIMEText(corpo)
    msg['Subject'] = f'CATAPIMBAS: {NOME_BUSCA} tá no DOU'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_DESTINO

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

# Função que faz a busca do nome completo no DOU
def check_dou():
    url = gerar_url(NOME_BUSCA)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            # Se não tiver "0 resultados para", o nome foi encontrado e envia e-mail
            if "0 resultados para" not in response.text:
                print(f"Finalmente achamos {NOME_BUSCA}!!!")
                enviar_email(url)
            else:
                print(f"O nome '{NOME_BUSCA}' ainda não consta no DOU ( ;^;)")
        else:
            print(f"Erro no portal do DOU: Status {response.status_code}")
    except Exception as e:
        print(f"Erro na execução: {e}")

# Fallback para erros de variável de ambiente
if __name__ == "__main__":
    if all([NOME_BUSCA, EMAIL_USER, EMAIL_PASS, EMAIL_DESTINO]):
        check_dou()
    else:
        print("Verifique se as variáveis de ambiente estão configuradas corretamente.")