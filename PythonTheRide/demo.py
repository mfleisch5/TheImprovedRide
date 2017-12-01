import os, pandas as pd, argparse, RoutingCalculator

parser = argparse.ArgumentParser()
parser.add_argument("infile")
parser.add_argument("num_locations")
args = parser.parse_args()

csvfile = args.infile
dir_path = os.path.dirname(os.path.realpath(__file__))
locations = args.num_locations

def csv_to_records(incsv):
    return [{"Anchor": trip['Anchor'],
             "RequestTime": trip['RequestTime'],
             "Companions": trip['Companions'],
             "PickHouseNumber": trip['PickHouseNumber'],
             "PickAddress1": trip['PickAddress1'],
             "Pickcity": trip['Pickcity'],
             "pickzip": trip['pickzip'],
             "DropHouseNumber": trip['DropHouseNumber'],
             "DropAddress1": trip['DropAddress1'],
             "Dropcity": trip['Dropcity'],
             "DropZip": trip['DropZip'],
             } for i, trip in pd.read_csv(incsv).iterrows()]


RoutingCalculator.main(csv_to_records(csvfile), os.path.join(dir_path, 'geocodes.json'),
                       os.path.join(dir_path,'failures.json'), int(locations))
