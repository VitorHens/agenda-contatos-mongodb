# Agenda de Contatos

Projeto de Banco de Dados do 4º bimestre.
Código base do professor Bruno: https://github.com/perabru/ProjetoBD-4Bimestre

O programa cadastra, busca, atualiza e remove contatos usando Python e MongoDB.

## Dois extras

- Organização/empresa: campo opcional no cadastro, salvo junto ao contato.
- Validação de e-mail: usa a biblioteca email-validator para verificar o formato
  e normalizar o endereço antes de cadastrar, atualizar ou remover.
  Essa validação não consulta DNS nem confirma a existência da caixa postal.

## Executar

Com Python e MongoDB instalados, execute na pasta do projeto:

```powershell
python -m pip install -r requirements.txt
python -m p04_contatos.main
```

No Compass: `laboratorio_python > contatos_p04`.
Para mudar a conexão, copie `.env.example` para `.env` e ajuste a URI.

## Testar

- Cadastre um contato com empresa e confira os campos no Compass.
- Tente cadastrar `ana`, `ana@@gmail.com` e `ana..teste@gmail.com`: devem ser recusados.
- Cadastre um e-mail válido e tente repeti-lo: a duplicação deve ser recusada.
- Busque o nome usando letras maiúsculas e minúsculas.
- Altere o telefone e remova um contato de teste.

Documentação da biblioteca: https://github.com/JoshData/python-email-validator
Não publique `.env`, bibliotecas locais ou contatos pessoais no GitHub.
