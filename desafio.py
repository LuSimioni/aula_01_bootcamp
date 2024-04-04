#Instruções:

CONSTANTE_BONUS = 1000

#1. O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Digite seu nome: ")

#2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario = float(input("Digite o valor do seu salário: "))

#3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus = float(input("Digite o seu bônus: "))

#4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
valor_bonus = CONSTANTE_BONUS + salario * bonus

#5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome}, o seu valor bônus foi de {valor_bonus}")

#Salve esse script python como kpi.py
#Faça uma documentação simples de como executar esse programa, utilize o README
#Salve no Git e no Github