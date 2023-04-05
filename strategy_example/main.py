# demora 30 min para atualizar o sistema.
# OS sistema não são interligados
# Existe milhares de franquiados


class Macaccino:

    def __init__(self):
        self.valor = 0.99
        self.ingredientes = "Cafe, leite, chocolate em pó"

    def __str__(self):
        return f"Macaccino: {self.valor}, {self.ingredientes}"
    
class CafePingado:

    def __init__(self):
        self.valor = 0.99
        self.ingredientes = "Cafe, leite"

    def __str__(self):
        return f"Café Pingado: {self.valor}, {self.ingredientes}"
    

class CafeExpresso:
    
        def __init__(self):
            self.valor = 0.99
            self.ingredientes = "Café expresso"
    
        def __str__(self):
            return f"Café Expresso: {self.valor}, {self.ingredientes}"
        

class Canela:

    def __init__(self):
        self.valor = 0.10
        self.ingredientes = "Canela"

    def __str__(self):
        return f"Canela: {self.valor}, {self.ingredientes}"
    

class Chantilly:

    def __init__(self):
        self.valor = 0.10
        self.ingredientes = "Chantilly"

    def __str__(self):
        return f"Chantilly: {self.valor}, {self.ingredientes}"


class Menu:


    def __init__(self):
        self.PedidoCliente = None


    def Pedido(self, itemMenu):

        if self.PedidoCliente is None:
            self.PedidoCliente = itemMenu

        else:


            self.PedidoCliente.valor = self.PedidoCliente.valor + itemMenu.valor

            self.PedidoCliente.ingredientes = self.PedidoCliente.ingredientes +", "+ itemMenu.ingredientes

            


            


if __name__ == "__main__":

    starbucksMenu = Menu()

    pedido = Macaccino()
    starbucksMenu.Pedido(pedido)

    adicionalCanela = Canela()
    starbucksMenu.Pedido(adicionalCanela)


    adicionalChantilly = Chantilly()
    starbucksMenu.Pedido(adicionalChantilly)


    print(starbucksMenu.PedidoCliente)