from services.UpdateOrderService import UpdateOrderService
from views.UpdateOrderView import UpdateOrderView

class UpdateOrderController:
  def handle():
    order = UpdateOrderView.handle()
    updatedOrder = UpdateOrderService.execute(order)

    if updatedOrder != None:
      print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
      print('Pedido atualizado com sucesso:\n')
      updatedOrder.readOrder()
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
