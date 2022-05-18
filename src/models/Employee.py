class Employee:
  def __init__(
    self,
    employeeId,
    lastName,
    firstName,
    title,
    titleOfCourtesy,
    birthDate,
    hireDate,
    address,
    city,
    region,
    postalCode,
    country,
    homePhone,
    extension,
    reportsTo,
    notes,
  ):
    self.employeeId = employeeId
    self.lastName = lastName
    self.firstName = firstName
    self.title = title
    self.titleOfCourtesy = titleOfCourtesy
    self.birthDate = birthDate
    self.hireDate = hireDate
    self.address = address
    self.city = city
    self.region = region
    self.postalCode = postalCode
    self.country = country
    self.homePhone = homePhone
    self.extension = extension
    self.notes = notes
    self.reportsTo = reportsTo
  
  def createEmployee(tuple):
    return Employee(
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
      tuple[14],
      tuple[15],
    )

  def readEmployee(self):
    print('Código do funcionário: ', self.employeeId)
    print('Nome: ', self.firstName)
    print('Sobrenome: ', self.lastName)
    print('Título: ', self.title)
    print('Título de cortesia: ', self.titleOfCourtesy)
    print('Data de nascimento: ', self.birthDate)
    print('Data de admissão: ', self.hireDate)
    print('Endereço: ', self.address)
    print('Cidade: ', self.city)
    print('Região: ', self.region)
    print('CEP: ', self.postalCode)
    print('País: ', self.country)
    print('Telefone residencial: ', self.homePhone)
    print('Ramal: ', self.extension)
    print('Notas: ', self.notes)
    print('Reporta a: ', self.reportsTo)
