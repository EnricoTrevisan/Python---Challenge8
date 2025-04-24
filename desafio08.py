# Desenvolva uma calculadora de operações básicas (+, -, /, *) na qual o usuário entre com 2 números 
# e a operação e depois realize o cálculo. Esse programa pode se repetir até o usuário quiser finalizar.
print("--------------->Programa de Calculadora<---------------")

opcao = 's'
resultado = ''

print("Olá. Seja bem-vindo a calculadora Seixon 0.5! Por recursos limitados, apenas poderá ser feito operações de soma, subtração, multiplicação ou/e de divisão.")
print("Então, para fazer sua conta, diga em minúsculo qual é a sua operação. Por exemplo: 'Soma' seria 'soma'.")
while opcao == 's':

    num1 = int(input('Então, para iniciar, digite o primeiro número para o seu cálculo:'))
    num2 = int(input("Agora, digite o segundo número para o seu cálculo:"))

    operacao = (input("Por fim, digite a operação que deseja usar. Caso deseja terminar de usar nossa calculadora, apenas escreva 'finalizar':"))

    if operacao == 'soma':
        resultado = print(num1 + num2)        

    elif operacao == "subtração":
        resultado = print(num1 - num2)
    elif operacao == "multiplicação":
        resultado = print(num1 * num2)
    elif operacao == "divisão":
            resultado = print(num1/num2)
    elif operacao == "finalizar":
        print("Obrigado por usar nossa calculadora. Esperamos para sua próxima visita.")

print("--------------->Finalização do Programa<---------------")