# 🏎️ Ferrari Car Chatbot

A RAG (Retrieval-Augmented Generation) chatbot that answers questions about Ferrari cars — built by scraping Wikipedia data, converting it into searchable embeddings, and using an LLM to generate natural answers.

## 🔗 Live Demo

https://niteash-patel-ferrari-chatbot-app-moacqd.streamlit.app

## Features

- Ask about any Ferrari model — from the 1940s to the latest releases
- Answers are grounded in scraped Wikipedia data (not just the model's general knowledge)
- Shows the car's image alongside the answer
- Simple, styled Streamlit chat interface

## How It Works

1. **Data Scraping** — Ferrari car data (names, summaries, images) is scraped from Wikipedia using `requests` and `BeautifulSoup`.
2. **Data Cleaning** — Missing entries and non-car pages (engines, films, etc.) are filtered out.
3. **Embeddings** — Each car's summary is converted into a vector using `sentence-transformers` (`all-MiniLM-L6-v2`).
4. **Vector Search** — Embeddings are stored in a Chroma vector database for fast semantic search.
5. **RAG Pipeline** — When a user asks a question, the most relevant car summaries are retrieved and passed to an LLM, which generates a natural-language answer grounded in that data.

## Tech Stack

- **Frontend:** Streamlit
- **Scraping:** `requests`, `beautifulsoup4`
- **Embeddings:** `sentence-transformers`
- **Vector DB:** `chromadb`
- **LLM:** NVIDIA NIM (via OpenAI-compatible API)

## Project Structure

```
ferrari-chatbot/
├── app.py                      # Streamlit app (main entry point)
├── ferrari_data_collector.py   # Scrapes Ferrari car data from Wikipedia
├── add_years.py                # Extracts/adds launch year to each car
├── ferrari_data.json           # Scraped and cleaned car data
├── ferrari_embeddings.npy      # Precomputed embeddings for each car summary
├── requirements.txt            # Python dependencies
├── .env                        # API keys (not committed to GitHub)
└── .gitignore
```

## Setup (Run Locally)

1. Clone the repository
   ```
   git clone https://github.com/niteash-patel/ferrari-chatbot.git
   cd ferrari-chatbot
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API key
   ```
   NVIDIA_API_KEY=your-key-here
   ```

4. Run the app
   ```
   streamlit run app.py
   ```

## Deployment

Deployed on **Streamlit Community Cloud**. The API key is stored securely using Streamlit's **Secrets** manager (not committed to the repo).

## Data Source

Car data is scraped from [Wikipedia's List of Ferrari road cars](https://en.wikipedia.org/wiki/List_of_Ferrari_road_cars) and individual car pages, via Wikipedia's public REST API.

## Known Limitations

- Generic queries like "latest Ferrari" can sometimes be inaccurate, since semantic search prioritizes meaning over exact recency.
- A few cars are missing images or summaries where Wikipedia's data was incomplete.
- The chatbot's knowledge is limited to what was scraped at collection time — it won't know about cars released after that.

## License

This project is for educational purposes. Ferrari and related trademarks belong to their respective owners.
