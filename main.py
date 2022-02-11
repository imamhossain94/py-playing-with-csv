import csv
import json


def buildDescription(keys):
    description = []
    for k in keys:
        if k in ['Style', 'Carton_Qty', 'Size', 'Price', 'Colour', 'Fit', 'Length', 'Width', 'Height', 'Weight(Kg)']:
            description.append(str(k).strip() + (' : ' if k == 'Weight(Kg)' else '-') + str(keys[k]).strip())
    return ','.join(description)


def saveJson():
    with open('client_json_data.json', 'w') as outfile:
        json.dump(myDict1, outfile)
    with open('wix_json_data.json', 'w') as outfile:
        json.dump(myDict2, outfile)
    with open('client2_json_data.json', 'w') as outfile:
        json.dump(myDict3, outfile)


def read_csv(filename):
    with open(filename) as f:
        file_data = csv.reader(f)
        headers = next(file_data)
        return [dict(zip(headers, i)) for i in file_data]


myDict1 = read_csv("files/1-client-csv.csv")
myDict2 = read_csv("files/Wix_Templates_Products_CSV (1).csv")
myDict3 = read_csv("files/2-client-csv.csv")


# saveJson()


def getProductsSize(dict, flag):
    filtered = []
    pdo1 = []
    for x in dict:
        if x['Style'] == flag:
            filtered.append(x)

    for filter in filtered:
        pdo1.append(str(filter['Size']).strip())

    return pdo1


def getProductsColor(dict, flag):
    filtered = []
    pdo1 = []
    for x in dict:
        if x['Style'] == flag:
            filtered.append(x)

    for filter in filtered:
        pdo1.append(str(filter['Colour']).strip())

    return pdo1


def generateNewCSVDictionary():
    finalData = []
    productFlag = ""
    for key in myDict1:

        if productFlag != key['Style']:
            productFlag = key['Style']

            newRowObj = {}

            prodSizes = getProductsSize(dict=myDict1, flag=key['Style'])
            prodColours = getProductsColor(dict=myDict1, flag=key['Style'])

            collections = ''
            for mKey in myDict3:
                if mKey['Style'] == key['Style']:
                    collections = mKey['ProductRange'] + ';' + mKey['ProductGroup']

            newRowObj['handleId'] = key['Style']
            newRowObj['fieldType'] = 'Product'
            newRowObj['name'] = key['Style'] + '-' + key['Desc']
            newRowObj['description'] = buildDescription(key)
            newRowObj['productImageUrl'] = key['Image_Path']
            newRowObj['price'] = float(key['Price'])*2 if key['Price'] else 0.0
            newRowObj["surcharge"] = 0.0
            newRowObj['visible'] = 'TRUE'
            newRowObj['inventory'] = 'InStock'
            newRowObj['weight'] = key['Weight(Kg)']
            newRowObj['productOptionName1'] = 'Size'
            newRowObj['productOptionType1'] = "DROP_DOWN"
            newRowObj['productOptionDescription1'] = ';'.join(set(prodSizes))
            newRowObj['productOptionName2'] = 'Color'
            newRowObj['productOptionType2'] = "DROP_DOWN"
            newRowObj['productOptionDescription2'] = ';'.join(set(prodColours))
            newRowObj["collection"] = collections
            newRowObj["sku"] = ''
            newRowObj["ribbon"] = ''
            newRowObj["discountMode"] = ''
            newRowObj["discountValue"] = ''
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
            newRowObj["additionalInfoTitle1"] = ''
            newRowObj["additionalInfoDescription1"] = ''
            newRowObj["additionalInfoTitle2"] = ''
            newRowObj["additionalInfoDescription2"] = ''
            newRowObj["additionalInfoTitle3"] = ''
            newRowObj["additionalInfoDescription3"] = ''
            newRowObj["additionalInfoTitle4"] = ''
            newRowObj["additionalInfoDescription4"] = ''
            newRowObj["additionalInfoTitle5"] = ''
            newRowObj["additionalInfoDescription5"] = ''
            newRowObj["additionalInfoTitle6"] = ''
            newRowObj["additionalInfoDescription6"] = ''
            newRowObj["customTextField1"] = ''
            newRowObj["customTextCharLimit1"] = ''
            newRowObj["customTextMandatory1"] = ''
            newRowObj["brand"] = ''

            finalData.append(newRowObj)

            if len(prodSizes) > 1:
                newRowObj = {}
                newRowObj['handleId'] = key['Style']
                newRowObj['fieldType'] = 'Variant'
                newRowObj['name'] = ''
                newRowObj['description'] = buildDescription(key)
                newRowObj['productImageUrl'] = key['Image_Path']
                newRowObj['price'] = ''
                newRowObj["surcharge"] = 0.0
                newRowObj['visible'] = 'TRUE'
                newRowObj['inventory'] = 'InStock'
                newRowObj['weight'] = key['Weight(Kg)']
                newRowObj['productOptionName1'] = 'Size'
                newRowObj['productOptionType1'] = "DROP_DOWN"
                newRowObj['productOptionDescription1'] = key['Size']
                newRowObj['productOptionName2'] = 'Color'
                newRowObj['productOptionType2'] = "DROP_DOWN"
                newRowObj['productOptionDescription2'] = str(key['Colour']).strip()
                newRowObj["collection"] = ''
                newRowObj["sku"] = ''
                newRowObj["ribbon"] = ''
                newRowObj["discountMode"] = ''
                newRowObj["discountValue"] = ''
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
                newRowObj["additionalInfoTitle1"] = ''
                newRowObj["additionalInfoDescription1"] = ''
                newRowObj["additionalInfoTitle2"] = ''
                newRowObj["additionalInfoDescription2"] = ''
                newRowObj["additionalInfoTitle3"] = ''
                newRowObj["additionalInfoDescription3"] = ''
                newRowObj["additionalInfoTitle4"] = ''
                newRowObj["additionalInfoDescription4"] = ''
                newRowObj["additionalInfoTitle5"] = ''
                newRowObj["additionalInfoDescription5"] = ''
                newRowObj["additionalInfoTitle6"] = ''
                newRowObj["additionalInfoDescription6"] = ''
                newRowObj["customTextField1"] = ''
                newRowObj["customTextCharLimit1"] = ''
                newRowObj["customTextMandatory1"] = ''
                newRowObj["brand"] = ''
                finalData.append(newRowObj)
        else:
            newRowObj = {}
            newRowObj['handleId'] = key['Style']
            newRowObj['fieldType'] = 'Variant'
            newRowObj['name'] = ''
            newRowObj['description'] = buildDescription(key)
            newRowObj['productImageUrl'] = key['Image_Path']
            newRowObj['price'] = ''
            newRowObj["surcharge"] = 0.0
            newRowObj['visible'] = 'TRUE'
            newRowObj['inventory'] = 'InStock'
            newRowObj['weight'] = key['Weight(Kg)']
            newRowObj['productOptionName1'] = 'Size'
            newRowObj['productOptionType1'] = "DROP_DOWN"
            newRowObj['productOptionDescription1'] = key['Size']
            newRowObj['productOptionName2'] = 'Color'
            newRowObj['productOptionType2'] = "DROP_DOWN"
            newRowObj['productOptionDescription2'] = str(key['Colour']).strip()
            newRowObj["collection"] = ''
            newRowObj["sku"] = ''
            newRowObj["ribbon"] = ''
            newRowObj["discountMode"] = ''
            newRowObj["discountValue"] = ''
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
            newRowObj["additionalInfoTitle1"] = ''
            newRowObj["additionalInfoDescription1"] = ''
            newRowObj["additionalInfoTitle2"] = ''
            newRowObj["additionalInfoDescription2"] = ''
            newRowObj["additionalInfoTitle3"] = ''
            newRowObj["additionalInfoDescription3"] = ''
            newRowObj["additionalInfoTitle4"] = ''
            newRowObj["additionalInfoDescription4"] = ''
            newRowObj["additionalInfoTitle5"] = ''
            newRowObj["additionalInfoDescription5"] = ''
            newRowObj["additionalInfoTitle6"] = ''
            newRowObj["additionalInfoDescription6"] = ''
            newRowObj["customTextField1"] = ''
            newRowObj["customTextCharLimit1"] = ''
            newRowObj["customTextMandatory1"] = ''
            newRowObj["brand"] = ''

            finalData.append(newRowObj)

    with open('final_json_data.json', 'w') as outfile:
        json.dump(finalData, outfile)

    return finalData


