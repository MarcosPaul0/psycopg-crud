from views.FindOrderView import FindOrderView
from services.FindOrderService import FindOrderService

class FindOrderController:
  def handle():
    orderId = FindOrderView.handle()
    order = FindOrderService.execute(orderId)
    
    if order != None:
      print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
      print('Pedido encontrado:\n')
      order.readOrder()
      print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
