from models.param_class import ParamClass
from models.prodclass import ProdClass

class ParamClassClassifierActions:
    def __init__(self, session):
        self.session = session

    def format_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f'{error_message}'

    def add(self, param_id, prodclass_id, min_value=None, max_value=None):
        try:
            if min_value is not None and max_value is not None and min_value > max_value:
                return ("Ошибка: Минимальное значение не может быть больше максимального.")
                
            new_param_class = ParamClass(param_id=param_id, prodclass_id=prodclass_id, min_value=min_value, max_value=max_value)
            self.session.add(new_param_class)
            self.session.commit()
            return "Параметр класса успешно добавлен."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при добавлении параметра класса."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def delete(self, param_class_id):
        try:
            param_class = self.session.query(ParamClass).filter_by(id=param_class_id).first()
            if param_class:
                self.session.delete(param_class)
                self.session.commit()
                return f"Параметр класса с ID {param_class_id} успешно удален."
            else:
                return f"Параметр класса с ID {param_class_id} не найден."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при удалении параметра класса."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def set_paramcl(self, param_class_id, min_value=None, max_value=None):
        try:
            if min_value is not None and max_value is not None and min_value > max_value:
                return ("Ошибка: Минимальное значение не может быть больше максимального.")
            param_class = self.session.query(ParamClass).filter_by(id=param_class_id).first()
            if param_class:
                if min_value is not None:
                    param_class.min_value = min_value
                if max_value is not None:
                    param_class.max_value = max_value
                self.session.commit()
                return f"Значения параметра класса с ID {param_class_id} успешно обновлены."
            else:
                return f"Параметр класса с ID {param_class_id} не найден."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при установке параметра класса."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show(self, param_class_id=None):
        try:
            result = []
            if param_class_id is None:
                param_classes = self.session.query(ParamClass).all()
                for param_class in param_classes:
                    # Получаем информацию о продуктовом классе по его идентификатору
                    prod_class = self.session.query(ProdClass).filter_by(id=param_class.prodclass_id).first()
                    if prod_class:
                        result.append(f"Класс продукта: {prod_class.class_name}, Параметр: {param_class}")
                    else:
                        result.append(f"Класс продукта с ID {param_class.prodclass_id} не найден, Параметр: {param_class}")
            else:
                param_class = self.session.query(ParamClass).filter_by(id=param_class_id).first()
                if param_class:
                    # Получаем информацию о продуктовом классе по его идентификатору
                    prod_class = self.session.query(ProdClass).filter_by(id=param_class.prodclass_id).first()
                    if prod_class:
                        result.append(f"Класс продукта: {prod_class.class_name}, Параметр: {param_class}")
                    else:
                        result.append(f"Класс продукта с ID {param_class.prodclass_id} не найден, Параметр: {param_class}")
                else:
                    result.append(f"Класс параметра с ID {param_class_id} не найден.")
            return "\n".join(result)
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить информацию о классе параметра."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show_by_class(self, prodclass_id):
        try:
            result = []
            prod_class = self.session.query(ProdClass).filter_by(id=prodclass_id).first()
            if prod_class:
                result.append(f"Параметры для класса: {prod_class.class_name}")
                param_classes = self.session.query(ParamClass).filter_by(prodclass_id=prodclass_id).all()
                if param_classes:
                    for param_class in param_classes:
                        result.append(str(param_class))
                else:
                    result.append(f"Параметры для класса с ID {prodclass_id} не найдены.")
            else:
                result.append(f"Класс продукта с ID {prodclass_id} не найден.")
            return "\n".join(result)
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить информацию о классе параметра."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )
