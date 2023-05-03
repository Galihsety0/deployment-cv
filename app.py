from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

app   = Flask(__name__, static_url_path='/static')

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('Portofolio.html')

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run()