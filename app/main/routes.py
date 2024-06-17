from flask import render_template, redirect, url_for, request, Blueprint
from app.extensions import db, migrate
from app.forms import DataForm
from app.models import Content

# 'main' Blueprint 생성
main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def home():
    contents = Content.query.all()
    return render_template('home.html', contents=contents)

@main.route('/tool')
def tool():
    return render_template('tool.html')

@main.route('/store')
def store():
    return render_template('store.html')

@main.route('/tool-request')
def tool_request():
    contents = Content.query.all()
    return render_template('tool-request.html', contents=contents)

@main.route('/add', methods=['GET', 'POST'])
def add_content():
    form = DataForm()
    if form.validate_on_submit():
        new_content = Content(title=form.title.data, author=form.author.data, genre=form.genre.data)
        db.session.add(new_content)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add-content.html', form=form)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_content(id):
    content = Content.query.get_or_404(id)
    form = DataForm(obj=content)
    if form.validate_on_submit():
        form.populate_obj(content)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('edit-content.html', form=form, content=content, id=id)

@main.route('/delete/<int:id>', methods=['POST'])
def delete_content(id):
    content = Content.query.get_or_404(id)
    db.session.delete(content)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/tool-searching/', methods=['POST'])
def tool_searching(id):
    content = Content.query.get_or_404(id)
    form = DataForm(obj=content)
    if form.validate_on_submit():
        db.session.delete(content)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('tool-searching.html')

@main.route('/test')
def test():
    return render_template('test.html')
