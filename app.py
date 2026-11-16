#web app

from flask import Flask,render_template,request

app = Flask(__name__) #backend via render.com (US -> SG -> US) gunicom.py then to html to CSS - GRADIO (new one)

@app.route("/")
def index():
    return (render_template("index.html"))

if __name__ == "__main__":
    app.run()  # cloud uses a different code 
