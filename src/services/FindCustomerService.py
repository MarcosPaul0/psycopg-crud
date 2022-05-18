from psycopg2 import Error
from connection import connection
from models.Customer import Customer

class FindCustomerService:
  def execute(id):
    try:
      section = connection.cursor()

      query = 'SELECT * FROM northwind.customers WHERE customerid = %s'

      section.execute(query, [str(id)])

      customer = section.fetchone()

      connection.commit()

      section.close()

      if customer:
        return Customer.createCustomer(customer)
      else:
        raise Exception('Cliente não encontrado')
    except Error as pError:
      print('\n-=- {} -=-\n'.format(pError))
    except Exception as error:
      print('\n-=- {} -=-\n'.format(error))
