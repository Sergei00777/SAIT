from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from db import db, Message
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Замените на свой!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db.init_app(app)
#with app.app_context():
#    db.create_all()

# Форма обратной связи
class ContactForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить')

# Главная страница
@app.route('/')
def home():
    return render_template('index.html')

# О себе
@app.route('/about')
def about():
    return render_template('about.html')

# Портфолио
@app.route('/portfolio')
def portfolio():
    projects = [
        {
            "title": "Communal-Apartment",
            "description": "Система учёта платежей за ЖКУ с прогнозированием расходов."
        },
        {
            "title": "HR-Department",
            "description": "CRM для кадрового учёта с аналитикой отпусков/больничных."
        },
        {
            "title": "MYcar",
            "description": "Сервис для учёта затрат на автомобиль (топливо, ремонты). Интеграции: VIN-декодер, API АЗС.."
        },
        {
            "title": "VIN-парсер",
            "description": "Парсер данных об авто по VIN (стек: Requests, bs4). Применение: Использовался в проекте «I Avto Expert»."
        },
        {
            "title": "Credit Calculator",
            "description": "Микросервис расчёта кредитных платежей с REST API (FastAPI)."
        },
        {
            "title": "VIN Checker Pro VIN Checker Pro",
            "description": "Оно предназначено для проверки информации об автомобилях по их VIN-номеру (Vehicle Identification Number), а также предоставляет доступ к различным онлайн-сервисам проверки автомобилей (например, ГИБДД, ФССП, реестр залогов и др.)"
        },
        {
            "title": "Car Analytics Dashboard Car Analytics Dashboard",
            "description": "предназначенное для анализа данных об автомобилях. Программа позволяет загружать данные из файлов (CSV, Excel, TXT), фильтровать их по марке и году выпуска, а также строить различные типы графиков для визуализации статистики: цены, пробега, мощности двигателей и других параметров автомобилей"
        },
        {
            "title": "Dog Photo Backup",
            "description": "Резервное копирование фото собак Программа автоматически загружает случайные изображения собак указанной породы с сайта https://dog.ceo и сохраняет их на Яндекс.Диск, организуя файлы по папкам. Также сохраняется информация о загруженных файлах в формате JSON."
        },
        {
            "title": "Парсер объявлений Drom.ru",
            "description": "Простая и удобная программа на Python с графическим интерфейсом (PyQt5). Парсить данные из скачанных файлов: название автомобиля, пробег, цену."
        },
        {
            "title": "Bitcoin Price Tracker Bitcoin Price Tracker",
            "description": "Позволяет отслеживать текущий курс Bitcoin в реальном времени и просматривать историю изменений цены в виде графика.."
        },
        {
            "title": "Elizabeth Bot – AI-автор для Telegram-канала",
            "description": "Elizabeth Bot – это Telegram-бот на Python, который автоматически генерирует и публикует контент в канал. Бот создает два типа постов: личные истории и автомобильные новости, используя API Mistral AI."
        },
        {
            "title": "Логистика автомобилей",
            "description": " Программа управления автопарком Простое и удобное приложение для учёта и управления автомобилями, поступающими на реализацию. Программа позволяет."
        },
        {
            "title": "QR-кодов",
            "description": "Генерировать QR-коды из текста или ссылки Настроить внешний вид: цвет, размер, формат Добавлять логотип в центр QR-кода Сохранять результат в разных форматах."
        },
        {
            "title": "ModernPDFEditor (Python)",
            "description": "Редактор PDF. Укажите библиотеки ( PyPDF2, ReportLab)."
        },
        {
            "title": "GOVORITTEXT  (HTML)",
            "description": "Приложение для голосового ввода."
        },
        {
            "title": "textconverter (HTML)",
            "description": "Конвертер текста. Полезно для резюме."
        },
        {
            "title": "home_accounting",
            "description": "Система учета финансов. Работа с базами данных (SQLite, PostgreSQL)"
        },
        {
            "title": "Web_scrapping",
            "description": "Скрипты для сбора данных. Библиотеки (BeautifulSoup, Scrapy, Selenium)."
        },
        {
            "title": "Password",
            "description": "Генератор/менеджер паролей."
        },
        {
            "title": "Thesnake",
            "description": "Классическая игра Змейка. Использование HTML/CSS/JS для реализации."
        },
        {
            "title": "TICtecTOE (Python)",
            "description": "Игра Крестики-нолики с логикой на Python."
        },
        {
            "title": "Tetris",
            "description": "Полноценная игра — Работы с графикой (Pygame)."
        },
        {
            "title": "ping_pong (Python)",
            "description": "Простая аркадная игра."
        },


        # Добавьте остальные проекты из резюме
    ]


    return render_template('portfolio.html', projects=projects)

