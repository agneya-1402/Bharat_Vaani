import os
import requests
from flask import Flask, render_template, request
from google import genai
from crawl4ai import WebCrawler 
import markdown

app = Flask(__name__)

# API 
GEMINI_API_KEY = "KEY"  
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY
client = genai.Client(api_key=GEMINI_API_KEY)

# Scraping (knowledge base)
URL_LIST = [
    "http://www.maharashtra.gov.in/Site/1560/General%20Information",
    "http://www.maharashtra.gov.in/",
    "http://www.maharashtra.gov.in/Site/1604/scheme",
    "http://www.maharashtra.gov.in/Site/1566/Health%20and%20Wellness",
]
# Store
SCRAPED_DATA = {}

def do_scraping():
    crawler = WebCrawler()
    for link in URL_LIST:
        try:
            text_content = crawler.scrape(link)
            SCRAPED_DATA[link] = text_content
        except Exception as e:
            SCRAPED_DATA[link] = f"Error scraping {link}: {str(e)}"


# Searches the scraped data
# Returns 500 chr
def find_relevant_context(query: str) -> str:
    query_words = set(query.lower().split())
    for link, text in SCRAPED_DATA.items():
        if isinstance(text, str) and any(word in text.lower() for word in query_words):
            return text[:500]
    return "No relevant context found from the scraped data."


# AI output (Markdown)
def gemini_rag_answer(user_query: str) -> str:
    context = find_relevant_context(user_query)
    chat = client.chats.create(model="gemini-2.0-flash") 
    prompt = (
        f"Context:\n{context}\n\n"
        f"User question:\n{user_query}\n\n"
        "Please provide a concise and helpful answer in Markdown, referencing the context if relevant."
    )
    try:
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"

@app.route("/scrape")
def scrape():
    do_scraping()
    return "Scraping completed. Knowledge base updated."

@app.route("/", methods=["GET", "POST"])

# Sidebar 
def index(): 
    how_to_use = [
        "Type your query or click the voice button to speak.",
        "Ask about Indian government topics (tax, laws, schemes, constitution, exams, banks, etc.).",
        "The AI will provide concise, context-informed answers.",
        "Voice input supports all languages.",
        "Each submission clears previous conversation history."
    ]
    
    user_query = ""
    answer_md = ""
    
    if request.method == "POST":
        user_query = request.form.get("query", "")
        if user_query:
            answer_md = gemini_rag_answer(user_query)
            answer_html = markdown.markdown(answer_md)
        else:
            answer_html = ""
    else:
        answer_html = ""
    
    return render_template(
        "index.html",
        user_query=user_query,
        answer=answer_html,
        how_to_use=how_to_use
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
