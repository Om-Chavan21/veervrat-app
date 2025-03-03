import tiktoken
import argparse
import os


def count_tokens_in_file(file_path, model="gpt-4"):
    """
    Reads data from a file and prints the token count based on the given model.

    Parameters:
    - file_path: Path to the file containing the text.
    - model: Name of the OpenAI model (default is "gpt-4").
    """
    try:
        # Load the appropriate encoding for the model
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print(f"Warning: Model '{model}' not found. Using 'cl100k_base' encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")

    try:
        # Read the file content
        with open(file_path, "r") as file:
            text_content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Encode the content to count tokens
    tokens = encoding.encode(text_content)

    # Output the number of tokens
    print(len(tokens))


def main():
    parser = argparse.ArgumentParser(
        description="Count tokens in a file using GPT-4 encoding."
    )
    parser.add_argument("file_path", type=str, help="Path to the file to analyze.")
    args = parser.parse_args()

    # Check if the path is absolute
    if not os.path.isabs(args.file_path):
        # If not, convert it to absolute path
        args.file_path = os.path.abspath(args.file_path)

    count_tokens_in_file(args.file_path)


if __name__ == "__main__":
    main()
