from psycopg2 import Error
from connection import connection
from models.Order import Order

from services.FindOrderService import FindOrderService
from services.FindOrderDetailsByOrderId import FindOrderDetailsByOrderId

class DeleteOrderService:
  def execute(id):
    try:
      # Procura a ordem
      order = FindOrderService.execute(id)
      
      # Caso não exista lança um erro
      if not order:
        raise Exception('Pedido não existe')

      section = connection.cursor()

      # Deleta detalhes do pedido
      deleteOrderDetailsQuery = 'DELETE FROM northwind.order_details WHERE orderid = %s'

      section.execute(deleteOrderDetailsQuery, [int(id)])

      # Deleta pedido
      deleteOrderQuery = 'DELETE FROM northwind.orders WHERE orderid = %s'

      section.execute(deleteOrderQuery, [int(id)])

      connection.commit()

      section.close()

      print(order)

      return order
    except Error:
      print('\n-=- Erro ao deletar pedido -=-\n')
    except Exception as error:
      print('\n-=- {} -=-\n'.format(error))
    