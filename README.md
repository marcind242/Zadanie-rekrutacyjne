# HTML Article Generation Application with OpenAI API

## Description
This Python application takes article content from a text file and then uses the OpenAI API to transform it into HTML code following specific guidelines (e.g., adding placeholders for images and corresponding captions). The generated HTML article is saved in the `artykul.html` file, which can then be displayed using the `szablon.html` template or directly in `podglad.html`.

The application consists of:
- **A Python file** (`zadanie.py`) that connects to the OpenAI API and generates HTML code for the article.
- **An HTML template file** (`szablon.html`) that contains styling and is ready for content insertion.
- **A preview HTML file** (`podglad.html`) that contains the full article in the HTML template for direct preview.

## Requirements
- Python 3.7 or later
- OpenAI API key
- Installed `openai` library

## Installation Instructions

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/marcind242/Zadanie-rekrutacyjne
    cd Zadanie-rekrutacyjne
    ```

2. **Install dependencies** using `pip`:
    ```bash
    pip install openai
    ```

3. **Add your OpenAI API key** to the `zadanie.py` file:
    ```python
    openai.api_key = 'YOUR_API_KEY'
    ```

4. Ensure that the text file `tresc artykulu.txt` is in the same directory as the script and contains the content you want to convert to HTML.

## Running Instructions

1. **Run the Python script** to generate the HTML article code:
    ```bash
    python zadanie.py
    ```

2. After running the script:
   - The generated HTML article will be saved in the `artykul.html` file.
   - The `szablon.html` file is an empty template, ready for content insertion.
   - The `podglad.html` file provides a complete visualization of the generated article.

## Application Workflow

1. The Python script (`zadanie.py`) reads the article content from the `tresc artykulu.txt` file.
2. It sends a request to the OpenAI API, which converts the article to HTML.
3. It generates HTML code with placeholders for images and captions and then saves it to the `artykul.html` file.
4. The `artykul.html` file is ready for direct viewing or can be copied into `szablon.html` to view with the correct styling.
