import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove script and style tags
        for tag in soup(['script', 'style']):
            tag.decompose()

        # Get all paragraph text
        paragraphs = [p.get_text().strip() for p in soup.find_all('p')]
        return "\n".join(paragraphs)

    except Exception as e:
        print(f"Error fetching article: {e}")
        return ""
