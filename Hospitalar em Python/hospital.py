import sqlite3
from sqlite3 import Error






class Hospital:
    def __init__(self,nome,tipo,especialidade,avaliacao):
        self.nome = nome
        self.tipo = tipo
        self.especialidade = especialidade
        self.avaliacao = avaliacao

    def inserir(self):
        try:
            conecta = sqlite3.connect('D:/hospitalar.db')
            cursor = conecta.cursor()
            sair = 'n'

            while sair == 'n':
                self.nome = input ('Digite o seu nome: --> ')    
                self.tipo = input ('Digite o tipo do Hospital: --> ')
                self.especialidade = input ('Digite a especialidade: --> ')
                self.avaliacao = input ('Como você alavia o Hospital?: --> ')
            
                cursor.execute("""INSERT INTO hospital(nome_hosp,tipo_hosp,especialidade_hosp,avalia_hosp) VALUES(?,?,?,?)
                """, (self.nome,self.tipo,self.especialidade,self.avaliacao) )
                conecta.commit()
                sair = input ('Deseja parar digite s para SIM e n para NÂO: --> ')
        except Error as e:
            print(e)
        
    def mostrar(self):
        try:
            conecta = sqlite3.connect('D:/hospitalar.db')
            cursor = conecta.cursor()
            cursor.execute('SELECT * FROM hospital')
            for linha in cursor:
                print (linha)
        except Error as e:
            print (e)        
       
class Medico:
    def __init__(self,nome,crm):
        self.nome = nome
        self.crm = crm
        
    def mostrar_medico(self):
        print(self.nome,' ',self.crm)
        
        
        

