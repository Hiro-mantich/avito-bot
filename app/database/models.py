import sqlalchemy
from sqlalchemy import BigInteger, String,LargeBinary
from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs,async_sessionmaker, create_async_engine


engine = create_async_engine(url='sqlite+aiosqlite:///db_card.sqlite3') #говорю проге о том, что буду sqlite3 использовать

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs,DeclarativeBase):
    pass

class Card(Base): #создание таблицы для хранения захваченных карточек товаров
    __tablename__ = 'card' #здесь задается имя таблицы

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(25))
    price: Mapped[str] = mapped_column(String(25))
    link: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(100))

async def async_make_db(): #функция создания таблицы при её отсутсвии
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

