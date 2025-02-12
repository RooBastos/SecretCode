# Missão 5: Recuperando o Cofre de Segurança 🔒
# O cofre da biblioteca guarda códigos raros de programação, mas o vírus resetou a senha!
# Agora, apenas quem souber a combinação correta poderá acessá-lo.
# Crie um programa que solicite ao usuário uma senha e verifique se ela está correta.
# A senha correta é "Python123".


senha_correta = "Python123"
senha_usuario = input("Digite a senha para acessar o cofre: ")

if senha_usuario == senha_correta:
    print("Acesso concedido! Bem-vindo ao cofre de segurança.")
else:
    print("Senha incorreta! Acesso negado.")
