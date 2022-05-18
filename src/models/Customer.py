class Customer:
  def __init__(
    self,
    customerId,
    companyName,
    contactName,
    contactTitle,
    address,
    city,
    region,
    postalCode,
    country,
    phone,
    fax,
  ):
    self.customerId = customerId
    self.companyName = companyName
    self.contactName = contactName
    self.contactTitle = contactTitle
    self.address = address
    self.city = city
    self.region = region
    self.postalCode = postalCode
    self.country = country
    self.phone = phone
    self.fax = fax

  def createCustomer(tuple):
    return Customer(
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
    )
  
  def readCustomer(self):
    print('Código do cliente: ', self.customerId)
    print('Nome da empresa: ', self.companyName)
    print('Nome do contato: ', self.contactName)
    print('Título do contato: ', self.contactTitle)
    print('Endereço: ', self.address)
    print('Cidade: ', self.city)
    print('Região: ', self.region)
    print('CEP: ', self.postalCode)
    print('País: ', self.country)
    print('Telefone: ', self.phone)
    print('Fax: ', self.fax)
