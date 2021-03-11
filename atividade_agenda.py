class Agenda(object):
    listaPessoas = []
    
    def armazenaPessoa(self, nome, idade, altura):
        
        if len(self.listaPessoas) < 10: #armazenamento limitado a 10 cadastros de pessoa
            dic = {
                "nome": nome, 
                "idade": idade, 
                "altura": altura
            }
            self.listaPessoas.append(dic)
            return True
        else:
            return False

    def removePessoa(self, nome):
        if len(self.listaPessoas) != 0:
           for pessoa in self.listaPessoas:
               if pessoa["nome"] == nome:
                    self.listaPessoas.remove(pessoa)
                    return 0
           return -1 #pessoa não encontrada
        return -2 #não existem cadastros

    def buscaPessoa(self, nome):
        if len(self.listaPessoas) != 0:
            for pessoa in self.listaPessoas:
                if pessoa["nome"] == nome:
                    return self.listaPessoas.index(pessoa)
            return -1 #pessoa não encontrada
        return -2 #não existem cadastros

    def imprimeAgenda(self):
        print(self.listaPessoas)

    def imprimePessoa(self, index):

        if len(self.listaPessoas) != 0:
            if index < len(self.listaPessoas):
                print(self.listaPessoas[index])
                return -1 #índice não encontrado
        return -2 #não existem cadastros


agenda = Agenda() 

opcao = int(input("Digite a opção que deseja executar:\n"
          "1 - Armazena Pessoa na Agenda\n"
          "2 - Remove Pessoa\n"
          "3 - Imprimir Pessoa pelo nome\n"
          "4 - Imprimir Agenda\n"
          "5 - Imprimir Pessoa pelo índice\n"
          "6 - Sair do Programa\n"))

if 1 <= opcao <= 6:
    if opcao == 1:
        registro = input("Digite o nome, idade e altura da pessoa separados por vírgula: \n")
        registroSplit = registro.split(",")
        nome = registroSplit[0]
        idade = registroSplit[1]
        altura = registroSplit[2]

        if agenda.armazenaPessoa(nome, idade, altura) == True:
            print("Pessoa armazenada com sucesso! \n")
        elif agenda.armazenaPessoa(nome, idade, altura) == False:
            print("Erro ao armazenar pessoa. \n")
        else:
            print("ERRO. \n")

    elif opcao == 2:
        pessoa = input("Digite o nome da pessoa que deseja remover: \n")
        agenda.removePessoa(pessoa)

        if agenda.removePessoa(pessoa) == 0:
            print("Pessoa removida com sucesso! \n")
        elif agenda.removePessoa(pessoa) == -1:
            print("Pessoa não encontrada. \n")
        elif agenda.removePessoa(pessoa) == -2:
            print("Não existem pessoas cadastradas no sistema. \n")
        else:
            print("ERRO. \n")

    elif opcao == 3:
        pessoa = input("Digite o nome da pessoa cadastrada: \n")
        buscaPessoa = agenda.buscaPessoa(pessoa)

        if buscaPessoa >= 0:
            print("A posição da pessoa é: %d" %buscaPessoa)
        elif buscaPessoa == -1:
            print("Pessoa não encontrada. \n")
        elif buscaPessoa == -2:
            print("Não existem pessoas cadastradas no sistema. \n")
        else:
            print("ERRO. \n")

    elif opcao == 4:
        agenda.imprimeAgenda()

    elif opcao == 5:
        indice = int(input("Digite a posição(índice) na agenda em que a pessoa está cadastrada. \n"))
        imprimePessoa = agenda.imprimePessoa(indice)

        if imprimePessoa >= 0:
            print("Os dados da pessoa é: %s \n" %imprimePessoa)
        elif imprimePessoa == -1:
            print("Índice não encontrado. \n")
        elif imprimePessoa == -2:
            print("Não existem pessoas cadastradas no sistema. \n")
        else:
            print("ERRO. \n")

    else: 
        print("Programa encerrado! \n")
else:
    print("Opção inválida. Tente novamente!")
