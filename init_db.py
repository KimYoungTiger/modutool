from app import create_app, db
from app.models import Book
import os

# 데이터베이스 파일 경로
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'books.db')

# 기존 데이터베이스 파일 삭제
if os.path.exists(db_path):
    os.remove(db_path)

# 애플리케이션 생성 및 데이터베이스 초기화
app = create_app()

with app.app_context():
    db.create_all()

    if Book.query.count() == 0:
        book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Fiction")
        book2 = Book(title="1984", author="George Orwell", genre="Dystopian")
        book3 = Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction")
        db.session.add(book1)
        db.session.add(book2)
        db.session.add(book3)
        db.session.commit()
        print("초기 데이터가 추가되었습니다.")
    else:
        print("데이터베이스에 이미 데이터가 있습니다.")
