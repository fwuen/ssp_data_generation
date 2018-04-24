import xml.etree.cElementTree as ET
import random

path = "C:/workspace/ssp_data/"

#########################################################################################
# product.xml

numberOfProducts = 100
numberOfProductTypes = 10

products = ET.Element("Products")

for x in range(0, numberOfProducts):
    product = ET.SubElement(products, "Product")
    ET.SubElement(product, "ProductID").text = str(x+1)
    ET.SubElement(product, "ProductTypeID").text = str(random.randrange(1, numberOfProductTypes+1, 1))

tree = ET.ElementTree(products)
tree.write(path + "product.xml")

#########################################################################################
# production.xml

numberOfProductions = 15000
numberOfMachines = 10
numberOfTools = 100
numberOfProductionOrders = 50

productions = ET.Element("Productions")

for x in range(0, numberOfProductions):
    production = ET.SubElement(productions, "Production")
    ET.SubElement(production, "ProductionID").text = str(x+1)

    machine = random.randint(1, numberOfMachines)
    productsMadeByEachMachine = numberOfProducts/numberOfMachines

    ET.SubElement(production, "ProductID").text = str(random.randint(machine*productsMadeByEachMachine-productsMadeByEachMachine,machine*productsMadeByEachMachine))
    ET.SubElement(production, "MachineID").text = str(machine)
    ET.SubElement(production, "ToolID").text = str(random.randint(1, numberOfTools))
    ET.SubElement(production, "ProductionOrderID").text = str(random.randint(1, numberOfProductionOrders))

    month = random.randint(1, 12)

    if month == 2:
        day = random.randint(1, 28)
        if day < 10:
            ET.SubElement(production, "ProductionDate").text = "2017-02" + "-0" + str(day)
        else:
            ET.SubElement(production, "ProductionDate").text = "2017-02" + "-" + str(day)
    elif month in (1, 3, 5, 7, 8):
        day = random.randint(1, 31)
        if day < 10:
            ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-0" + str(day)
        else:
            ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-" + str(day)
    else:
        day = random.randint(1, 30)
        if day < 10:
            if month < 10:
                ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-0" + str(day)
            else:
                ET.SubElement(production, "ProductionDate").text = "2017-" + str(month) + "-0" + str(day)
        else:
            if month < 10:
                ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-" + str(day)
            else:
                ET.SubElement(production, "ProductionDate").text = "2017-" + str(month) + "-" + str(day)

tree = ET.ElementTree(productions)
tree.write(path + "production.xml")

#########################################################################################
# prod_type.xml

productTypes = ET.Element("ProductTypes")

for x in range(0, numberOfProductTypes):
    productType = ET.SubElement(productTypes, "ProductType")
    ET.SubElement(productType, "ProductTypeID").text = str(x+1)
    if x+1 <= 3:
        ET.SubElement(productType, "ParentProductTypeID").text = str(x+1)
    else:
        ET.SubElement(productType, "ParentProductTypeID").text = str(random.randint(1, numberOfProductTypes-7))

tree = ET.ElementTree(productTypes)
tree.write(path + "prod_type.xml")

#########################################################################################
# production_order

productionOrders = ET.Element("ProductionOrders")
maxNumberOfProductionOrderItems = 50
numberOfCustomers = 2000

for x in range(0, numberOfProductionOrders):
    productionOrder = ET.SubElement(productionOrders, "ProductionOrder")
    ET.SubElement(productionOrder, "ProductionOrderID").text = str(x+1)
    ET.SubElement(productionOrder, "CustomerID").text = str(random.randint(1, numberOfCustomers))
    productionOrderItems = ET.SubElement(productionOrder, "ProductionOrderItems")

    numberOfProductionOrderItems = random.randint(1, maxNumberOfProductionOrderItems)

    for y in range(0, numberOfProductionOrderItems):
        productionOrderItem = ET.SubElement(productionOrderItems, "ProductionOrderItem")
        ET.SubElement(productionOrderItem, "ProductID").text = str(random.randint(1, numberOfProducts))

tree = ET.ElementTree(productionOrders)
tree.write(path + "production_order.xml")
