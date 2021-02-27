import json
import spacy
import sys

from flask import Flask, render_template, request

from ner_client import NamedEntityClient

app = Flask(__name__)

SPACY_MODEL = 'en_core_web_sm'
try:
    model = spacy.load(SPACY_MODEL)
except OSError:
    print('Downloading language model for the spaCy POS tagger\n'
        "(don't worry, this will only happen once)",
        file=sys.stderr)
    from spacy.cli import download
    download(SPACY_MODEL)
    model = spacy.load(SPACY_MODEL)
ner = NamedEntityClient(model)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ner', methods=['POST'])
def get_named_ents():
    data = request.get_json()
    result = ner.get_ents(data['sentence'])
    response = {'entities': result.get('ents'), 'html': result.get('html')}
    return json.dumps(response)

if __name__ == "__main__":
    app.run(debug=True)
