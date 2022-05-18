from controllers.CreateOrderController import CreateOrderController
from controllers.FindOrderController import FindOrderController
from controllers.UpdateOrderController import UpdateOrderController
from controllers.DeleteOrderController import DeleteOrderController

if __name__ == '__main__':
  while True:
    print('-=-=-=-=-=- MENU -=-=-=-=-=-')
    print('1 - Inserir pedido')
    print('2 - Buscar pedido')
    print('3 - Atualizar pedido')
    print('4 - Deletar pedido')
    print('0 - Sair')

    option = input('\nOpção: ')

    if option == '0':
      print('\nVolte Sempre!')
      break

    options = {
      '1': CreateOrderController.handle,
      '2': FindOrderController.handle,
      '3': UpdateOrderController.handle,
      '4': DeleteOrderController.handle,
    }

    try:
      options[option]()
    except KeyError:
      print('Opção inválida!\n')
