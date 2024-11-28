from sqlalchemy.orm import sessionmaker
from database import session_maker, create_db, drop_db
from gui import GuiApp

# Импорты для действий
from classifier.prodclassactions import ProdClassActions
from classifier.unitactions import UnitActions
from classifier.productactions import ProductActions
from classifier.paramactions import ParamClassifierActions
from classifier.paramclassactions import ParamClassClassifierActions
from classifier.paramproductactions import ParamProductClassifierActions

def main():
    create_db()

    with session_maker() as session:
        # Создание экземпляров действий
        prodclassactions = ProdClassActions(session)
        unitactions = UnitActions(session)
        productactions = ProductActions(session)
        paramactions = ParamClassifierActions(session)
        paramclassactions = ParamClassClassifierActions(session)
        paramproductactions = ParamProductClassifierActions(session)

        # Заполнение данными
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
        productactions.add("Стелажи для торговых помещений", 5)
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

        # Запуск GUI
        app = GuiApp(session)
        app.mainloop()

if __name__ == "__main__":
    main()