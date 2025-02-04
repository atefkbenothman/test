def read_write_file(input_path, output_path):
    """
    Reads contents from input file and writes to output file.
    
    Args:
        input_path (str): Path to the input file
        output_path (str): Path to the output file
    
    Returns:
        bool: True if operation was successful, False otherwise
    """
    try:
        # Open and read the input file
        with open(input_path, 'r') as input_file:
            file_content = input_file.read()
        
        # Write contents to output file
        with open(output_path, 'w') as output_file:
            output_file.write(file_content)
        
        return True
    
    except FileNotFoundError:
        print(f"Input file {input_path} not found.")
        return False
    except IOError:
        print(f"An error occurred while reading/writing files.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

# Example usage:
# if __name__ == "__main__":
#     success = read_write_file('source.txt', 'destination.txt')
#     print(f"File operation successful: {success}")