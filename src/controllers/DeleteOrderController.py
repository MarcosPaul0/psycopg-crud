from services.DeleteOrderService import DeleteOrderService
from views.DeleteOrderView import DeleteOrderView

class DeleteOrderController:
  def handle():
    orderId = DeleteOrderView.handle()
    deletedOrder = DeleteOrderService.execute(orderId)
    
    if deletedOrder != None:
      print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
      print('Pedido deletado com sucesso:\n')
      deletedOrder.readOrder()
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')