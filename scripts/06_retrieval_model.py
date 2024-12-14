from flask import Flask, request, render_template
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, ID, NUMERIC, BOOLEAN
from whoosh.qparser import QueryParser
import os
import json

# Initialize Flask app
app = Flask(__name__, template_folder="templates")

# Define Whoosh schema
schema = Schema(
    video_id=ID(stored=True),
    title=TEXT(stored=True),
    channel_title=TEXT(stored=True),
    category_label=TEXT(stored=True),
    profanity=BOOLEAN(stored=True),
    themes=BOOLEAN(stored=True),
    readability=BOOLEAN(stored=True),
    tone=BOOLEAN(stored=True),
    cultural_sensitivity=BOOLEAN(stored=True),
    kids_safe_content=BOOLEAN(stored=True),
    tone_score=NUMERIC(stored=True, numtype=float),
    profanity_words=TEXT(stored=True), 
    themes_identified=TEXT(stored=True), 
)

# Function to load JSON data
def load_data(json_file):
    with open(json_file, "r") as f:
        return json.load(f)

# Indexing function
def create_search_index(data, index_dir="../indexdir"):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    ix = create_in(index_dir, schema)
    writer = ix.writer()
    for video in data:
        # Ensure profanity_words and themes_identified are always lists, even if they are None
        profanity_words = video.get("profanity_words", [])
        if profanity_words is None:
            profanity_words = []
        
        themes_identified = video.get("themes_identified", [])
        if themes_identified is None:
            themes_identified = []
        
        writer.add_document(
            video_id=video.get("video_id", ""),
            title=video.get("title", ""),
            channel_title=video.get("channel_title", ""),
            category_label=video.get("category_label", ""),
            profanity=video.get("profanity", False),
            themes=video.get("themes", False),
            readability=video.get("readability", False),
            tone=video.get("tone", False),
            cultural_sensitivity=video.get("cultural_sensitivity", False),
            kids_safe_content=video.get("kids_safe_content", False),
            tone_score=video.get("tone_score", 0.0),
            profanity_words=" ".join(profanity_words),  # Safely join the list
            themes_identified=" ".join(themes_identified),  # Safely join the list
        )
    writer.commit()


# Load JSON data and create index (adjust path as necessary)
filtered_videos = load_data("../data/raw/youtube_traffic_2024-12-13_14-32-24.json")
create_search_index(filtered_videos)

from whoosh.qparser import MultifieldParser

@app.route("/", methods=["GET", "POST"])
def search():
    query_term = request.form.get("query", "")
    results = []
    if query_term:
        ix = open_dir("../indexdir")
        with ix.searcher() as searcher:
            # Use MultifieldParser to search both 'title' and 'profanity_words' fields
            parser = MultifieldParser(["title", "profanity_words"], schema=ix.schema)
            query = parser.parse(query_term)  # Parse the query term
            search_results = searcher.search(query, limit=10)
            for hit in search_results:
                results.append({
                    "video_id": hit["video_id"],
                    "title": hit["title"],
                    "channel_title": hit["channel_title"],
                    "category_label": hit["category_label"],
                })
    return render_template("search.html", query=query_term, results=results)



if __name__ == "__main__":
    app.run(port=5001)
