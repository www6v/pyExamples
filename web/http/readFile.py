

def read_file_to_string(file_path: str) -> str:
    """
    Read the contents of a file and return it as a string.

    Args:
        file_path (str): Path to the file to read.

    Returns:
        str: The contents of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        raise

# Example usage
if __name__ == "__main__":
    file_path = "/Users/wei.wang/workspace/pyExamples/web/http/danone_post.tpl"
    file_content = read_file_to_string(file_path)
    print(file_content)
