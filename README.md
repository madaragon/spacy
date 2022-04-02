# spacy
Wrapper library that connects to twitter api v2 with Python.

This library allows you to access endpoints for space ID searches and keyword searches.

## Requirement
requests 
pip install requests

## Usage

```
$python3
>>>import spacy
>>>sp = spacy.spacy()
>>>sp.create_params(query='characters', state='live')
>>>sp.connect_to_search_space_endpoint()
print return json
```