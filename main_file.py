import csv
import json


def saveJson():
    with open('new-json/prods.json', 'w') as outfile:
        json.dump(prodDict, outfile)
    with open('new-json/stds.json', 'w') as outfile:
        json.dump(stdDict, outfile)
    with open('new-json/collections.json', 'w') as outfile:
        json.dump(collDict, outfile)


def read_csv(filename):
    with open(filename,  encoding="utf8") as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]


prodDict = read_csv("new-files/prods.csv")
stdDict = read_csv("new-files/stds.csv")
collDict = read_csv("new-files/collections.csv")


# saveJson()
all_sizes = []


def getProductsSize(dict, flag):
    filtered = []
    pdo1 = []
    for x in dict:
        if x['Style Code'] == flag:
            filtered.append(x)

    for filter in filtered:
        pdo1.append(str(filter['Size']).strip())
        all_sizes.append(str(filter['Size']).strip())

    return pdo1


def sortProductSize(sizes):
    if '' in sizes:
        sizes.remove('')
    sizeOne = ['XXS', 'XS', 'S', 'S/M', 'M', 'M/XL', 'L', 'L/XL', 'XL', 'XXL', 'XXXL', 'XXXXL', '4XL', '5XL', '6XL', '7XL', '8XL', 'XX/3X', 'XX/4X', '4X/5X', '6X/7X']
    sizeTwo = ['B001', 'B002', 'B003', 'B004', 'B005', 'B006', 'B007', 'B008', 'B009', 'B010', 'B011']
    sizeThree = ['P027', 'P028', 'P029', 'P030', 'P031', 'P032', ]
    sizeFour = [str(x) for x in range(1, 200 + 1)]

    sizeSequences = []
    if 'B' in ''.join(sizes):
        sizeSequences = sizeTwo
    elif 'P' in ''.join(sizes):
        sizeSequences = sizeThree
    elif any(x in sizes for x in sizeOne):
        sizeSequences = sizeOne
    else:
        sizeSequences = sizeFour

    sizes.sort(key=lambda size: sizeSequences.index(size))

    return sizes


def getProductsColor(dict, flag):
    filtered = []
    pdo1 = []
    for x in dict:
        if x['Style Code'] == flag:
            filtered.append(x)

    for filter in filtered:
        pdo1.append(str(filter['Colour']).strip())

    return pdo1


def buildProductsStandardList(flag):
    stdItems = ""
    for keys in stdDict:
        if keys["Style"] == flag:
            stdItems = ""
            for key in keys:
                if key == "Style":
                    continue
                elif str(keys[key]).strip() != "":
                    stdItems += "<li>" + str(keys[key]).strip() + "</li>"
                else:
                    break

    return "<p></p>" if stdItems == "" else "<ul>" + stdItems + "</ul>"


