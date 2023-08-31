import time
import funcoes

print("======================== Autentificação de E-mail ==================================\n")

email = input("Favor insira seu e-mail para enviarmos um código de verificação -> ")

print("Processando...")

criar_codigo = funcoes.criar_codigo()

enviar_email = funcoes.envia_email(criar_codigo, email)

time.sleep(2)

print("Código Enviado.\n")

codigo_recebido = input("Informe o código recebido ->")

if(codigo_recebido == criar_codigo):
    print("\nVerificado com sucesso!")
else: print("\nFalha na verificação")

time.sleep(3)