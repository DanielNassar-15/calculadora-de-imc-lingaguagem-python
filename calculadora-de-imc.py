altura = float(input("Qual sua altura?: ")) 
altura = altura / 100
#insira sua altura.

peso = float(input("Qual seu peso?: ")) 
#insira seu peso.

imc = peso / (altura * altura) 
#cálculo do IMC.

if(imc < 18.5):
    print(f"\nSeu IMC é: {imc:.2f}")
    print("Você está no abaixo do peso.")
#condição de IMC abaixo do ideal.

elif(imc >= 18.5 and imc <= 24.9):
    print(f"\nSeu IMC é: {imc:.2f}")
    print("Você está no peso ideal.")
#condição de IMC ideal.    

elif(imc >= 25.0 and imc <= 29.9):
    print(f"\nSeu IMC é: {imc:.2f}")
    print("Você está acima do peso.")
#condição de IMC acima do ideal.

elif(imc >= 30.0 and imc <= 34.9):
    print(f"\nSeu IMC é: {imc:.2f}")
    print("Você está com obesidade nível 1.")
#condição de IMC de obesidade nível 1.

elif(imc >= 35.0 and imc <= 39.9):
    print(f"\nSeu IMC é: {imc:.2f}")
    print("Você está com obesidade nível 2.")
#condição de IMC de obesidade nível 2.

else:
    print(f"\nSeu IMC é: {imc:.2f}")
    print("Você está com obesidade nível 3.")
#condição de IMC de obesidade nível 3.
