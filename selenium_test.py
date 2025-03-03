import os
import webbrowser
import pyautogui
import time
import pyperclip


def paste_content(file_path):
    """Pastes content from a file into the current window."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    print(f"Pasting content from {file_path}:")
    print(content[:100])  # Print first 100 characters for verification

    pyperclip.copy(content)  # Copy content to clipboard

    clipboard_content = pyperclip.paste()
    print(f"Clipboard content: {clipboard_content[:100]}")  # Print first 100 characters

    pyautogui.hotkey("command", "v")  # Paste from clipboard


def main():
    """Main function to automate pasting content into a single Perplexity AI tab."""
    directory_path = "context_files"  # Path to your files

    # Ensure Brave Browser is focused
    print("Please focus Brave Browser and wait for 5 seconds...")
    # time.sleep(5)

    # Open Perplexity AI tab once
    url = "https://www.perplexity.ai/"
    webbrowser.open_new_tab(url)
    time.sleep(3)  # Wait for the tab to open

    # Filter and sort files
    files_to_paste = sorted(
        [
            filename
            for filename in os.listdir(directory_path)
            if filename.endswith(".txt") and filename[:-4].isdigit()
        ]
    )

    for filename in files_to_paste:
        file_path = os.path.join(directory_path, filename)
        paste_content(file_path)
        # time.sleep(1)  # Wait before pasting next file


if __name__ == "__main__":
    main()
