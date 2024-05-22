from models.param_product import ParamProduct
from models.param_class import ParamClass
from models.product import Product

class ParamProductClassifierActions:
    def __init__(self, session):
        self.session = session

    def format_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f'{error_message}'

    def add(self, product_id, param_class_id, value):
        try:
            product = self.session.query(Product).filter_by(id_product=product_id).first()
            if product:
                param_class = self.session.query(ParamClass).filter_by(id=param_class_id).first()
                if param_class:
                    if param_class.prodclass_id == product.prod_class_id:
                        if param_class.min_value <= int(value) <= param_class.max_value:
                            new_param_product = ParamProduct(product_id=product_id, param_class_id=param_class_id, value=value)
                            self.session.add(new_param_product)
                            self.session.commit()
                            return f"Параметр успешно добавлен для продукта с ID {product_id}."
                        else:
                            return f"Значение параметра {value} выходит за пределы диапазона [{param_class.min_value}, {param_class.max_value}]."
                    else:
                        return f"Продукт с ID {product_id} не принадлежит к классу параметра с ID {param_class_id}."
                else:
                    return f"Класс параметра с ID {param_class_id} не найден."
            else:
                return f"Продукт с ID {product_id} не найден."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при добавлении параметра для продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def delete(self, product_id, param_class_id):
        try:
            param_product = self.session.query(ParamProduct).filter_by(product_id=product_id, param_class_id=param_class_id).first()
            if param_product:
                self.session.delete(param_product)
                self.session.commit()
                return f"Параметр с param_class_id={param_class_id} удален для продукта с product_id={product_id}."
            else:
                return f"Параметр с param_class_id={param_class_id} для продукта с product_id={product_id} не найден."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при удалении параметра продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show(self, product_id=None):
        try:
            result = []
            if product_id is None:
                param_products = self.session.query(ParamProduct).all()
                for param_product in param_products:
                    product = self.session.query(Product).filter_by(id_product=param_product.product_id).first()
                    if product:
                        result.append(f"Продукт: {product.product_name}, Параметр: {param_product}")
                    else:
                        result.append(f"Продукт с ID {param_product.product_id} не найден, Параметр: {param_product}")
            else:
                param_products = self.session.query(ParamProduct).filter_by(product_id=product_id).all()
                if param_products:
                    for param_product in param_products:
                        product = self.session.query(Product).filter_by(id_product=product_id).first()
                        if product:
                            result.append(f"Продукт: {product.product_name}, Параметр: {param_product}")
                        else:
                            result.append(f"Продукт с ID {product_id} не найден, Параметр: {param_product}")
                else:
                    result.append(f"Параметры для продукта с ID {product_id} не найдены.")
            return "\n".join(result)
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при выводе параметров продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def edit(self, product_id, param_class_id, value):
        try:
            param_product = self.session.query(ParamProduct).filter_by(product_id=product_id, param_class_id=param_class_id).first()
            if param_product:
                param_class = self.session.query(ParamClass).filter_by(id=param_class_id).first()
                if param_class and param_class.min_value <= int(value) <= param_class.max_value:
                    param_product.value = value
                    self.session.commit()
                    return f"Значение параметра с param_class_id={param_class_id} для продукта с product_id={product_id} успешно обновлено."
                else:
                    return f"Ошибка: Значение параметра {value} выходит за пределы диапазона [{param_class.min_value}, {param_class.max_value}]."
            else:
                return f"Параметр с param_class_id={param_class_id} для продукта с product_id={product_id} не найден."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка при редактировании параметра продукта."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )
