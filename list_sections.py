import os
import re
import json
from pathlib import Path

def read_numbers_from_file(file_path):
    """Read numbers from a file, one per line."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def find_matching_files(folder_path, number):
    """Find files in the folder that contain the number in their filename."""
    matches = []
    for file in os.listdir(folder_path):
        if number in file:
            matches.append(os.path.join(folder_path, file))
    return matches

def extract_section_content(file_content, section_name):
    """Extract content for a specific section from file content."""
    pattern = r'\(\(<\(\(##<## ' + re.escape(section_name) + r' ##>##\)\)>\)\)(.*?)(?=\(\(<\(\(##<##|\Z)'
    match = re.search(pattern, file_content, re.DOTALL)
    if match:
        # Return content, stripping leading/trailing whitespace
        return match.group(1).strip()
    return None

def process_file(file_path):
    """Process a file to extract specified sections."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    sections = {
        'Issue Number': extract_section_content(content, 'Issue Number'),
        'InventoryId': extract_section_content(content, 'InventoryId'),
        'License Type': extract_section_content(content, 'License Type'),
        'Name': extract_section_content(content, 'Name'),
        'Notes': extract_section_content(content, 'Notes')
    }
    
    return sections

def main():
    # Paths
    current_dir = Path('.')
    file_y_path = current_dir / 'fileY'
    folder_x_path = current_dir / 'folderX'
    
    # Check if paths exist
    if not file_y_path.exists():
        print(f"Error: fileY not found at {file_y_path.absolute()}")
        return
    
    if not folder_x_path.exists() or not folder_x_path.is_dir():
        print(f"Error: folderX not found at {folder_x_path.absolute()}")
        return
    
    # Read numbers from fileY
    numbers = read_numbers_from_file(file_y_path)
    
    # Initialize results list for JSON output
    results = []
    
    # Process each number
    for number in numbers:
        matching_files = find_matching_files(folder_x_path, number)
        
        if matching_files:
            for file_path in matching_files:
                print(f"\nFound match for number {number} in file: {os.path.basename(file_path)}")
                
                # Extract sections
                sections = process_file(file_path)
                
                # Print to screen
                print(f"Matched Number: {number}")
                print(f"InventoryId: {sections['InventoryId']}")
                print(f"Issue Number: {sections['Issue Number']}")
                print(f"License Type: {sections['License Type']}")
                print(f"Name: {sections['Name']}")
                print(f"Notes: {sections['Notes']}")
                
                # Add to results list
                result = {
                    'matched_number': number,
                    'file_name': os.path.basename(file_path),
                    'InventoryId': sections['InventoryId'],
                    'Issue Number': sections['Issue Number'],
                    'License Type': sections['License Type'],
                    'Name': sections['Name'],
                    'Notes': sections['Notes']
                }
                results.append(result)
        else:
            print(f"No matches found for number: {number}")
    
    # Write results to JSON file
    output_file = current_dir / 'results.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)
    
    print(f"\nResults have been saved to {output_file.absolute()}")

if __name__ == "__main__":
    main()
