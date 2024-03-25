import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale


def get_data():
    """ Считывание данных с файла """
    with open('fixtures/tests_data.json') as file:
        data = json.load(file)
    return data


def get_instances():
    """ Создание списка экземпляров """
    data = get_data()
    instances = []
    for object in data:
        match object['model']:
            case 'publisher':
                instances.append(Publisher(name=object['fields']['name']))
            case 'book':
                instances.append(Book(title=object['fields']['title'],
                                      id_publisher=object['fields']['id_publisher']))
            case 'shop':
                instances.append(Shop(name=object['fields']['name']))
            case 'stock':
                instances.append(Stock(id_shop=object['fields']['id_shop'],
                                       id_book=object['fields']['id_book'],
                                       count=object['fields']['count']))
            case 'sale':
                instances.append(Sale(price=object['fields']['price'],
                                      date_sale=object['fields']['date_sale'],
                                      count=object['fields']['count'],
                                      id_stock=object['fields']['id_stock']))
    return instances


def commit_instances(session):
    """ Добавление экземпляров в БД """
    instances = get_instances()
    session.add_all(instances)
    session.commit()


if __name__ == '__main__':
    DSN = 'postgresql://postgres:admin@localhost:5432/book_system'
    engine = sqlalchemy.create_engine(DSN)

    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    commit_instances(session)

    session.close()
