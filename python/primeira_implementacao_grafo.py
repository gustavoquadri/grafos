def pedir_posicoes():
    while 1:
        try:
            posicao = input("digite a posicao da aresta (ex: 1,2): ")
            posicao_um, posicao_dois = posicao.split(",")
            return posicao_um, posicao_dois
        except ValueError:
            print("input nao e um numero! tente novamente")

def pedir_peso():
    while 1:
        try:
            peso = int(input("digite um peso para essa aresta: "))
            return peso
        except ValueError:
            print("input nao e um numero! tente novamente")


def iniciar_novo_grafo():

    arestas = int(input("quantas arestas deseja? "))
    vertices = int(input("quantos vertices deseja? "))
    
    grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    print("grafo inicial")
    for linha in grafo:
        print(linha)
    
    return grafo, arestas


def adicionar_arestas_grafo_normal(grafo, arestas):
    contador = 0
    while contador < arestas:
        posicao_um, posicao_dois = pedir_posicoes()
        
        try:
            if grafo[int(posicao_um)][int(posicao_dois)] == 0:
                grafo[int(posicao_um)][int(posicao_dois)] = 1
                grafo[int(posicao_dois)][int(posicao_um)] = 1
                contador += 1
                mostrar_grafo(grafo)
            else:
                print("posicao ja alocada, tente outra")
                mostrar_grafo(grafo)
        except IndexError:
            print("lembre que estamos tratando em indices! (comeca do 0 ate o limite-1)")
  
  
def adicionar_arestas_grafo_ponderado(grafo, arestas):
    contador = 0
    
    while contador < arestas:
        posicao_um, posicao_dois = pedir_posicoes()
        
        try:
            if grafo[int(posicao_um)][int(posicao_dois)] == 0:
                peso = pedir_peso()
                grafo[int(posicao_um)][int(posicao_dois)] = peso
                grafo[int(posicao_dois)][int(posicao_um)] = peso
                contador += 1
                mostrar_grafo(grafo)
            else:
                print("posicao ja alocada, tente outra")
                mostrar_grafo(grafo)
        except IndexError:
            print("lembre que estamos tratando em indices! (comeca do 0 ate o limite-1)")
   

def adicionar_arestas_grafo_direcionado(grafo, arestas):
    contador = 0
    
    while contador < arestas:
        posicao_um, posicao_dois = pedir_posicoes()
        
        try:
            if grafo[int(posicao_um)][int(posicao_dois)] == 0:
                grafo[int(posicao_um)][int(posicao_dois)] = 1
                contador += 1
                mostrar_grafo(grafo)
            else:
                print("posicao ja alocada, tente outra")
                mostrar_grafo(grafo)
        except IndexError:
            print("lembre que estamos tratando em indices! (comeca do 0 ate o limite-1)")


def adicionar_arestas_grafo_direcionado_com_peso(grafo, arestas):
    contador = 0
    
    while contador < arestas:
        posicao_um, posicao_dois = pedir_posicoes()
        
        try:
            if grafo[int(posicao_um)][int(posicao_dois)] == 0:
                peso = pedir_peso()
                grafo[int(posicao_um)][int(posicao_dois)] = peso
                contador += 1
                mostrar_grafo(grafo)
            else:
                print("posicao ja alocada, tente outra")
                mostrar_grafo(grafo)
        except IndexError:
            print("lembre que estamos tratando em indices! (comeca do 0 ate o limite-1)")
   

def mostrar_grafo(grafo):
    for linha in grafo:
        print(linha)

def menu():
    grafo = ""
    arestas = ""
    uso = 0
    while 1:
        print("="*10)
        print("1. Iniciar novo grafo.")
        print("2. Adicionar arestas (grafo normal).")
        print("3. Adicionar arestas (grafo ponderado).")
        print("4. Adicionar arestas (grafo direcionado).")
        print("5. Adicionar arestas (grafo direcionado ponderado).")
        print("6. Mostrar grafo.")
        print("0. Sair")
        escolha = int(input())

        match escolha:
            case 1:
                grafo, arestas = iniciar_novo_grafo()
                print("grafo inicializado")
                uso = 0
            case 2:
                if uso == 0:
                    adicionar_arestas_grafo_normal(grafo, arestas)
                    uso = 1
                else:
                    print("gere um novo grafo, esse ja foi modificado!")
            case 3:
                if uso == 0:
                    adicionar_arestas_grafo_ponderado(grafo, arestas)
                    uso = 1
                else:
                    print("gere um novo grafo, esse ja foi modificado!")
            
            case 4:
                if uso == 0:
                    adicionar_arestas_grafo_direcionado(grafo, arestas)
                    uso = 1
                else:
                    print("gere um novo grafo, esse ja foi modificado!")
                
            case 5:
                if uso == 0:
                    adicionar_arestas_grafo_direcionado_com_peso(grafo, arestas)
                    uso = 1
                else:
                    print("gere um novo grafo, esse ja foi modificado!")
            
            case 6:
                if grafo != "":
                    mostrar_grafo(grafo)
                else:
                    print("inicialize antes o grafo!")

            case 0:
                print("saindo...")
                print("="*10)
                break
        

if __name__ == '__main__':
    menu()