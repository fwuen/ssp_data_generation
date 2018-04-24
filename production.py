#########################################################################################

# production.xml

# numberOfMachines = 10
# numberOfTools = 100
#
# productions = ET.Element("Productions")
#
# for x in range(0, numberOfProductions):
#     production = ET.SubElement(productions, "Production")
#     ET.SubElement(production, "ProductionID").text = str(x+1)
#
#     machine = random.randint(1, numberOfMachines)
#     productsMadeByEachMachine = numberOfProducts/numberOfMachines
#
#     productType = random.randint(1, numberOfProductTypes)
#     productsPerProductType = numberOfProducts/numberOfProductTypes
#
#     product = ET.SubElement(production, "Product")
#     productId = ET.SubElement(product, "ProductID").text = products.
#     ET.SubElement(product, "ProductName").text = "Product" + str(productId)
#     ET.SubElement(product, "ProductTypeID").text = str(machine)
#
#     ET.SubElement(production, "MachineID").text = str(machine)
#     ET.SubElement(production, "ToolID").text = str(random.randint(1, numberOfTools))
#     ET.SubElement(production, "ProductionOrderID").text = str(random.randint(1, numberOfProductionOrders))
#
#     month = random.randint(1, 12)
#
#     if month == 2:
#         day = random.randint(1, 28)
#         if day < 10:
#             ET.SubElement(production, "ProductionDate").text = "2017-02" + "-0" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#         else:
#             ET.SubElement(production, "ProductionDate").text = "2017-02" + "-" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#     elif month in (1, 3, 5, 7, 8):
#         day = random.randint(1, 31)
#         if day < 10:
#             ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-0" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#         else:
#             ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#     else:
#         day = random.randint(1, 30)
#         if day < 10:
#             if month < 10:
#                 ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-0" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#             else:
#                 ET.SubElement(production, "ProductionDate").text = "2017-" + str(month) + "-0" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#         else:
#             if month < 10:
#                 ET.SubElement(production, "ProductionDate").text = "2017-0" + str(month) + "-" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#             else:
#                 ET.SubElement(production, "ProductionDate").text = "2017-" + str(month) + "-" + str(day) + " " + str(random.randint(0,23)) + ":" + str(random.randint(0,59))
#
# tree = ET.ElementTree(productions)
# tree.write(path + "production.xml")
