from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crt-books.db"

db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique=True, nullable=False)
    author_name = db.Column(db.String, unique=False, nullable=True)
    book_photo = db.Column(db.String, unique=False, nullable=True)

@app.route("/create_database")
def create_database():
    with app.app_context():
        db.create_all()
    return "DB Created."

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/books")
def get_all_books():
    books = Book.query.all()
    return render_template("books.html", all_books=books)

@app.route("/create", methods=["GET", "POST"])
def create_book():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        
        book = Book(
            book_name=book_name,
            author_name=author_name
        )

        db.session.add(book)
        db.session.commit()
        return redirect(url_for("get_all_books"))


@app.route("/health")
def health():
    return "Application is up."