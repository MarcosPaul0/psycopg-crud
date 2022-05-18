from psycopg2 import Error
from connection import connection

class FindOrderDetailsByOrderId:
  def execute(orderId):
    try:
      section = connection.cursor()
      
      query = 'SELECT * FROM northwind.order_details WHERE orderid = %s'
      
      section.execute(query, [int(orderId)])
      
      orderDetails = section.fetchall()
      
      connection.commit()
      
      section.close()
      
      return orderDetails
    except Error:
      print('\n-=- Erro ao buscar detalhes do pedido -=-\n')
    except Exception as error:
      print('\n-=- {} -=-\n'.format(error))