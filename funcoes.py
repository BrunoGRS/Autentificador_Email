import pyotp
import smtplib
import time

def criar_codigo():

    chave_mestra = 'QEBQ3JCS4RJDP5JR3QNX4TFLW5E7ZYJ5'

    codigo_verificacao = pyotp.TOTP(chave_mestra)

    codigo =codigo_verificacao.now()

    return codigo


def envia_email(codigo, email):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("bruno.rodriguesr01@gmail.com", "dpgajloztbmdlrip")
    server.sendmail(
    "brunorodriguesr01@gmail.com",
    email,
    codigo)
    server.quit()