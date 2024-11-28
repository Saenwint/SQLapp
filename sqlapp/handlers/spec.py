from classifier.specificationsactions import SpecificationActions

class SpecificationHandler:
    def __init__(self, session):
        self.specification_actions = SpecificationActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.spec_help()
        elif command == "add":
            return self.spec_add(args[1:])
        elif command == "del":
            return self.spec_del(args[1:])
        elif command == "show":
            return self.spec_show(args[1:])
        elif command == "findall":
            return self.spec_findall(args[1:])
        elif command == "calcnorms":
            return self.spec_calcnorms(args[1:])
        else:
            return "Неверная команда. Введите 'spec help', чтобы увидеть доступные команды."

    def spec_help(self):
        return (
            "spec help\n"
            "spec add     [product_id] [component_id] [quantity]\n"
            "spec del     [line_id]\n"
            "spec show    [product_id]\n"
            "spec findall [product_id]\n"
            "spec calcnorms [product_id] [resource_class_id]\n"
        )

    def spec_add(self, args):
        if len(args) < 3:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта, идентификатор компонента и количество."
        product_id = args[0]
        component_id = args[1]
        quantity = float(args[2])
        return self.specification_actions.add_line(product_id, component_id, quantity)

    def spec_del(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор строки спецификации."
        line_id = args[0]
        return self.specification_actions.delete_line(line_id)

    def spec_show(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта."
        product_id = args[0]
        return self.specification_actions.show_lines(product_id)

    def spec_findall(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта."
        product_id = args[0]
        return self.specification_actions.find_all_lines(product_id)

    def spec_calcnorms(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта и идентификатор класса ресурсов."
        product_id = args[0]
        resource_class_id = args[1]
        return self.specification_actions.calculate_summary_norms(product_id, resource_class_id)