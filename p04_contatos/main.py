"""Projeto 04: agenda com filtro por nome e indice unico."""
import re
from pymongo.errors import DuplicateKeyError
from email_validator import validate_email, EmailNotValidError
from conexao import banco


def validar_email(email):
    try:
        return validate_email(email, check_deliverability=False).normalized.lower()
    except EmailNotValidError:
        print('E-mail inválido. Exemplo: nome@dominio.com')
        return None


contatos = banco['contatos_p04']
contatos.create_index('email', unique=True)

while True:
    print('\n[1] Adicionar [2] Buscar [3] Atualizar [4] Remover [0] Sair')
    op = input('Opção: ').strip()
    if op == '1':
        nome = input('Nome: ').strip()
        email = validar_email(input('E-mail: ').strip())
        if email is None: continue
        telefone = input('Telefone: ').strip()
        empresa = input('Empresa (opcional): ').strip()
        if not all([nome, email, telefone]): continue
        try:
            contatos.insert_one({'nome': nome, 'email': email,
                                 'telefone': telefone, 'empresa': empresa})
            print('Contato salvo!')
        except DuplicateKeyError:
            print('E-mail já utilizado.')
    elif op == '2':
        trecho = input('Parte do nome: ').strip()
        if not trecho:
            print('Informe um termo.'); continue
        busca = {'nome': {'$regex': re.escape(trecho), '$options': 'i'}}
        encontrados = list(contatos.find(busca, {'_id': 0}).sort('nome'))
        if not encontrados:
            print('Nenhum encontrado.')
        else:
            for item in encontrados:
                print(item)
    elif op == '3':
        email = validar_email(input('E-mail do contato: ').strip())
        if email is None: continue
        telefone = input('Novo telefone: ').strip()
        if telefone:
            r = contatos.update_one({'email': email}, {'$set': {'telefone': telefone}})
            print('Atualizado!' if r.matched_count else 'Contato não encontrado.')
    elif op == '4':
        email = validar_email(input('E-mail: ').strip())
        if email is None: continue
        r = contatos.delete_one({'email': email})
        print('Excluído!' if r.deleted_count else 'Contato não encontrado.')
    elif op == '0':
        break
    else:
        print('Opção inválida.')
