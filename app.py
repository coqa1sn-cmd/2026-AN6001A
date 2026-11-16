#web app

from flask import Flask,render_template,request
import joblib

model = joblib.load("dbs.pkl")

app = Flask(__name__) #backend via render.com (US -> SG -> US) gunicom.py then to html to CSS - GRADIO (new one)

@app.route("/",methods=["GET", "POST"])
def index():
    return (render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return (render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return (render_template("dbs.html"))

@app.route("/dbsResult",methods=["GET","POST"])
def dbsResult():
    q = float(request.form.get("q"))
    r = model.predict([[q]])
    return (render_template("dbsResult.html",r=r[0][0]))

if __name__ == "__main__":
    app.run()  # cloud uses a different code 

# to save 
# $ git add . 
# $ git commit -m "v1"
# $ git push
# $ python app.py