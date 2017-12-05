import pandas as pd, argparse
from routing import RoutingCalculator, tools

parser = argparse.ArgumentParser()
parser.add_argument("infile")
parser.add_argument("num_locations")
args = parser.parse_args()

csvfile = args.infile
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


RoutingCalculator.main(csv_to_records(csvfile), tools.geo_path, tools.fail_path, int(locations))
