class Order:
  def __init__(
    self, 
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
    shipPerId,
  ):
    self.orderId = int(orderId)
    self.customerId = str(customerId)
    self.employeeId = int(employeeId)
    self.orderDate = str(orderDate)
    self.requiredDate = str(requiredDate)
    self.shippedDate = str(shippedDate)
    self.freight = float(freight)
    self.shipName = str(shipName)
    self.shipAddress = str(shipAddress)
    self.shipCity = str(shipCity)
    self.shipRegion = str(shipRegion)
    self.shipPostalCode = str(shipPostalCode)
    self.shipCountry = str(shipCountry)
    self.shipperId = int(shipPerId)

  def createOrder(tuple):
    return Order(
      tuple[0],
      tuple[1],
      tuple[2],
      tuple[3],
      tuple[4],
      tuple[5],
      tuple[6],
      tuple[7],
      tuple[8],
      tuple[9],
      tuple[10],
      tuple[11],
      tuple[12],
      tuple[13],
    )

  def readOrder(self):
    print('Código do pedido: ', self.orderId)
    print('Código do cliente: ', self.customerId)
    print('Código do funcionário: ', self.employeeId)
    print('Data do pedido: ', self.orderDate)
    print('Data de entrega: ', self.requiredDate)
    print('Data de envio: ', self.shippedDate)
    print('Frete: ', self.freight)
    print('Nome da entregadora: ', self.shipName)
    print('Endereço da entrega: ', self.shipAddress)
    print('Cidade da entrega: ', self.shipCity)
    print('Região da entrega: ', self.shipRegion)
    print('CEP da entrega: ', self.shipPostalCode)
    print('País da entrega: ', self.shipCountry)
    print('Código do funcionário de entrega: ', self.shipperId)
