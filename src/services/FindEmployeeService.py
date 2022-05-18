from psycopg2 import Error
from connection import connection
from models.Employee import Employee

class FindEmployeeService:
  def execute(id):
    try:
      section = connection.cursor()

      query = 'SELECT * FROM northwind.employees WHERE employeeid = %s'

      section.execute(query, [int(id)])

      employee = section.fetchone()

      connection.commit()

      section.close()

      if employee:
        return Employee.createEmployee(employee)
      else:
        raise Exception('Funcionário não encontrado')
    except Error:
      print('\n-=- Erro ao buscar funcionário -=-\n')
    except Exception as error:
      print('\n-=- {} -=-\n'.format(error))
