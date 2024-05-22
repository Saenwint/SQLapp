from models.product import Product

class ProductActions:
    def __init__(self, session):
        self.session = session

    def format_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f'{error_message}'

    def add(self, product_name, prod_class_id=None, enum_classifier_id=None):
        try:
            new_product = Product(product_name=product_name, prod_class_id=prod_class_id, enum_classifier_id=enum_classifier_id)
            self.session.add(new_product)
            self.session.commit()
            return "Продукт успешно добавлен!"
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось добавить продукт."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def delete(self, product_id):
        try:
            product_to_delete = self.session.query(Product).get(product_id)
            if product_to_delete:
                self.session.delete(product_to_delete)
                self.session.commit()
                return "Продукт успешно удален!"
            else:
                return "Продукт не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось удалить продукт."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show(self, product_id=None):
        try:
            if product_id is None:
                products = self.session.query(Product).all()
                result = "Все продукты:\n"
                for product in products:
                    result += f"{product}\n"
                return result
            else:
                product = self.session.query(Product).get(product_id)
                if product:
                    return str(product)
                else:
                    return "Продукт не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить информацию о продуктах."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show_by_prod_class(self, prod_class_id):
        try:
            products = self.session.query(Product).filter_by(prod_class_id=prod_class_id).all()
            if products:
                result = f"Продукты класса с идентификатором {prod_class_id}:\n"
                for product in products:
                    result += f"{product}\n"
                return result
            else:
                return "Для указанного идентификатора класса не найдены продукты."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить продукты по идентификатору класса."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show_by_enum_class(self, enum_classifier_id):
        try:
            products = self.session.query(Product).filter_by(enum_classifier_id=enum_classifier_id).all()
            if products:
                result = f"Продукты классификатора с идентификатором {enum_classifier_id}:\n"
                for product in products:
                    result += f"{product}\n"
                return result
            else:
                return "Для указанного идентификатора классификатора не найдены продукты."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить продукты по идентификатору классификатора."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def set_class(self, product_id, prod_class_id):
        try:
            product = self.session.query(Product).get(product_id)
            if product:
                product.prod_class_id = prod_class_id
                self.session.commit()
                return "Класс продукта успешно обновлен!"
            else:
                return "Продукт не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось обновить класс продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def set_enum(self, product_id, enum_classifier_id):
        try:
            product = self.session.query(Product).get(product_id)
            if product:
                product.enum_classifier_id = enum_classifier_id
                self.session.commit()
                return "Классификатор продукта успешно обновлен!"
            else:
                return "Продукт не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось обновить классификатор продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def check_class(self, product_id, prodclass_id):
        try:
            product = self.session.query(Product).get(product_id)
            if product:
                if product.prod_class_id == prodclass_id:
                    return "Выбранный класс принадлежит выбранному продукту."
                else:
                    return "Выбранный класс не принадлежит выбранному продукту."
            else:
                return "Продукт не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось проверить класс для продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )
