class Product():
  def __init__(
    self,
    productId,
    productName,
    supplirId,
    categoryId,
    quantityPerUnit,
    unityPrice,
    unitInStock,
    unitsOnOrder,
    reorderLevel,
    discontinued
  ):
    self.productId = productId
    self.productName = productName
    self.supplirId = supplirId
    self.categoryId = categoryId
    self.quantityPerUnit = quantityPerUnit
    self.unityPrice = unityPrice
    self.unitInStock = unitInStock
    self.unitsOnOrder = unitsOnOrder
    self.reorderLevel = reorderLevel
    self.discontinued = discontinued

  def createProduct(tuple):
    return Product(
      tuple[0],
      tuple[1],
      tuple[2],
      tuple[3],
      tuple[4],
      tuple[5],
      tuple[6],
      tuple[7],
      tuple[8],
      tuple[9]
    )

  def readProduct(self):
    print('Id: ', self.productId)
    print('Nome: ', self.productName)
    print('Fornecedor: ', self.supplirId)
    print('Categoria: ', self.categoryId)
    print('Quantidade: ', self.quantityPerUnit)
    print('Preço: ', self.unityPrice)
    print('Estoque: ', self.unitInStock)
    print('Vendas: ', self.unitsOnOrder)
    print('Nível: ', self.reorderLevel)
    print('Descontinuado: ', self.discontinued)