def generateNewCSVDictionary():
    finalData = []
    productFlag = ""
    for key in prodDict:

        if productFlag != key['Style Code']:
            productFlag = key['Style Code']

            newRowObj = {}

            prodSizes = sortProductSize(sizes=list(set(getProductsSize(dict=prodDict, flag=key['Style Code']))))
            prodColours = getProductsColor(dict=prodDict, flag=key['Style Code'])

            standared = buildProductsStandardList(flag=key['Style Code'])

            collections = ''
            for mKey in collDict:
                if mKey['Style'] == key['Style Code']:
                    collections = mKey['ProductRange'] + ';' + mKey['ProductGroup']

            newRowObj['handleId'] = key['Style Code']
            newRowObj['fieldType'] = 'Product'
            newRowObj['name'] = key['Style Code'] + ' - ' + key['Product']
            newRowObj['description'] = key['Description']
            newRowObj['productImageUrl'] = key['Image']
            newRowObj['price'] = float(key['Price'])*2 if key['Price'] else 0.0
            newRowObj["surcharge"] = 0.0
            newRowObj['visible'] = 'TRUE'
            newRowObj['inventory'] = 'InStock'
            newRowObj['weight'] = key['Weight (KG)']
            newRowObj["collection"] = collections
            newRowObj["sku"] = key['Item']
            newRowObj["ribbon"] = ''
            newRowObj["discountMode"] = ''
            newRowObj["discountValue"] = ''
            newRowObj['productOptionName1'] = 'Size'
            newRowObj['productOptionType1'] = "DROP_DOWN"
            newRowObj['productOptionDescription1'] = ';'.join(prodSizes)
            newRowObj['productOptionName2'] = 'Color'
            newRowObj['productOptionType2'] = "DROP_DOWN"
            newRowObj['productOptionDescription2'] = ';'.join(set(prodColours))
            newRowObj["productOptionName3"] = ''
            newRowObj["productOptionType3"] = ''
            newRowObj["productOptionDescription3"] = ''
            newRowObj["productOptionName4"] = ''
            newRowObj["productOptionType4"] = ''
            newRowObj["productOptionDescription4"] = ''
            newRowObj["productOptionName5"] = ''
            newRowObj["productOptionType5"] = ''
            newRowObj["productOptionDescription5"] = ''
            newRowObj["productOptionName6"] = ''
            newRowObj["productOptionType6"] = ''
            newRowObj["productOptionDescription6"] = ''
            newRowObj["additionalInfoTitle1"] = 'Fit'
            newRowObj["additionalInfoDescription1"] = "<p>" + key['Fit'] + "</p>"
            newRowObj["additionalInfoTitle2"] = 'Length'
            newRowObj["additionalInfoDescription2"] = "<p>" + key['Length'] + "</p>"
            newRowObj["additionalInfoTitle3"] = 'Width'
            newRowObj["additionalInfoDescription3"] = "<p>" + key['Width'] + "</p>"
            newRowObj["additionalInfoTitle4"] = 'Height'
            newRowObj["additionalInfoDescription4"] = "<p>" + key['Height'] + "</p>"
            newRowObj["additionalInfoTitle5"] = 'Box Quantity'
            newRowObj["additionalInfoDescription5"] = "<p>" + key['Box Qty'] + "</p>"
            newRowObj["additionalInfoTitle6"] = 'Inner Pack Quantity'
            newRowObj["additionalInfoDescription6"] = "<p>" + key['Inner Pack Qty'] + "</p>"
            newRowObj["additionalInfoTitle7"] = 'Country Of Origin'
            newRowObj["additionalInfoDescription7"] = "<p>" + key['Country Of Origin'] + "</p>"
            newRowObj["additionalInfoTitle8"] = 'Standards'
            newRowObj["additionalInfoDescription8"] = standared
            newRowObj["customTextField1"] = ''
            newRowObj["customTextCharLimit1"] = ''
            newRowObj["customTextMandatory1"] = ''
            newRowObj["brand"] = ''

            finalData.append(newRowObj)

            if len(prodSizes) > 1:
                newRowObj = {}
                newRowObj['handleId'] = key['Style Code']
                newRowObj['fieldType'] = 'Variant'
                newRowObj['name'] = ''
                newRowObj['description'] = key['Description']
                newRowObj['productImageUrl'] = key['Image']
                newRowObj['price'] = ''
                newRowObj["surcharge"] = 0.0
                newRowObj['visible'] = 'TRUE'
                newRowObj['inventory'] = 'InStock'
                newRowObj['weight'] = key['Weight (KG)']
                newRowObj["collection"] = ''
                newRowObj["sku"] = key['Item']
                newRowObj["ribbon"] = ''
                newRowObj["discountMode"] = ''
                newRowObj["discountValue"] = ''
                newRowObj['productOptionName1'] = 'Size'
                newRowObj['productOptionType1'] = "DROP_DOWN"
                newRowObj['productOptionDescription1'] = key['Size']
                newRowObj['productOptionName2'] = 'Color'
                newRowObj['productOptionType2'] = "DROP_DOWN"
                newRowObj['productOptionDescription2'] = str(key['Colour']).strip()
                newRowObj["productOptionName3"] = ''
                newRowObj["productOptionType3"] = ''
                newRowObj["productOptionDescription3"] = ''
                newRowObj["productOptionName4"] = ''
                newRowObj["productOptionType4"] = ''
                newRowObj["productOptionDescription4"] = ''
                newRowObj["productOptionName5"] = ''
                newRowObj["productOptionType5"] = ''
                newRowObj["productOptionDescription5"] = ''
                newRowObj["productOptionName6"] = ''
                newRowObj["productOptionType6"] = ''
                newRowObj["productOptionDescription6"] = ''
                newRowObj["additionalInfoTitle1"] = 'Fit'
                newRowObj["additionalInfoDescription1"] = "<p>" + key['Fit'] + "</p>"
                newRowObj["additionalInfoTitle2"] = 'Length'
                newRowObj["additionalInfoDescription2"] = "<p>" + key['Length'] + "</p>"
                newRowObj["additionalInfoTitle3"] = 'Width'
                newRowObj["additionalInfoDescription3"] = "<p>" + key['Width'] + "</p>"
                newRowObj["additionalInfoTitle4"] = 'Height'
                newRowObj["additionalInfoDescription4"] = "<p>" + key['Height'] + "</p>"
                newRowObj["additionalInfoTitle5"] = 'Box Quantity'
                newRowObj["additionalInfoDescription5"] = "<p>" + key['Box Qty'] + "</p>"
                newRowObj["additionalInfoTitle6"] = 'Inner Pack Quantity'
                newRowObj["additionalInfoDescription6"] = "<p>" + key['Inner Pack Qty'] + "</p>"
                newRowObj["additionalInfoTitle7"] = 'Country Of Origin'
                newRowObj["additionalInfoDescription7"] = "<p>" + key['Country Of Origin'] + "</p>"
                newRowObj["additionalInfoTitle8"] = 'Standards'
                newRowObj["additionalInfoDescription8"] = standared
                newRowObj["customTextField1"] = ''
                newRowObj["customTextCharLimit1"] = ''
                newRowObj["customTextMandatory1"] = ''
                newRowObj["brand"] = ''

                finalData.append(newRowObj)
        else:
            newRowObj = {}
            newRowObj['handleId'] = key['Style Code']
            newRowObj['fieldType'] = 'Variant'
            newRowObj['name'] = ''
            newRowObj['description'] = key['Description']
            newRowObj['productImageUrl'] = key['Image']
            newRowObj['price'] = ''
            newRowObj["surcharge"] = 0.0
            newRowObj['visible'] = 'TRUE'
            newRowObj['inventory'] = 'InStock'
            newRowObj['weight'] = key['Weight (KG)']
            newRowObj["collection"] = ''
            newRowObj["sku"] = key['Item']
            newRowObj["ribbon"] = ''
            newRowObj["discountMode"] = ''
            newRowObj["discountValue"] = ''
            newRowObj['productOptionName1'] = 'Size'
            newRowObj['productOptionType1'] = "DROP_DOWN"
            newRowObj['productOptionDescription1'] = key['Size']
            newRowObj['productOptionName2'] = 'Color'
            newRowObj['productOptionType2'] = "DROP_DOWN"
            newRowObj['productOptionDescription2'] = str(key['Colour']).strip()
            newRowObj["productOptionName3"] = ''
            newRowObj["productOptionType3"] = ''
            newRowObj["productOptionDescription3"] = ''
            newRowObj["productOptionName4"] = ''
            newRowObj["productOptionType4"] = ''
            newRowObj["productOptionDescription4"] = ''
            newRowObj["productOptionName5"] = ''
            newRowObj["productOptionType5"] = ''
            newRowObj["productOptionDescription5"] = ''
            newRowObj["productOptionName6"] = ''
            newRowObj["productOptionType6"] = ''
            newRowObj["productOptionDescription6"] = ''
            newRowObj["additionalInfoTitle1"] = 'Fit'
            newRowObj["additionalInfoDescription1"] = "<p>" + key['Fit'] + "</p>"
            newRowObj["additionalInfoTitle2"] = 'Length'
            newRowObj["additionalInfoDescription2"] = "<p>" + key['Length'] + "</p>"
            newRowObj["additionalInfoTitle3"] = 'Width'
            newRowObj["additionalInfoDescription3"] = "<p>" + key['Width'] + "</p>"
            newRowObj["additionalInfoTitle4"] = 'Height'
            newRowObj["additionalInfoDescription4"] = "<p>" + key['Height'] + "</p>"
            newRowObj["additionalInfoTitle5"] = 'Box Quantity'
            newRowObj["additionalInfoDescription5"] = "<p>" + key['Box Qty'] + "</p>"
            newRowObj["additionalInfoTitle6"] = 'Inner Pack Quantity'
            newRowObj["additionalInfoDescription6"] = "<p>" + key['Inner Pack Qty'] + "</p>"
            newRowObj["additionalInfoTitle7"] = 'Country Of Origin'
            newRowObj["additionalInfoDescription7"] = "<p>" + key['Country Of Origin'] + "</p>"
            newRowObj["additionalInfoTitle8"] = 'Standards'
            newRowObj["additionalInfoDescription8"] = standared
            newRowObj["customTextField1"] = ''
            newRowObj["customTextCharLimit1"] = ''
            newRowObj["customTextMandatory1"] = ''
            newRowObj["brand"] = ''

            finalData.append(newRowObj)

    with open('new-json/final_data.json', 'w') as outfile:
        json.dump(finalData, outfile)

    return finalData


