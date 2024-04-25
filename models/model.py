from typing import List
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Restaurant(Base):
    __tablename__ = "restaurant"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)


class Feedback(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(ForeignKey("client.id"))
    feedback: Mapped[str] = mapped_column(String(500))
    stars: Mapped[int]
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))


class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    name: Mapped[str]


class DishOrder(Base):
    __tablename__ = "DishOrder"

    dish_id: Mapped[int] = mapped_column(ForeignKey("dish.id"), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), primary_key=True)

    dish: Mapped["Dish"] = relationship(back_populates="orders")
    order: Mapped["Order"] = relationship(back_populates="dishes")


class Dish(Base):
    __tablename__ = "dish"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    cost: Mapped[float]
    type: Mapped[str] = mapped_column(String(20))
    description: Mapped[str] = mapped_column(String(500))
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurant.id"))

    orders: Mapped[List["DishOrder"]] = relationship(back_populates="dish")


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(default=datetime.now)
    comment: Mapped[str] = mapped_column(String(500))
    cost: Mapped[float] = mapped_column(default=0)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"))

    dishes: Mapped[List["DishOrder"]] = relationship(back_populates="order")
