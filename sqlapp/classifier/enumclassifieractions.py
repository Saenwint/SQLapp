from models.enumclassifier import EnumClassifier

class EnumClassifierActions:
    def __init__(self, session):
        self.session = session

    def format_error(self, *args):
        error_message = ' '.join(map(str, args))
        return f'{error_message}'

    def is_descendant(self, cls, potential_parent):
        while cls is not None:
            if cls.id == potential_parent.id:
                return True
            cls = cls.parent
        return False

    def add(self, name, parent_id=None):
        try:
            new_classifier = EnumClassifier(name=name, parent_id=parent_id)
            self.session.add(new_classifier)
            self.session.commit()
            return "Классификатор перечисления успешно добавлен!"
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось добавить классификатор перечисления."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def delete(self, class_id):
        try:
            classifier_to_delete = self.session.query(EnumClassifier).get(class_id)
            if classifier_to_delete:
                self.session.delete(classifier_to_delete)
                self.session.commit()
                return "Классификатор перечисления успешно удален!"
            else:
                return "Классификатор перечисления не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось удалить классификатор перечисления."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def show(self, class_id=None):
        try:
            result = []
            if class_id is None:
                classifiers = self.session.query(EnumClassifier).all()
                result.append("Все классификаторы:")
                for classifier in classifiers:
                    result.append(str(classifier))
            else:
                classifier = self.session.query(EnumClassifier).get(class_id)
                if classifier:
                    result.append(str(classifier))
                else:
                    result.append("Классификатор перечисления не найден по указанному идентификатору.")
            return "\n".join(result)
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить классификаторы перечисления."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )
    
    def parent(self, class_id):
        try:
            classifier = self.session.query(EnumClassifier).get(class_id)
            if classifier:
                parent_classifier = self.session.query(EnumClassifier).get(classifier.parent_id)
                if parent_classifier:
                    return "Родительский классификатор:\n" + str(parent_classifier)
                else:
                    return "У классификатора нет родителя."
            else:
                return "Классификатор перечисления не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить родительский классификатор."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def children(self, class_id):
        try:
            classifier = self.session.query(EnumClassifier).get(class_id)
            if classifier:
                children_classifiers = classifier.children
                if children_classifiers:
                    result = ["Дочерние классификаторы:"]
                    result.extend(self.get_children_recursive(children_classifiers, level=0))
                    return "\n".join(result)
                else:
                    return "У классификатора перечисления нет дочерних элементов."
            else:
                return "Классификатор перечисления не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить дочерние классификаторы."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def get_children_recursive(self, children_cls, level):
        result = []
        for child_cls in children_cls:
            result.append("  " * level + str(child_cls))
            result.extend(self.get_children_recursive(child_cls.children, level + 1))
        return result

    def positions(self, class_id):
        try:
            classifier = self.session.query(EnumClassifier).get(class_id)
            if classifier:
                classifier_positions = classifier.positions
                if classifier_positions:
                    result = ["Позиции классификатора:"]
                    for position in classifier_positions:
                        result.append(str(position))
                    return "\n".join(result)
                else:
                    return "У классификатора нет позииций."
            else:
                return "Классификатор перечисления не найден по указанному идентификатору."
        except Exception as e:
            return (
                self.format_error("Ошибка: Не удалось получить позиции классификатора."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
                )
    def change_parent(self, class_id, new_parent_id):
        try:
            classifier = self.session.query(EnumClassifier).get(class_id)
            new_parent_classifier = self.session.query(EnumClassifier).get(new_parent_id)

            if not self.is_descendant(new_parent_classifier, classifier):
                if classifier and new_parent_classifier:
                    classifier.parent = new_parent_classifier
                    self.session.commit()
                    return "Родительский классификатор успешно изменен!"
                else:
                    return "Один из классификаторов или новый родительский классификатор не найдены по указанным идентификаторам."
            else:
                return "Изменение родительского классификатора создаст циклическую зависимость."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось изменить родительский классификатор."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def swap(self, class_id1, class_id2):
        try:
            classifier1 = self.session.query(EnumClassifier).get(class_id1)
            classifier2 = self.session.query(EnumClassifier).get(class_id2)
            if classifier1.parent_id == classifier2.parent_id:
                cls1children = classifier1.children
                cls2children = classifier2.children

                for child in cls1children:
                    child.parent_id = classifier2.id
                for child in cls2children:
                    child.parent_id = classifier1.id

                cls1pos = classifier1.positions
                cls2pos = classifier2.positions

                for position in cls1pos:
                    position.classifier_id = classifier2.id
                for position in cls2pos:
                    position.classifier_id = classifier1.id

                classifier1.name, classifier2.name = classifier2.name, classifier1.name
                classifier1.unit_id, classifier2.unit_id = classifier2.unit_id, classifier1.unit_id

                self.session.commit()
                return "Идентификаторы классов и их дочерних элементов успешно обменяны!"
            else:
                return "Классификаторы имеют разных родителей, их нельзя обменять."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось обменять классификаторы перечисления."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
            )

    def set_unit(self, class_id, unit_id):
        try:
            classifier = self.session.query(EnumClassifier).get(class_id)
            if classifier:
                classifier.unit_id = unit_id
                self.session.commit()
                return "Единица успешно установлена для классификатора перечисления!"
            else:
                return "Классификатор перечисления не найден по указанному идентификатору."
        except Exception as e:
            self.session.rollback()
            return (
                self.format_error("Ошибка: Не удалось установить единицу для классификатора перечисления."),
                self.format_error("Тип исключения:", type(e)),
                self.format_error("Описание ошибки:", str(e))
        )