@app.route('/certificates')
def certificates():
    certs = [
        {
            "title": "Python-разработчик (Нетология)",
            "file": "5bbadd4abacab2959d6c9c433a0bbda2.jpeg",
            "year": 2025
        },
        {
            "title": "Основы Python: телеграм-бот (Нетология)",
            "file": "60d9d334284a95b4db2936d81575302d.jpeg",
            "year": 2022
        },
        {
            "title": "ООП и работа с API (Нетология)",
            "file": "72c0ccb64abe1ec1e2b45d2e221cf050.jpeg",
            "year": 2025
        },
        {
            "title": "Основы языка програмирования Python (Нетология)",
            "file": "97db4c865af4b72e025525da50746459.jpeg",
            "year": 2025
        },
        {
            "title": "Git - система контроля версий (Нетология)",
            "file": "3804da23da3c709181edfdeb723bd8d4.jpeg",
            "year": 2025
        },
        {
            "title": "Поколение Python: курс для начинающих (Stepik)",
            "file": "2025-06-03_10-15-39.jpeg",
            "year": 2023
        },
        {
            "title": "Лучший по Python. Для всех начинающих! (Stepik)",
            "file": "2025-07-24_18-17-00.jpeg",
            "year": 2025
        },
        {
            "title": "Лучший по Python. Часть 2! (Stepik)",
            "file": "2025-07-24_18-17-59.jpeg",
            "year": 2025
        },
        {
            "title": "Лучший по Python. Часть 3! (Stepik)",
            "file": "Python3.jpeg",
            "year": 2025
        },
        {
            "title": "Git: от новичка до профи (Stepik)",
            "file": "git2.jpeg",
            "year": 2025
        },
        {
            "title": "Создание Телеграм БОТОВ (Stepik)",
            "file": "БОТ.jpeg",
            "year": 2025
        },
        {
            "title": "Риторика (Stepik)",
            "file": "Риторика.jpeg",
            "year": 2025
        },
        {
            "title": "Игрофикация (Stepik)",
            "file": "Игрофикация.jpeg",
            "year": 2025
        },
        {
            "title": "Профессиональная работа с Python (Нетология)",
            "file": "Профессиональная работа с Python.jpeg",
            "year": 2025
        },
        {
            "title": "Основы Excel (Stepik)",
            "file": "Основы Excel.jpeg",
            "year": 2025
        },
        {
            "title": "Обучения онлайн (Нетология)",
            "file": "Обучения онлайн.jpeg",
            "year": 2025
        },
        {
            "title": "Компьютерная грамотность (Нетология)",
            "file": "Компьютерная грамотность.jpeg",
            "year": 2025
        },
        {
            "title": "Офисные приложения для начинающих (Word, Excel, Google сервисы) (Stepik)",
            "file": "Офисные приложения для начинающих (Word, Excel, Google сервисы).jpeg",
            "year": 2025
        },
        {
            "title": "Войти в IT (Stepik)",
            "file": "Войти в IT.jpeg",
            "year": 2025
        },
        {
            "title": "Риск-менеджмент в стартапах (Stepik)",
            "file": "Риск-менеджмент в стартапах.jpeg",
            "year": 2025
        },
        # Добавьте остальные дипломы аналогично
    ]
    return render_template('certificates.html', certificates=certs)

# Контакты
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(msg)
        db.session.commit()
        flash('Сообщение отправлено!', 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', form=form)

@app.route('/programs')
def programs():
    return render_template('programs.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=False)