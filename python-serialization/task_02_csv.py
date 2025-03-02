import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert csv to json
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            read_csv = csv.DictReader(csv_file)
            data = [row for row in read_csv]
            
            data_json = json.dumps(data, indent=4)
            
            with open('data.json', mode='w') as j_file:
                j_file.write(data_json)
                
            return (True)
        
    except FileNotFoundError:
        print(f"Error: No hemos encontrado el archiv {csv_filename}.")
        return False
    except Exception as e:
        print(f"Error indeseado e inesperado: {e}")
        return (False)