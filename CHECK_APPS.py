import csv                                                      #importa biblioteca responsavel pelo formato csv
import random                                                   #importa biblioteca responsavel por numeros aleatorios
from datetime import date                                       #
import datetime                                                 #   bibliotecas responsaveis pela verificacao da data e hora
import time                                                     #   
import requests                                                 #biblioteca utilizada para requests e verificacao do status da pagina



today = date.today()                                            #define a variavel today como a data usando a funcao da biblioteca datetime date
today_s = str(today)                                            #transfere a data today para uma nova string para que seja utilizada depois
ts = datetime.datetime.now().time()   
tss = str(ts)
first_run = 1   

def check_data():
    global first_run
    first_run = 1                                                   #define a variavel first run para verificar se e a primeira vez que o programa esta rodando
    try:                                                            #caso o arquivo nao exista na pasta ele ira criar o novo arquivo com cabecalho
        f = open("app01_DATA.csv")                                        #abre o arquivo como f
        g = open("app02_DATA.csv")
        first_run = 0                                      
        f.close()                                                   #fecha o arquivo pois a verificao esta completa
        g.close()
    except IOError:                                                 #caso o arquivo nao exista
        first_run = 1                                               #e dado como a primeira vez rodando e sera necessario criar um novo arquivo com cabecalho
    
    



def create_request(url):
    global ts
    global tss
    ts = datetime.datetime.now().time()                             #define a variavel ts como a hora
    tss = str(ts)                                                   #transfere a variavel ts para uma string para que seja utilizada depois
    try:                                                            #caso a conexao seja bem sucedida
        r = requests.head(url)       #cria a request
        status = r.status_code                                      #executa o pedido de status
        status = "CONNECTION"                                       #define a string status como connection em funcao de simplificar o exercicio
    
    except requests.ConnectionError:                                #caso houver erro de conexao
        status = "NO CONNECTION"                                    #define status como sem conexao em uma string
    
    return status
    
header = ['DATA_REGISTRO', 'APLICACAO', 'STATUS', 'LATENCIA', 'DATA_COLETA']        #cria o cabecalho conforme o exercicio
data = [today_s, "app01", create_request("https://server-linux/app1/status"), str(random.randint(30,50)), tss]      
data2 = [today_s, "app02", create_request("https://server-linux/app2/status"), str(random.randint(30,50)), tss]           
print(", ".join(data))
print(", ".join(data2))      
#header_line = "; ".join(header)                                                     #junta a lista do cabecalho em uma so string
#data_line = "; ".join(data)                                                         #junta a lista de dados em uma so string
#header = [header_line]                                                              #define a string como item da lista para que seja escrita no documento
#data = [data_line]                                                                  #define a string dos dados como itens da lista tambem

check_data()

with open('app01_DATA.csv', 'a', newline='', encoding='UTF8') as f:                       #abre o arquivo no modo append para que os dados nao sejam apagados
    writer = csv.writer(f)                                                          #cria o objeto writer da biblioteca csv
    
    if first_run == 1:                                                              #caso seja a primeira vez esta variavel estara como um
        writer.writerow(header)                                                     #escrever o cabecalho
        writer.writerow("")                                                         #pula uma linha

    writer.writerow(data)                                                           #escreve os dados mais recentes recolhidos no documento csv
    f.close()
    
with open('app02_DATA.csv', 'a', newline='', encoding='UTF8') as f:                       #abre o arquivo no modo append para que os dados nao sejam apagados
    writer = csv.writer(f)                                                          #cria o objeto writer da biblioteca csv
    
    if first_run == 1:                                                              #caso seja a primeira vez esta variavel estara como um
        writer.writerow(header)                                                     #escrever o cabecalho
        writer.writerow("")                                                         #pula uma linha

    writer.writerow(data2)
    f.close()