from models.unit import Unit

class UnitActions:
    def __init__(self, session):
        self.session = session

    def format_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f'{error_message}'

    def add(self, unit_name, short_name):
        try:
            new_unit = Unit(unit_name=unit_name, short_name=short_name)
            self.session.add(new_unit)
            self.session.commit()
            return "Единица измерения успешно добавлена!"
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось добавить единицу измерения."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def delete(self, unit_id):
        try:
            unit = self.session.query(Unit).filter_by(id=unit_id).first()
            if unit:
                self.session.delete(unit)
                self.session.commit()
                return "Единица измерения успешно удалена!"
            else:
                return f"Единица измерения с ID {unit_id} не найдена."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось удалить единицу измерения."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show(self, unit_id=None):
        try:
            if unit_id is None:
                units = self.session.query(Unit).all()
                result = "Все единицы измерения:\n"
                for unit in units:
                    result += f"{unit}\n"
                return result
            else:
                unit = self.session.query(Unit).filter_by(id=unit_id).first()
                if unit:
                    return str(unit)
                else:
                    return f"Единица измерения с ID {unit_id} не найдена."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить информацию о единице измерения."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )
