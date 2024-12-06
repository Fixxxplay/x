#Импорт
from flask import Flask, render_template,request, redirect

app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')                       
def feedback():

    text = request.form.get('text')
    email = request.form.get('email')
    with open('text.txt', 'w', encoding='utf-8') as o:
              o.write( str(email))
              o.write(' - ')
              o.write( str(text))
    return render_template('index.html', text=text, email=email)
      
        

#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)
#def feedback():

    #text = request.form.get('text')
    #email = request.form.get('email')
    #with open('text.txt', 'w', encoding='utf-8') as o:
              #o.write( str(email))
              #o.write(' - ')
              #o.write( str(text))
    #return render_template('index.html', text=text, email=email)


if __name__ == "__main__":
    app.run(debug=True)