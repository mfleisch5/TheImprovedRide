import pandas

GOOGLEKEY = "AIzaSyBF3pvalcQ0fdP9FjdPjTiL2T4YQMnvHps"
data = pandas.read_csv('../Data.csv')
data['PickFullAddress'] = data['PickHouseNumber'].astype(str) + " " + data['PickAddress1'] + ", " + data['Pickcity'] + \
                          ", " + data['pickzip'].astype(str)
data['DropFullAddress'] = data['DropHouseNumber'].astype(str) + " " + data['DropAddress1'] + ", " + data['Dropcity'] + \
                      ", " + data['DropZip'].astype(str)


print(*data['DropFullAddress'], sep='\n')

