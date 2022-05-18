from datetime import date

from models.Order import Order


class CreateOrderView:
  def handle():
    orderId = input('Código do pedido: ')
    customerId = input('Código do cliente: ')
    employeeId = input('Código do funcionário: ')
    orderDate = input('Data do pedido (mm-dd-aaaa): ')
    requiredDate = input('Data de entrega (mm-dd-aaaa): ')
    shippedDate = input('Data de envio (mm-dd-aaaa): ')
    freight = input('Frete: ')
    shipName = input('Nome da entregadora: ')
    shipAddress = input('Endereço da entrega: ')
    shipCity = input('Cidade da entrega: ')
    shipRegion = input('Região da entrega: ')
    shipPostalCode = input('CEP da entrega: ')
    shipCountry = input('País da entrega: ')
    shipperId = input('Código do funcionário de entrega: ')

    return Order(
      orderId,
      customerId,
      employeeId,
      orderDate,
      requiredDate,
      shippedDate,
      freight,
      shipName,
      shipAddress,
      shipCity,
      shipRegion,
      shipPostalCode,
      shipCountry,
      shipperId
    )
