## Factcheck Helper

This tool uses generative AI to help journalism fact-checking. 
It provides a web page where a user can upload an article. The tool will then generate a list of assertions contained
within the article.

### Installation

edit your OPENAI API key in `secrets.py`

```
poetry install
factcheck_helper:app --reload --host 0.0.0.0 --port 8080
```

The page willl load at http://localhost:8080
Paste an article into the box at the top, and click the 'submit for fact-checking' button. Wait a few seconds --
be patient, it takes a while to generate. When it is finished, you will see the assertions listed underneath
the article


### Development Status

TODO:
- [ ] Option to select different prompts
- [ ] Support for different backends (llamaindex)
- [ ] A few minimal tests
- [ ] first pass with mypy, black, pylint