def dictionaryToCSV():
    finalCSVDictionary = generateNewCSVDictionary()

    csv_file = "new-files/final_data2.csv"

    csv_columns = ["handleId", "fieldType", "name", "description", "productImageUrl", "price", "surcharge", "visible",
                   "inventory", "weight", "collection", "sku", "ribbon", "discountMode", "discountValue",
                   "productOptionName1", "productOptionType1", "productOptionDescription1", "productOptionName2",
                   "productOptionType2", "productOptionDescription2", "productOptionName3", "productOptionType3",
                   "productOptionDescription3", "productOptionName4", "productOptionType4", "productOptionDescription4",
                   "productOptionName5", "productOptionType5", "productOptionDescription5", "productOptionName6",
                   "productOptionType6", "productOptionDescription6", "additionalInfoTitle1",
                   "additionalInfoDescription1", "additionalInfoTitle2", "additionalInfoDescription2",
                   "additionalInfoTitle3", "additionalInfoDescription3", "additionalInfoTitle4",
                   "additionalInfoDescription4", "additionalInfoTitle5", "additionalInfoDescription5",
                   "additionalInfoTitle6", "additionalInfoDescription6", "additionalInfoTitle7",
                   "additionalInfoDescription7", "additionalInfoTitle8", "additionalInfoDescription8",
                   "customTextField1", "customTextCharLimit1", "customTextMandatory1", "brand"]

    try:
        with open(csv_file, 'w', newline='', encoding="utf8") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
            writer.writeheader()
            for data in finalCSVDictionary[5146:]:
                writer.writerow(data)
    except IOError:
        print("I/O error")


dictionaryToCSV()


# Testing area:
# What to do?

#   {
#     "Style": "A001",
#     "b": "",
#     "c": "",
#     "d": "",
#     "e": "",
#     "f": "",
#     "g": "",
#     "h": "",
#     "i": "",
#     "j": "",
#     "k": "",
#     "l": "",
#     "": ""
#   },

# <ul>
#     <li>EN ISO 21420 Dexterity 3</li>
#     <li>EN388:2016 +A1:2018 - 4242X</li>
#     <li>EN 407 X2XXXX</li>
#     <li>EN 511 X2X</li>
#     <li>ANSI/ISEA 105: 2016 CUT Level A2</li>
# </ul>


# a = set(all_sizes)
# a.remove('')
# b = list(a)
# b.sort()
# print(b)

