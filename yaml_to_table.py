import sys
from pathlib import Path
import oyaml as yaml
from prettytable import PrettyTable
import argparse

INPUT_YAML = "/home/polina/projects/tableForCurrencies/currencis.yaml"

in_file = Path(INPUT_YAML)
if not in_file.is_file():
    sys.exit("Input file [" + INPUT_YAML + "] does not exist")

SPACE_CHAR = ''

def listToString(inList):
    """Convert list to String"""
    ret = ""
    for line in inList:
        ret = ret + line
    return ret

def printDic(inDictionary, inPTable, indent):
    for item in inDictionary:
        if isinstance(item, dict):
            inPTable.add_row([SPACE_CHAR, SPACE_CHAR, SPACE_CHAR, SPACE_CHAR, SPACE_CHAR, SPACE_CHAR, SPACE_CHAR, ""])
            printDic(item, inPTable, indent)
        else:
            moreStuff = inDictionary.get(item)
            if isinstance(moreStuff, dict):
                inPTable.add_row([indent, SPACE_CHAR+SPACE_CHAR, SPACE_CHAR+SPACE_CHAR, SPACE_CHAR+SPACE_CHAR, SPACE_CHAR, ""])
                printDic(moreStuff, inPTable, SPACE_CHAR + SPACE_CHAR + SPACE_CHAR + SPACE_CHAR + SPACE_CHAR + SPACE_CHAR + SPACE_CHAR + indent)
            elif isinstance(moreStuff, list):
                
                for dicInDic in moreStuff:
                    if dicInDic is not None:
                        inPTable.add_row([])

with open(INPUT_YAML) as file:
    yaml_file_object = yaml.load(file, Loader=yaml.FullLoader)

    i = 0
    for key in yaml_file_object:
        body_st = []
        prettyTable = PrettyTable(["Code", "Exponent", "Iso4217", "Fiat", "Crypto", "Title", "Reference URL"])

        def print_dic_in_table(data):
            code = data.get("Code", "")
            exponent = data.get("Exponent", "")
            iso4217 = data.get("Iso4217", "")
            fiat = data.get("Fiat", "")
            crypto = data.get("Crypto", "")
            title = data.get("Title", "")
            reference_url = data.get("Reference URL", "")

            code = code if code is not None else ""
            exponent = exponent if exponent is not None else ""
            iso4217 = iso4217 if iso4217 is not None else ""
            fiat = fiat if fiat is not None else ""
            crypto = crypto if crypto is not None else ""
            title = title if title is not None else ""
            reference_url = reference_url if reference_url is not None else ""
    
            prettyTable.add_row([code, exponent, iso4217, fiat, crypto, title, reference_url])
            if (data.get == None):
                for dic in yaml_file_object:
                    print_dic_in_table("")

        if isinstance(yaml_file_object, list):
            for dic in yaml_file_object:
                if isinstance(dic, dict):
                    print_dic_in_table(dic)
        elif isinstance(yaml_file_object, dict):
            print_dic_in_table(yaml_file_object)
    
    table = prettyTable.get_string(attributes={"name": key, "id": key, "class": key, "style": "width: 1450px;table-layout: fixed;overflow-wrap: break-word;"})
    table = table.replace("+", "|")
    table_lines = table.split('\n')
    table_lines = table_lines[1:-1]
    table = '\n'.join(table_lines)
    body_st.append(table)
    print(listToString(body_st))