def dictionaryToCSV():
    finalCSVDictionary = generateNewCSVDictionary()

    csv_file = "files/final_csv_data.csv"

    csv_columns = ["handleId", "fieldType", "name", "description", "productImageUrl", "price", "visible", "inventory",
                   "weight", "productOptionName1", "productOptionType1", "productOptionDescription1",
                   "productOptionName2", "productOptionType2", "productOptionDescription2", "collection", "sku",
                   "ribbon", "surcharge", "discountMode", "discountValue", "productOptionName3", "productOptionType3",
                   "productOptionDescription3", "productOptionName4", "productOptionType4", "productOptionDescription4",
                   "productOptionName5", "productOptionType5", "productOptionDescription5", "productOptionName6",
                   "productOptionType6", "productOptionDescription6", "additionalInfoTitle1",
                   "additionalInfoDescription1", "additionalInfoTitle2", "additionalInfoDescription2",
                   "additionalInfoTitle3", "additionalInfoDescription3", "additionalInfoTitle4",
                   "additionalInfoDescription4", "additionalInfoTitle5", "additionalInfoDescription5",
                   "additionalInfoTitle6", "additionalInfoDescription6", "customTextField1", "customTextCharLimit1",
                   "customTextMandatory1", "brand"]

    try:
        with open(csv_file, 'w') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
            writer.writeheader()
            for data in finalCSVDictionary:
                writer.writerow(data)
    except IOError:
        print("I/O error")


# def removeRedundentRows():
#     pqr = ['B027', 'PS11', 'B013', 'HB10', 'T601', 'B029', 'PS12', 'HA16', 'PS89', 'PW47', 'PW01', 'HV55', 'CV03', 'PW02', 'PW13', 'PW38', 'CV04', 'B028', 'PW33', 'PS53', 'PS56', 'PW11', 'B023', 'PS50', 'PW52', 'C701', 'PW15', 'PW14', 'PV60', 'PS54', 'PV64', 'PW32', 'HA20', 'CS20', 'HA10']


dictionaryToCSV()
