## Deploy
Aplicação publicada em: https://controle-estoque-micro.onrender.com

## Nova Funcionalidade (Etapa 2)
Integração com a [AwesomeAPI](https://economia.awesomeapi.com.br) para exibir
a cotação do dólar em tempo real, auxiliando microempreendedores na
precificação de produtos importados.

# Controle de Estoque para Microempreendedores

## Problema Real
Microempreendedores muitas vezes perdem o controle manual de seus produtos, resultando em prejuízos financeiros por falta de estoque ou excesso de itens parados.

## Solução
Uma aplicação simples via linha de comando (CLI) que permite registrar entradas de produtos com validações de segurança.

## Tecnologias
- **Linguagem:** Python
- **Testes:** Pytest
- **Qualidade:** Ruff (Linting)
- **CI:** GitHub Actions

## Como usar
1. Instale as dependências: `pip install -r requirements.txt`
2. Rode o app: `python src/main.py`
3. Rode os testes: `pytest`

## Funcionalidades Principais
* Cadastro rápido de itens.
* Validação de quantidades negativas.
* Listagem simplificada.

**Autor:** Danilo Vilela Franco
**Versão:** 1.0.0
