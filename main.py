from flask import Flask,render_template,request

app=Flask(__name__)
@app.get("/") #decorator
def showPage():
    return render_template("index.html")

@app.post("/analyze")
def analyze():
    text = request.form['text']
    action=request.form['action']
    print(text,action)
    answer=""
    if(action=="cntchr"):
        answer=f"the number of character are:-{len(text)}"
    if(action=="cntws"):
        answer="the numer of white space are:-{text.count(' ')}"    
    return render_template('index.html' ,output=answer)

app.run(debug=True)