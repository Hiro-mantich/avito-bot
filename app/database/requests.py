from app.database.models import async_session
from app.database.models import Card
from sqlalchemy import select

async def add_card_in_db(title_card,price_card,link_card,description_card): #создание записи в ДБ
    async with async_session() as session:
        async with session.begin():
            # Создаем экземпляр Card и заполняем его поля
            new_order = Card(
                title=title_card,
                price=price_card,
                link=link_card,
                description="This is a sample description"
            )
            # Добавляем экземпляр в сессию
            session.add(new_order)
            # Транзакция будет зафиксирована автоматически при выходе из блока `async with session.begin()`

async def get_all_cards(): #Вывести все записи (строки) из БД
    async with async_session() as session:
        return await session.scalars(select(Card))
