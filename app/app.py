import logging
import os

from flask import Flask

app = Flask(__name__)


@app.route('/health')
def health():
    return 'Hey.. I\'m walkin\' here!\n'


@app.route('/hello')
def hello():
    return {'hello': 'world'}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
