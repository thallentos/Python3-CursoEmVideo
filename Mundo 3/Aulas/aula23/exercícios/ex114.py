# O site pudim é bugado
import urllib.request

url = "https://www.google.com.br/"

try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except:
    print(f'O site {url} está indisponível no momento')
else:
    print(f'Consegui acessar o site {url} com sucesso')
# referente à aula 23