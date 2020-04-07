# coding: iso-8859-1 -*-
# Importando uma biblioteca do Python para operar o sistema operacional (OS)
import os

msg_commit = input("Mensagem do commit: ")

# Se a mensagem for pequena demais, for�a o usu�rio a digitar uma msg maior
while len(msg_commit) < 5:
    print("A mensagem deve ter pelo menos 5 caracteres.")
    msg_commit = input("Mensagem do commit: ")

# Define um email padr�o para este script
email = "lucasnavarro103@gmail.com"

# O \n dentro do print funciona como o <br/> no HTML (pula mais uma linha)
print("\n------------------------------------")

print("Adicionando os novos arquivos...\n")
os.system("git add *")

# O + soma quando os operadores s�o n�meros e junta (une, concatena) quando s�o strings
print("Configurando o email do usu�rio...\n")
os.system('git config user.email "'+email+'"')

print("Efetuando o commit das modifica��es...\n")
os.system('git commit -m "'+msg_commit+'"')

print("Conectando com os servidores do Github...\n")
os.system('git push origin master')