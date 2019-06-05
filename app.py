from flask import Flask,request,render_template,redirect,url_for
import wikipedia

app=Flask(__name__)

@app.route('/')
def index():
    return("hello world")

@app.route('/query',methods=['GET','POST'])
def query():
     if request.method=='GET':
         return render_template("query.html")
     else:
         query=request.form.get('query')
         wiki_page=wikipedia.page(query)
         try:
            title=wiki_page.title
            url=wiki_page.url
            summ = wikipedia.summary(query)
         except wikipedia.exceptions.DisambiguationError as e: 
            summ=e.options
          
         return render_template('query.html', summ=summ,title=title,url=url)
         

if __name__=="__main__":
    app.run(use_reloader=True,debug=True)             
