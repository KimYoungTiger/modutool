from flask import render_template, redirect, url_for, request
from app import db
from app.forms import DataForm
from app.models import Content

def init_routes(app):
    @app.route('/')
    def index():
        contents = Content.query.all()
        return render_template('index.html', contents=contents)

    @app.route('/add', methods=['GET', 'POST'])
    def add_content():
        form = DataForm()
        if form.validate_on_submit():
            new_content = Content(title=form.title.data, author=form.author.data, genre=form.genre.data)
            db.session.add(new_content)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_content.html', form=form)

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit_content(id):
        content = Content.query.get_or_404(id)
        form = DataForm(obj=content)
        if form.validate_on_submit():
            form.populate_obj(content)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit_content.html', form=form, content=content, id=id)

    @app.route('/delete/<int:id>', methods=['POST'])
    def delete_content(id):
        content = Content.query.get_or_404(id)
        db.session.delete(content)
        db.session.commit()
        return redirect(url_for('index'))

    @app.route('/tool_searching/', methods=['POST'])
    def tool_searching(id):
        content = Content.query.get_or_404(id)
        form = DataForm(obj=content)
        if form.validate_on_submit():
            db.session.delete(content)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('tool_searching.html')
