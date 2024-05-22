from flask import render_template, redirect, url_for, request
from app import db
from app.forms import DataForm
from app.models import Book

def init_routes(app):
    @app.route('/')
    def index():
        books = Book.query.all()
        return render_template('index.html', books=books)

    @app.route('/add', methods=['GET', 'POST'])
    def add_book():
        form = DataForm()
        if form.validate_on_submit():
            new_book = Book(title=form.title.data, author=form.author.data, genre=form.genre.data)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_book.html', form=form)

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit_book(id):
        book = Book.query.get_or_404(id)
        form = DataForm(obj=book)
        if form.validate_on_submit():
            book.title = form.title.data
            book.author = form.author.data
            book.genre = form.genre.data
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit_book.html', form=form, book=book)

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_book(id):
        book = Book.query.get_or_404(id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))
