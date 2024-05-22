from models.prodclass import ProdClass

class ProdClassActions:
    def __init__(self, session):
        self.session = session

    def is_descendant(self, cls, potential_parent):
        while cls is not None:
            if cls.id == potential_parent.id:
                return True
            cls = cls.parent
        return False

    def print_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f"{error_message}"

    def add(self, class_name, unit_id=None, parent_id=None):
        try:
            new_class = ProdClass(class_name=class_name, unit_id=unit_id, parent_id=parent_id)
            self.session.add(new_class)
            self.session.commit()
            return "Класс успешно добавлен!"
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка: Не удалось добавить класс."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def delete(self, class_id):
        try:
            class_to_delete = self.session.query(ProdClass).get(class_id)
            if class_to_delete:
                self.session.delete(class_to_delete)
                self.session.commit()
                return "Класс успешно удален!"
            else:
                return "Класс не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка: Не удалось удалить класс."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def show(self, class_id=None):
        try:
            if class_id is None:
                classes = self.session.query(ProdClass).all()
                return "\n".join(str(cls) for cls in classes)
            else:
                cls = self.session.query(ProdClass).get(class_id)
                if cls:
                    return str(cls)
                else:
                    return "Класс не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.print_error("Ошибка: Не удалось получить информацию о классах."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def parent(self, class_id):
        try:
            cls = self.session.query(ProdClass).get(class_id)
            if cls:
                parent_cls = self.session.query(ProdClass).get(cls.parent_id)
                if parent_cls:
                    return f"Родительский класс:\n{parent_cls}"
                else:
                    return "У класса нет родителя."
            else:
                return "Класс не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.print_error("Ошибка: Не удалось получить родительский класс."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def children(self, class_id):
        try:
            cls = self.session.query(ProdClass).get(class_id)
            if cls:
                children_cls = cls.children
                if children_cls:
                    return "Дочерние классы:\n" + self.print_children_recursive(children_cls, level=0)
                else:
                    return "У класса нет дочерних элементов."
            else:
                return "Класс не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.print_error("Ошибка: Не удалось получить дочерние классы."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def print_children_recursive(self, children_cls, level):
        result = []
        for child_cls in children_cls:
            result.append("  " * level + str(child_cls))
            result.append(self.print_children_recursive(child_cls.children, level + 1))
        return "\n".join(result)

    def change_parent(self, class_id, new_parent_id):
        try:
            cls = self.session.query(ProdClass).get(class_id)
            new_parent_cls = self.session.query(ProdClass).get(new_parent_id)
            
            if not self.is_descendant(new_parent_cls, cls):
                if cls and new_parent_cls:
                    cls.parent = new_parent_cls
                    self.session.commit()
                    return "Родительский класс успешно изменен!"
                else:
                    return "Не удалось найти класс или новый родительский класс с указанными идентификаторами."
            else:
                return "Изменение родительского класса создаст циклическую зависимость."
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка: Не удалось изменить родительский класс."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def set_unit(self, class_id, unit_id):
        try:
            cls = self.session.query(ProdClass).get(class_id)
            if cls:
                cls.unit_id = unit_id
                self.session.commit()
                return "Единица измерения успешно установлена для класса!"
            else:
                return "Класс не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка: Не удалось установить единицу измерения для класса."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )

    def swap(self, class_id1, class_id2):
        try:
            cls1 = self.session.query(ProdClass).get(class_id1)
            cls2 = self.session.query(ProdClass).get(class_id2)

            if cls1.parent_id == cls2.parent_id:
                cls1children = cls1.children
                cls2children = cls2.children

                for child in cls1children:
                    child.parent_id = cls2.id
                for child in cls2children:
                    child.parent_id = cls1.id

                cls1.class_name, cls2.class_name = cls2.class_name, cls1.class_name
                cls1.unit_id, cls2.unit_id = cls2.unit_id, cls1.unit_id

                self.session.commit()
                return "Идентификаторы классов и их дочерних элементов успешно обменяны!"
            else:
                return "Классы имеют разных родителей, не могут быть обменены."
        except Exception as e:
            self.session.rollback()
            return (
                self.print_error("Ошибка: Не удалось обменять классы и их дочерние элементы."),
                self.print_error("Тип исключения:", type(e)),
                self.print_error("Описание ошибки:", str(e))
            )
