from flask import Flask, request, render_template
from conf import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

VECTORIZER = load_model('./model/vectorizer.plk')

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template("form.html")


@app.route('/answer', methods=['POST'])
def answer():
    url = [request.form.get("url")]
    urls_vectorized = VECTORIZER.transform(url)
    model = load_model('./model/url_detector.plk')
    predict = model.predict(urls_vectorized)

    if predict == 1:
        result = '¡CUIDADO! Es una web maliciosa'
    elif predict == 0:
        result = 'No es un web maliciosa'
    return render_template("answer.html", result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
