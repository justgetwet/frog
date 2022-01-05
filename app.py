from flask import Flask, render_template
import os
from scipy.stats import binom

p = 1/99.9
pmf = lambda n, p: binom.pmf(0, n, p)

app = Flask(__name__)

@app.route('/')
def hello():
    variable = pmf(100, p) + 1.
    return render_template("index.html", variable=variable)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8888)), debug=True)