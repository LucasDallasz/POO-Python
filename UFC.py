from random import randint

class Pessoa:
    """
        [Classe Pessoa]:
        A classe em questão é a classe base (mãe) da class Lutador.
        Lutador por padrão, vai conter tudo que esta classe tem,
        devido a herança.
    """
    
    # Construtor
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
        
    def __str__(self) -> str: # Método especial.
        return self.nome
        
        
    # Métodos
    def alterar_nome(self, nome) -> None: # Método que altera o nome.
        setattr(self, 'nome', nome)
        
    
    def alterar_idade(self, idade) -> None: # Método que altera a idade.
        setattr(self, 'idade', idade)
        
        
        
class Lutador(Pessoa): # Herdando tudo de Pessoa.
    """
        [Classe Lutador]
        A classe em questão está herdando tudo da classe Pessoa,
        com tudo, os atributos e métodos da classe Pessoa estão
        disponíveis aqui. Mais abaixo iremos fazer exemplos.
    """
    
    # Construtor
    def __init__(self, nome, idade, peso) -> None:
        super().__init__(nome, idade) 
        self.peso = peso
        
        
    # Métodos
    def alterar_peso(self, peso): # Método que altera o peso.
        setattr(self, 'peso', peso)
        
        
class Luta:
    """
        [Classe Luta]
        A classe em questão não herda de nenhuma outra classe,
        portanto os atributos e métodos das instâncias desta classe
        só possuem os que estão aqui dentro.
    """
    
    def __init__(self, lutador1, lutador2, juiz) -> None:
        self.lutador1 = lutador1
        self.lutador2 = lutador2
        self.juiz = juiz
        self.vencedor = self.definir_vencedor()
        
        
    def definir_vencedor(self): # Definindo vencedor de uma luta.
        valor = randint(1, 2)
        if valor == 1: 
            setattr(self, 'vencedor', self.lutador1)
        else:
            setattr(self, 'vencedor', self.lutador2)
            
            
    def detalhes(self):
        return f'{self.lutador1} x {self.lutador2} = {self.vencedor} VENCEDOR! Juiz: {self.juiz}.'        
        
        
        
def main():
    
    juiz = Pessoa('Marcelo', 51)
    """
        [Instância Juiz]
        A instância em questão tem todos os métodos disponíveis da classe Pessoa.
    """
    juiz.alterar_nome('Diniz') # Utilizei o método de alterar o nome.
    
    
    
    lutador1 = Lutador('Jorge', 45, 85.0)
    lutador2 = Lutador('Pereira', 39, 92.5)
    """
        [Instância Lutador]
        Estas instâncias são da classe Lutador.
        Eu quero alterar o nome do lutador1, mas na classe Lutador, não tem o método para alterar.
        Será? vamos testar.
    """
    
    print('[EXEMPLO 1]')
    print('Nome anterior ', lutador1)
    lutador1.alterar_nome('VeioDaLancha')
    print('Nome posterior ', lutador1, end='\n\n')
    """
        Funcionou! Agora por que? como foi dito acima, a classe Lutador tem tudo que
        a class Pessoa tem, porque está ocorrendo uma herança, 
        portanto temos o método alterar_nome().
    """
    
    
    """
        [Dúvida]
        Mas e se eu quiser alterar o peso do juiz?
        1 - A instância juiz está sendo instanciada da classe Pessoa.
        2 - A classe pessoa não possuí o atributo peso;
        3 - A classe pessoa não está herdando de Lutador, que é onde está o atributo/método.
        
        Portanto não podemos fazer isso.
    """
    
    
    luta = Luta(lutador1, lutador2, juiz)
    """
        [Classe Luta]
        Acabamos de criar uma instância da Classe Luta.
        Como vimos, ela não tem herança, portando os atributos/métodos são apenas daquela classe.
    """
    
    print('[EXEMPLO 2]')
    luta.definir_vencedor()
    resultado = luta.detalhes()
    print(resultado, end='\n\n')


    """
        Pode perceber que TODAS as instâncias definidas aqui, são INDEPENDENTES.
        Os atributos são únicos, exemplo quando alteramos o nome do lutador1,
        o lutador2 continuou com o mesmo nome.
    """
    
    print('[EXEMPLO 3]')
    print('Nome Lutador 2', lutador2)

if __name__ == '__main__':
    main()
    
    
        
        
        
        
        