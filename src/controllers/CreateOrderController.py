from views.CreateOrderView import CreateOrderView
from services.CreteOrderService import CreateOrderService

class CreateOrderController:
  def handle():
    order = CreateOrderView.handle()
    createdOrder = CreateOrderService.execute(order)

    if createdOrder != None:
      print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
      print('Pedido salvo com sucesso:\n')
      createdOrder.readOrder()
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
