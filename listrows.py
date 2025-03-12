import json
import sys

def find_numbers_with_keyword(data, keywords):
    """
    Find all numbers where at least one associated copyright statement contains any of the keywords.
    
    Args:
        data (dict): JSON data mapping numbers to list of copyright statements
        keywords (list): List of keywords to search for
        
    Returns:
        list: List of numbers with matching copyright statements
    """
    matching_numbers = []
    
    for number, copyright_statements in data.items():
        for statement in copyright_statements:
            if any(keyword in statement for keyword in keywords):
                matching_numbers.append(number)
                break  # Once we find one match, we can move to the next number
                
    return matching_numbers

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <json_file> <keyword1> [keyword2] [keyword3] ...")
        sys.exit(1)
        
    json_file = sys.argv[1]
    keywords = sys.argv[2:]
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{json_file}' is not a valid JSON file.")
        sys.exit(1)
        
    matching_numbers = find_numbers_with_keyword(data, keywords)
    
    if matching_numbers:
        print("Numbers that contain at least one matching copyright statement:")
        for number in matching_numbers:
            print(number)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
