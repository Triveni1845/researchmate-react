from pathlib import Path

DOCS = Path(__file__).parent / 'docs'

def calculate(a: float, b: float):
    return {'result': float(a) * float(b)}

def search_documents(query: str):
    terms = set(query.lower().split())
    hits = []
    for p in DOCS.glob('*.md'):
        text = p.read_text(encoding='utf-8')
        if terms & set(text.lower().split()):
            hits.append({'source': p.name, 'excerpt': text[:500]})
    return {'matches': hits}