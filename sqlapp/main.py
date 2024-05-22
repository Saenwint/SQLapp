from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

from classifier.prodclassactions import ProdClassActions
from classifier.unitactions import UnitActions
from classifier.productactions import ProductActions
from classifier.paramactions import ParamClassifierActions
from classifier.paramclassactions import ParamClassClassifierActions
from classifier.paramproductactions import ParamProductClassifierActions
from config import settings
from sqlapp.cli import CLInterface
from sqlapp.gui import GuiApp
# Константа, отвечающая за пересоздание таблиц
RECREATE_ALL = True

# Создание подключения к базе данных
def recreate_tables(engine_url, echo=False, recreate=RECREATE_ALL):
    print("Инициализация сессии работы с базой данных...")

    engine = create_engine(engine_url, echo=echo)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    if recreate:
        print("Таблицы будут пересозданы.")
        metadata.drop_all(engine)

    metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    return session

# Создание сессии
engine_url = settings.DATABASE_URL
session = recreate_tables(engine_url, recreate=RECREATE_ALL)

if RECREATE_ALL:
    # Создание объектов 
    prodclassactions = ProdClassActions(session)
    unitactions = UnitActions(session)
    productactions = ProductActions(session)
    paramactions = ParamClassifierActions(session)
    paramclassactions = ParamClassClassifierActions(session)
    paramproductactions = ParamProductClassifierActions(session)

    unitactions.add("Штука", "шт")
    unitactions.add("Миллиметр", "мм")
    unitactions.add("Килограмм", "кг")

    prodclassactions.add("Изделия", 1)
    
    prodclassactions.add("Мебель", 1, 1)
    prodclassactions.add("Шкафы", 1, 2)
    prodclassactions.add("Столы", 1, 2)
    prodclassactions.add("Стелажи", 1, 2)

    prodclassactions.add("Шкафы для жилых помещений", 1, 3)

    productactions.add("Шкафы для учебных заведений", 3)
    productactions.add("Шкафы для административных помещений", 3)
    productactions.add("Шкафы детские", 3)

    productactions.add("Шкафы для одежды", 6)
    productactions.add("Шкафы для белья", 6)
    productactions.add("Шкафы для книг", 6)

    productactions.add("Столы бытовые", 4)
    productactions.add("Столы для учебных заведений", 4)
    
    productactions.add("Стелажи бытовые", 5)
    productactions.add("Стелажи библиотечные", 5)
    productactions.add("Стелажи для торговых помещенй", 5)
    productactions.add("Стелажи для мастерских", 5)
    
    productactions.add("Стелажи1", 5)
    productactions.add("Стелажи2", 5)
    productactions.add("Стелажи3", 5)
    productactions.add("Стелажи4", 5)
    productactions.add("Стелажи5", 5)
    productactions.add("Стелажи6", 5)
    productactions.add("Стелажи7", 5)
    productactions.add("Стелажи8", 5)
    productactions.add("Стелажи9", 5)
    productactions.add("Стелажи10", 5)
    productactions.add("Стелажи11", 5)
    productactions.add("Стелажи12", 5)
    productactions.add("Стелажи13", 5)
    productactions.add("Стелажи14", 5)
    productactions.add("Стелажи15", 5)
    productactions.add("Стелажи16", 5)

    paramactions.add("Первый параметр", "пер", 2)
    paramactions.add("Второй параметр", "вт", 2)
    paramactions.add("Третий параметр", "трет", 3)

    paramclassactions.add(1, 3, 10, 50)
    paramclassactions.add(2, 3, 100, 150)
    paramclassactions.add(2, 4, 20, 35)
    paramclassactions.add(3, 4, 120, 130)

    paramproductactions.add(1, 2, 150)



# Графический интерфейс
guiapp = GuiApp(session)
guiapp.mainloop()

# Закрытие сессии
print("Завершение работы с базой данных...")
session.close()
