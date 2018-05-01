import os
import modelo

def generate_certificate(nome, curso, evento, local, data, carga, autenticacao):
    text = modelo.assemble_text(nome, curso, evento, local, data, carga, autenticacao)
    document = modelo.assemble_document(text)

    nomeSemEspacos = ''.join(nome.split())
    cursoSemEspacos = ''.join(curso.split())

    fileName = f'{nomeSemEspacos}{cursoSemEspacos}'

    with open(f'{fileName}.tex', 'w', encoding='utf-8') as f:
        f.write(document)

    # os.system(f'DEL /Q certificados\\{fileName}.*')
    os.system(f'pdflatex {fileName}.tex')
    os.system(f'pdflatex {fileName}.tex')
    os.system(f'MOVE {fileName}.pdf certificados\\PDFs')
    os.system(f'MOVE {fileName}.* certificados')
    # os.system(f'MOVE certificados\\{fileName}.pdf certificados\\PDFs')
    # os.system(f'DEL /Q certificados\\*')

if __name__ == '__main__':
    nome = 'John Cena'
    curso = 'Worshop Python Básico'
    evento = 'Civcom Workshop Week'
    local = 'no Laboratório Central de Computação Científica da Faculdade de Tecnologia da Universidade de Brasília'
    data = '07 de maio de 2018'
    carga = '02 horas e 30 minutos'
    autenticacao = 'CCWW201805-BF15D46A'
    generate_certificate(nome, curso, evento, local, data, carga, autenticacao)