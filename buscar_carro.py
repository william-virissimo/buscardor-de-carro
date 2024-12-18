
class carro():
    def __init__(self, modelo):
        self.modelo = modelo


    def caracteristica():

        modelo= input('digite um carro: ').lower()       
        lista_modelos = ['fusion', 'c180', 'jetta', 'golf', 'gol', 'up', ]
        lista_marcas = ['ford', 'mercedes', 'vw', 'vw', 'vw', 'vw']
        lista_ano = [2014,2020,2022,2023,2024,2020]
        lista_cambio = ['manual','automatico', 'automatico','manual','manual','manual',]
        lista_cor = ['preto','prata','prata', 'preto','vermelho','branco']

        carros = zip(lista_modelos,lista_marcas, lista_ano, lista_cambio, lista_cor)

        for carro in carros:
            if carro[0] == modelo:
                print(f"Modelo: {carro[0]}")
                print(f"Marca: {carro[1]}")
                print(f"Ano: {carro[2]}")
                print(f"Câmbio: {carro[3]}")
                print(f"Cor: {carro[4]}")
                break
        else:
            print("Modelo não encontrado.")

                
carro.caracteristica()
      
# caracteriscas
    # cor 
    # ano
    # marca

#  metodo da classe 'carro'
    # modelo
'''
modelos = [a, b , c , d , e , f , g , h , y , j , k ]
 opcoes= modelos 
 a= automatico 
m = manual 
'''