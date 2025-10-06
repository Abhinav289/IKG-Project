import os
import json
import requests
import pandas as pd
from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich.prompt import Prompt

load_dotenv()
console = Console()

url = "https://api.twitterapi.io/twitter/tweet/advanced_search"
headers = {"X-API-Key": os.getenv("API_KEY")}
query = "\"diffusion\" OR \"image generation\" OR \"text to image\" lang:en from:HuggingPapers"
cursor = ""
count = 1
rows = []

while True:

    console.rule(f"[bold green] Round {count} [/bold green]")

    params = {
        "query": query,
        "queryType": "Top",
        "cursor": cursor
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        console.print(f"[bold red]Error {response.status_code}: {response.text}[/bold red]")
        break

    try:
        data = response.json()
    except Exception as e:
        console.print(f"[bold red]Failed to parse JSON: {e}[/bold red]")
        break

    for t in data.get("tweets", []):
        hashtags = [h["text"] for h in t.get("entities", {}).get("hashtags", [])]
        urls = [u["expanded_url"] for u in t.get("entities", {}).get("urls", [])]
        mentions = [m["screen_name"] for m in t.get("entities", {}).get("user_mentions", [])]

        rows.append({
            "id": t.get("id"),
            "createdAt": t.get("createdAt"),
            "text": t.get("text"),
            "hashtags": ", ".join(hashtags),
            "urls": ", ".join(urls),
            "user_mentions": ", ".join(mentions),
            "retweetCount": t.get("retweetCount"),
            "replyCount": t.get("replyCount"),
            "likeCount": t.get("likeCount"),
            "quoteCount": t.get("quoteCount"),
            "viewCount": t.get("viewCount"),
            "bookmarkCount": t.get("bookmarkCount"),
        })

    count += 1

    if data.get('has_next_page'):
        cursor = data.get('next_cursor')
        console.print(f"[bold magenta]Next cursor:[/bold magenta] [cyan]{cursor[:10]}...{cursor[-10:]}[/cyan]")
    else:
        console.print("[bold green]No more pages available.[/bold green]")
        break

    status = Prompt.ask("Continue with next round?", choices=["yes", "no"], default="default: no")
    if status.lower() == 'no':
        break

df = pd.DataFrame(rows)
df.to_csv("response2.csv", index=False, encoding="utf-8")
console.rule("[bold green] Data saved to response2_final.csv [/bold green]")