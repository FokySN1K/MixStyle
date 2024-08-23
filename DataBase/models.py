from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, relationship, Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, Text, BigInteger, ForeignKey
from DataBase import config



# создаем движок SqlAlchemy
engine = config.engine


# создаем базовый класс для моделей
class Base(DeclarativeBase): pass



class product_color(Base):

    __tablename__ = "product_color"

    id: Mapped[int] = mapped_column(primary_key=True)
    color_id: Mapped[int] = mapped_column(
        ForeignKey('Color.name')
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('Product.id')
    )

class Color(Base):

    __tablename__ = "Color"

    name: Mapped[str] = mapped_column(String(100), nullable=False, primary_key=True)
    products = relationship('Product', secondary=product_color.__table__, back_populates='colors')


class product_category(Base):

    __tablename__ = "product_category"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey('Category.name')
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('Product.id')
    )



class Category(Base):
    __tablename__ = "Category"

    name: Mapped[str] = mapped_column(String(100), nullable=False, primary_key=True)
    products = relationship('Product', secondary=product_category.__table__, back_populates="categories")



class product_size(Base):

    __tablename__ = "product_size"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey('Size.id')
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('Product.id')
    )


class Size(Base):

    __tablename__ = "Size"

    id: Mapped[int] = mapped_column(primary_key=True)
    clothing_size: Mapped[int] = mapped_column(nullable=False)
    products = relationship('Product', secondary=product_size.__table__, back_populates="size")
    amount: Mapped[int] = mapped_column()

class product_country(Base):
    __tablename__ = "product_country"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey('Country.name')
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('Product.id')
    )


class Country(Base):
    __tablename__ = "Country"

    name: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    products = relationship('Product', secondary=product_country.__table__, back_populates="countries")




class product_order(Base):

    __tablename__ = "product_order"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(
        ForeignKey('Order.id')
    )
    product_id: Mapped[int] = mapped_column(
        ForeignKey('Product.id')
    )


class Product(Base):

    __tablename__ = "Product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    cost: Mapped[int] = mapped_column(nullable=False)
    article_number: Mapped[int] = mapped_column(BigInteger, nullable=False)
    company: Mapped[str] = mapped_column(String(30), nullable=False)
    describe: Mapped[str] = mapped_column(Text, nullable=False)

    colors = relationship('Color', secondary=product_color.__table__, back_populates="products")
    categories = relationship("Category", secondary=product_category.__table__, back_populates="products")
    countries = relationship("Country", secondary=product_country.__table__, back_populates="products")
    size = relationship("Size", secondary=product_size.__table__, back_populates="products")
    orders = relationship("Order", secondary=product_order.__table__, back_populates="products")



class Consumer(Base):

    __tablename__ = "Consumer"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger,unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False)
    LastName: Mapped[str] = mapped_column(String(30), nullable=False)
    FirstName: Mapped[str] = mapped_column(String(30), nullable=False)
    MiddleName: Mapped[str] = mapped_column(String(30), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(30), nullable=True)
    orders = relationship("Order", back_populates="consumers")



class Order(Base):

    __tablename__ = "Order"

    id: Mapped[int] = mapped_column(primary_key=True)
    number_order: Mapped[int] = mapped_column(unique=True)
    purchased: Mapped[bool] = mapped_column()

    products = relationship("Product", secondary=product_order.__table__, back_populates="orders")
    consumer_id: Mapped[int] = mapped_column(
        ForeignKey("Consumer.id")
    )
    consumers = relationship("Consumer", back_populates="orders")


def create_tables():
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)





# создаем таблицы
if __name__ == '__main__':
    with engine.begin() as conn:
        Base.metadata.create_all(bind=conn)

