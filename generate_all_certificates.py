from certificate_generator import generate_certificate
from configs import *

with open(validacoesFile, 'r') as f:
    for line in f:
        l = line.strip()
        l = l.split(', ')
        nome, autenticacao = l[0], l[1]
        generate_certificate(nome, curso, evento, local, data, carga, autenticacao)