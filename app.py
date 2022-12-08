#integrate our library and objects 
from flask import Flask, render_template

#create our flask instance/application 
app = Flask(__name__)
#create our directory 
@app.route('/')
def home2():
  return render_template("index.html")

@app.route('/')
def about():
  return render_template('index.html')

#run our aplication
#if __name__ == "__main__":
 # app.run(debug=True)