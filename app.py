from flask import Flask


app = Flask(__name__)#Фласк будет искать все файлы в этой папке


@app.route('/')#юрл главная страница
def index():
    return 'Главная страница' #Эта строка будет отображаться на главной странице

@app.route('/blog')
def blog():
    return 'Страница блога'

@app.route('/news')
def news():
    return 'Страница новостей'



if __name__ =='__main__':
    app.run(debug=True)#если True то все ошибки показываются на сайте, поэтому когда сайт будет готов надо ставить False

