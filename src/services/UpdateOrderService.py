from psycopg2 import Error
from connection import connection
from models.Order import Order
from datetime import datetime

from services.FindCustomerService import FindCustomerService
from services.FindEmployeeService import FindEmployeeService

class UpdateOrderService:
  def execute(order):
    try:
      # Procura o cliente
      customer = FindCustomerService.execute(order.customerId)
      
      # Caso não exista lança um erro
      if not customer:
        raise Exception('Cliente não existe')

      # Procura o funcionário
      employee = FindEmployeeService.execute(order.employeeId)

      # Caso não exista lança um erro
      if not employee:
        raise Exception('Funcionário não existe')

      section = connection.cursor()

      # Insere o pedido
      query = 'UPDATE northwind.orders SET customerid = %s, employeeid = %s, orderdate = %s, requireddate = %s, shippeddate = %s, freight = %s, shipname = %s, shipaddress = %s, shipcity = %s, shipregion = %s, shippostalcode = %s, shipcountry = %s, shipperid = %s WHERE orderid = %s'
      values = (
        order.customerId,
        order.employeeId,
        order.orderDate,
        order.requiredDate,
        order.shippedDate,
        order.freight,
        order.shipName,
        order.shipAddress,
        order.shipCity,
        order.shipRegion,
        order.shipPostalCode,
        order.shipCountry,
        order.shipperId,
        order.orderId,
      )

      section.execute(query, values)

      connection.commit()

      section.close()

      return order
    except Error:
      print('\n-=- Erro ao cadastrar pedido -=-\n')
    except Exception as error:
      print('\n-=- {} -=-\n'.format(error))
