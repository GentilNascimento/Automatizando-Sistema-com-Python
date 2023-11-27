from time import sleep
import pyautogui
#Arquivo produtos.txt -  https://drive.google.com/file/d/1bEAU
#Sistema de Cadastro de Produtos - https://drive.google.com/file/d/1dOAp.
# _Passos manuais para realizar este processo?
# 1 - Clicar e digitar meu usuário
pyautogui.click(970,541, duration=0.5)
pyautogui.write('Gentil')
# 2 - Clicar e digitar minha senha
pyautogui.click(967,567, duration=0.5)
pyautogui.write('123456')
#3 - Clicar em "Entrar"
pyautogui.click(866,593, duration=0.5)
# 4 - Extrarir cada produto
with open('produtos.txt','r') as arquivo: #(abrir prod.txt,e ler arquivos)
    for linha in arquivo:
        produto = linha.split(',')[0] #(dividir linhas a cada vírgula)
        quantidade = linha.split(',')[1] #(dividir linhas a cada vírgula)
        preco = linha.split(',')[2] #(dividir linhas a cada vírgula)       
# 1 - clicar e digitar produto
        pyautogui.click(704,528, duration=0.5)
        pyautogui.write(produto)
# 2 - clicar e digitar quantidade
        pyautogui.click(697,553, duration=0.5)
        pyautogui.write(quantidade)
# 3 - clicar e digitar preço
        pyautogui.click(696,580, duration=0.5)
        pyautogui.write(preco)
# 4 - clicar em registrar 
        pyautogui.click(589,736, duration=0.5)
        sleep(1)