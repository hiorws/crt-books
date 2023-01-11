from flask import Flask, render_template, request

app = Flask(__name__)

books = [
    [1, "Test Book#1", "Ozgur"],
    [2, "Test Book#2", "Su"],
    [3, "Test Book#3", "Can"],
    [4, "Test Book#4", "Selim"],
]


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/books")
def get_all_books():
    return render_template("books.html", all_books=books)

@app.route("/create", methods=["GET", "POST"])
def create_book():
    if request.method == "GET":
        return render_template("create.html")
    elif request.method == "POST":
        book_name = request.form['book_name']
        author_name = request.form['author_name']
        
        book_index = books[-1][0] + 1
        books.append([book_index, book_name, author_name])

        print("BOOK_NAME: " + book_name)
        return "Book saved."


@app.route("/health")
def health():
    return "Application is up."