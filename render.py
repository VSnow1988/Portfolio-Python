from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def indexRender():
  return render_template('index.html')



@app.route('/Projects')

def projectsRender():
  return render_template('index.html')



@app.route('/AboutMe')

def aboutRender():
  return render_template('index.html')
