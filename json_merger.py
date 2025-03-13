import json
import sys

def merge_json_files(first_json_file, second_json_file, output_file):
    """
    Merge contents of the first JSON file into the second JSON file when a matching number is found.
    For each match, add the copyright information directly to the second JSON objects.
    
    Args:
        first_json_file (str): Path to the first JSON file with numbers as keys
        second_json_file (str): Path to the second JSON file with matched_number fields
        output_file (str): Path to save the merged JSON output
    """
    try:
        # Load the first JSON file (with numbers as keys)
        with open(first_json_file, 'r') as f1:
            first_json = json.load(f1)
        
        # Load the second JSON file (list of objects with matched_number)
        with open(second_json_file, 'r') as f2:
            second_json = json.load(f2)
        
        # Merge the data
        for item in second_json:
            matched_number = item.get('matched_number')
            if matched_number in first_json:
                # Add the copyright data from the first JSON to the matching item in the second JSON
                item['copyright'] = first_json[matched_number]
        
        # Save the merged result to the output file
        with open(output_file, 'w') as out_file:
            json.dump(second_json, out_file, indent=2)
        
        print(f"Successfully merged JSON files. Result saved to {output_file}")
        return second_json
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_json.py <first_json_file> <second_json_file> <output_file>")
        sys.exit(1)
    
    first_json_file = sys.argv[1]
    second_json_file = sys.argv[2]
    output_file = sys.argv[3]
    
    merge_json_files(first_json_file, second_json_file, output_file)
