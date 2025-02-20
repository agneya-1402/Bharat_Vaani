# Bharat Vaani 🇮🇳

Bharat Vaani is an AI-powered chat assistant built with Flask that helps users ask questions about Indian government topics such as tax laws, schemes, constitutional details, exams, and banks. It uses a Retrieval-Augmented Generation (RAG) approach by scraping knowledge from government websites (using [crawl4ai](https://github.com/unclecode/crawl4ai)) and feeding relevant context along with user queries into Google's Gemini API. The application also supports voice input via the Web Speech API with Marathi language support.

## Features

- **RAG-Based Chatbot:**  
  Combines scraped data from specified websites with user queries to generate context-informed answers using the Gemini API.

- **Web Scraping with crawl4ai:**  
  Scrapes content from a configurable list of URLs to build an in-memory knowledge base.

- **Voice Input:**  
  Provides a microphone button that uses the Web Speech API to capture the user's voice (supports Marathi). Recording lasts for up to 10 minutes or until the button is clicked again, with the transcribed text automatically filled into the query box.

- **Markdown Output Rendering:**  
  The Gemini API returns answers in Markdown, which are rendered as HTML on the UI.

- **Custom UI:**  
  A responsive UI built using HTML/CSS (with Flask templates) featuring:
  - A left sidebar with branding (Emblem of India alongside "Bharat Vaani") and usage instructions (as bullet points describing how to use the AI and its capabilities).
  - A top input area with reduced-width text input, a voice input (microphone) button, and a submit button aligned inline.
  - Chat output (questions and answers) displayed beneath the input area in a chat bubble style.

## Prerequisites

- Python 3.7+
- [Flask](https://flask.palletsprojects.com/)
- [google-genai](https://pypi.org/project/google-genai/)
- [crawl4ai](https://github.com/unclecode/crawl4ai) (install from PyPI or source)
- [requests](https://pypi.org/project/requests/)


## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/agneya-1402/bharat-vaani.git
   cd bharat-vaani
   ```
   

2. **Install Libariaries:**

```python 
Flask
google-genai
requests
crawl4ai
```


## Scrape Knowledge Base:
Before running the main app, populate your in-memory knowledge base by accessing the /scrape endpoint in your browser:

```bash

http://localhost:5000/scrape
```
This will use crawl4ai to scrape the URLs defined in the URL_LIST.

## Run the Flask App:

### Start the Flask application by running:

```bash
python app.py
The app will be available at http://localhost:5000
```

## Using the Chat Interface:

### Input Area:
At the top of the main content area, enter your query in the text box. Alternatively, click the microphone icon to activate voice input. The app will capture your speech (with Marathi support), transcribe it using the Web Speech API, and place the transcribed text into the input box.

### Submission:
Click the SUBMIT button to send your query. Each submission clears the previous conversation history.

### View the Answer:
The answer, rendered from Markdown to HTML, is displayed in a chat bubble beneath the input area.

## Project Structure

```markdown

bharat-vaani/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

app.py:
Contains the Flask application, routes, and backend logic for scraping, context retrieval, and querying the Gemini API.

templates/index.html:
The HTML template that defines the UI, including the left sidebar (branding and instructions) and the main content area (input and chat output).

## Customization
* Knowledge Base:
Update the URL_LIST variable in app.py to scrape additional websites.

* UI Styling:
Modify templates/index.html to adjust the layout, colors, fonts, or any other styling elements to better match your desired design.

* Advanced RAG:
For a more robust retrieval-augmented generation approach, consider integrating embeddings-based search and a vector database for improved context retrieval.

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.

## Acknowledgements

* Google Gemini API
* crawl4ai
* Flask
* NewsAPI
