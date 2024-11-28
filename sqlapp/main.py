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
from classifier.specificationsactions import SpecificationActions

def main():
    drop_db()
    create_db()

    with session_maker() as session:
        # Создание экземпляров действий
        prodclassactions = ProdClassActions(session)
        unitactions = UnitActions(session)
        productactions = ProductActions(session)
        paramactions = ParamClassifierActions(session)
        paramclassactions = ParamClassClassifierActions(session)
        paramproductactions = ParamProductClassifierActions(session)
        specificationactions = SpecificationActions(session)

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

        productactions.add("Шкафы для учебных заведений", 3, price=100.0, quantity=10)
        productactions.add("Шкафы для административных помещений", 3, price=150.0, quantity=5)
        productactions.add("Шкафы детские", 3, price=200.0, quantity=3)

        productactions.add("Шкафы для одежды", 6, price=250.0, quantity=7)
        productactions.add("Шкафы для белья", 6, price=300.0, quantity=2)
        productactions.add("Шкафы для книг", 6, price=350.0, quantity=4)

        paramactions.add("Первый параметр", "пер", 2)
        paramactions.add("Второй параметр", "вт", 2)
        paramactions.add("Третий параметр", "трет", 3)

        paramclassactions.add(1, 3, 10, 50)
        paramclassactions.add(2, 3, 100, 150)
        paramclassactions.add(2, 4, 20, 35)
        paramclassactions.add(3, 4, 120, 130)

        paramproductactions.add(1, 2, 150)

        # Добавление строк спецификации
        specificationactions.add_line(1, 2, 2.5)
        specificationactions.add_line(1, 3, 1.0)
        specificationactions.add_line(2, 4, 3.0)

        # Запуск GUI
        app = GuiApp(session)
        app.mainloop()

if __name__ == "__main__":
    main()