from flask import Flask
from flask import render_template #функция которая позволяет возвращать html страницу


app = Flask(__name__)#Фласк будет искать все файлы в этой папке


@app.route('/')#юрл главная страница
def index():
    return render_template('index.html') #пишем только название файла, т.к. фласк знает что все шаблоны лежат тут

@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/news.html')
def news():
    return render_template('news.html')



if __name__ =='__main__':
    app.run(debug=True)#если True то все ошибки показываются на сайте, поэтому когда сайт будет готов надо ставить False

