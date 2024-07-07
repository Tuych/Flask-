from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'skjh1nmwdcee9dcde7cwdwhvg4rf4673t23dvcdgcvxsjxhg1f'
pages = [
    {'name': 'Главная', 'url': 'index'},
    {'name': 'Регистрация', 'url': 'register'}
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Главний странитца', pages=pages)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_age = int(request.form['age'])
        if user_age >= 18:
            flash('Вы зарегистрированы', category='success')
        else:
            flash('Для регистрации вам должно быть больше 18 лет', category='error')

        return render_template('register.html', title='Регистрация', pages=pages)

    return render_template('register.html', title='Регистрация', pages=pages)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Странитца не найдена', pages=pages)


if __name__ == '__main__':
    app.run(debug=True)