import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from models import Publisher, Book, Shop, Stock, Sale


def get_session():
    """ Получение сессии для работы с ORM """
    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB = os.getenv('POSTGRES_DB')

    DSN = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    engine = sqlalchemy.create_engine(DSN)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_info(publisher_name):
    """ Получение информации о покупке книг конкретного издателя """
    session = get_session()

    query = session.query(Publisher, Book, Shop, Stock, Sale)
    query = query.filter(Publisher.name == publisher_name.title())
    query = query.join(Book, Book.id_publisher == Publisher.id)
    query = query.join(Stock, Stock.id_book == Book.id)
    query = query.join(Shop, Stock.id_shop == Shop.id)
    query = query.join(Sale, Sale.id_stock == Stock.id)

    records = query.all()

    for publ, book, shop, stock, sale in records:
        print(f'{book.title} | {shop.name} | {sale.price} | {sale.date_sale}')


if __name__ == '__main__':
    publisher = input('Введите издателя: ')

    # Указание на новый файл с переменными окружения
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    get_info(publisher)


