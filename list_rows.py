import json

def find_copyrights_with_keyword(file_path, keyword):
    # Load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Dictionary to store rows with matching copyrights
    matching_rows = {}
    
    # Iterate through the data
    for row_number, copyright_list in data.items():
        matching_copyrights = []
        
        # Check each copyright in the list for the keyword
        for copyright_text in copyright_list:
            if keyword.lower() in copyright_text.lower():
                matching_copyrights.append(copyright_text)
        
        # If we found any matches in this row, add to our results
        if matching_copyrights:
            matching_rows[row_number] = matching_copyrights
    
    return matching_rows

def main():
    # File path to the JSON file
    file_path = 'data.json'
    
    # Keyword to search for
    keyword = 'vol ag'
    
    try:
        # Find matching rows
        results = find_copyrights_with_keyword(file_path, keyword)
        
        # Display the results
        if results:
            print(f"Found {len(results)} rows with copyrights containing '{keyword}':")
            for row_number, copyrights in results.items():
                print(f"\nRow {row_number}:")
                for i, copyright_text in enumerate(copyrights, 1):
                    print(f"  {i}. {copyright_text}")
        else:
            print(f"No copyrights containing '{keyword}' were found.")
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
