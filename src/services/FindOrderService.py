from psycopg2 import Error
from connection import connection
from models.Order import Order

class FindOrderService:
  def execute(id):
    try:
      section = connection.cursor()

      query = 'SELECT * FROM northwind.orders WHERE orderid = %s'

      section.execute(query, [int(id)])

      order = section.fetchone()

      connection.commit()

      section.close()

      if order:
        return Order.createOrder(order)
      else:
        raise Exception('Pedido não encontrado')
    except Error:
      print('\n-=- Erro ao buscar pedido -=-\n')
    except Exception as error:
      print('\n-=- {} -=-\n'.format(error))
