print("====================================")
print("      CAIXA ELETRÔNICO PYTHON")
print("====================================")

valor = int(input("Digite o valor do saque: R$ "))

notas_disponiveis = [200, 100, 50, 20, 10, 5, 2, 1]

usar_notas = []

print("\nEscolha quais notas deseja usar:")
print("(Digite S para SIM ou N para NÃO)\n")

for nota in notas_disponiveis:
    resposta = input(f"Usar nota de R$ {nota}? ").upper()

    if resposta == "S":
        usar_notas.append(nota)

# ordena do maior para o menor
usar_notas.sort(reverse=True)

print("\n====================================")
print("RESULTADO DO SAQUE")
print("====================================")

restante = valor

for nota in usar_notas:

    quantidade = restante // nota

    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {nota}")

    restante = restante % nota

# verifica se conseguiu sacar tudo
if restante > 0:
    print("\nNão foi possível sacar o valor exato.")
    print(f"Faltou sacar: R$ {restante}")
else:
    print("\nSaque realizado com sucesso!")

print("====================================")