from models.enumposition import EnumPosition

class EnumPositionActions:
    def __init__(self, session):
        self.session = session

    def print_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f"{error_message}"

    def add(self, name, short_name, classifier_id, value_type, value):
        try:
            new_position = EnumPosition(
                name=name,
                short_name=short_name,
                classifier_id=classifier_id
            )
            if value_type == 'integer':
                new_position.integer_value = value
            elif value_type == 'real':
                new_position.real_value = value
            elif value_type == 'string':
                new_position.string_value = value
            else:
                return "Недопустимый тип значения."
            
            self.session.add(new_position)
            self.session.commit()
            return "Позиция перечисления успешно добавлена!"
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка добавления позиции перечисления:", str(e)),
                self.print_error("Тип исключения:", type(e))
            )

    def delete(self, pos_id):
        try:
            position_to_delete = self.session.query(EnumPosition).get(pos_id)
            if position_to_delete:
                self.session.delete(position_to_delete)
                self.session.commit()
                return "Позиция перечисления успешно удалена!"
            else:
                return "Позиция перечисления не найдена по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка удаления позиции перечисления:", str(e)),
                self.print_error("Тип исключения:", type(e))
            )
            

    def show(self, pos_id=None):
        try:
            if pos_id is None:
                positions = self.session.query(EnumPosition).all()
                result = ""
                for pos in positions:
                    result += str(pos) + "\n"
                return result
            else:
                pos = self.session.query(EnumPosition).get(pos_id)
                if pos:
                    return str(pos)
                else:
                    return "Позиция перечисления не найдена по указанному идентификатору."
        except Exception as e:
            return (
                self.print_error("Ошибка получения позиций перечисления:", str(e)),
                self.print_error("Тип исключения:", type(e))
            )

    def swap(self, pos_id1, pos_id2):
        try:
            pos1 = self.session.query(EnumPosition).get(pos_id1)
            pos2 = self.session.query(EnumPosition).get(pos_id2)

            if pos1.classifier_id == pos2.classifier_id:
                pos1.name, pos2.name = pos2.name, pos1.name
                pos1.short_name, pos2.short_name = pos2.short_name, pos1.short_name
                pos1.integer_value, pos2.integer_value = pos2.integer_value, pos1.integer_value
                pos1.real_value, pos2.real_value = pos2.real_value, pos1.real_value
                pos1.string_value, pos2.string_value = pos2.string_value, pos1.string_value

                self.session.commit()
                return "Идентификаторы позиций перечисления успешно обменяны!"
            else:
                return "Позиции имеют разные классификаторы, не могут быть обменены."
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка обмена позициями перечисления:", str(e)),
                self.print_error("Тип исключения:", type(e))
            )



