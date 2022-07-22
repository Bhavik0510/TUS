import csv

with open('sales_order_sheet_read_csv.csv','r') as file:
    read_file = csv.DictReader(file)
    # for i in read_file:
    #     print(i['Order Reference'],i['Total'],i['Untaxed Amount'],i['Status'])
    totalv = []
    untax = []
    tax_data = []
    for i in read_file:
        if i['Status'] == 'Sales Order':
            print({i['Order Reference'],i['Status']})

        if i['Total'] >= i['Untaxed Amount']:
            totalv.append(i['Total'])
            untax.append(i['Untaxed Amount'])
    # print(totalv)
    # print(untax)
        taxtotal = list(zip(totalv,untax))
        print(taxtotal)

    # print(taxtotal[0])
    #     A=int(taxtotal[i][0])
    #     B=int(taxtotal[i][1])
        C = int(taxtotal[i][0]) - int(taxtotal[i][1])
    # print(A-B)
        print({i['Customer'],taxtotal[C]})



    # for i , j in (totalv,untax):
    #     i[tax] = totalv[i] - untax[j]
    #     tax_data.append(i[tax])


    # print(tax_data)
    #     if i['Total'] >= i['Untaxed Amount']:
    #         i[tax] = i['Total'] - i['Untaxed Amount']
    #         print(i[tax])
    # #         tax_data.append(tax)
    # # print(tax_data)
