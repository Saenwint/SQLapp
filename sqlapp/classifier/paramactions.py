from models.param import Param

class ParamClassifierActions:
    def __init__(self, session):
        self.session = session

    def format_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f'{error_message}'

    def add(self, name, short_name, unit_id=None, enum_classifier_id=None):
        try:
            new_param = Param(name=name, short_name=short_name, unit_id=unit_id, enum_classifier_id=enum_classifier_id)
            self.session.add(new_param)
            self.session.commit()
            return "Параметр успешно добавлен!"
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось добавить параметр."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def delete(self, param_id):
        try:
            param = self.session.query(Param).filter_by(id=param_id).first()
            if param:
                self.session.delete(param)
                self.session.commit()
                return "Параметр успешно удален!"
            else:
                return f"Параметр с ID {param_id} не найден."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось удалить параметр."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show(self, param_id=None):
        try:
            if param_id is None:
                params = self.session.query(Param).all()
                result = "Все параметры:\n"
                for param in params:
                    result += f"{param}\n"
                return result
            else:
                param = self.session.query(Param).get(param_id)
                if param:
                    return str(param)
                else:
                    return "Параметр не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить информацию о параметрах."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )
