from cotacao import buscar_cotacao_dolar

def adicionar_produto(estoque, nome, qtd):
    if qtd < 0:
        return False
    estoque[nome] = estoque.get(nome, 0) + qtd
    return True

def main():
    estoque = {}
    print("--- Controle de Estoque Micro ---")

    cotacao = buscar_cotacao_dolar()
    if cotacao:
        print(f"💵 Cotação do dólar (USD): R$ {cotacao:.2f}")
    else:
        print("⚠️  Cotação indisponível no momento.")

    while True:
        nome = input("Produto (ou 'sair'): ")
        if nome.lower() == 'sair':
            break
        try:
            qtd = int(input("Quantidade: "))
            if adicionar_produto(estoque, nome, qtd):
                print(f"Estoque atual: {estoque}")
            else:
                print("Erro: Quantidade negativa!")
        except ValueError:
            print("Erro: Digite um número válido.")

if __name__ == "__main__":
    main()
