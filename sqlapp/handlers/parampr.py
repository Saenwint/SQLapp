from classifier.paramproductactions import ParamProductClassifierActions

class ParamProdHandler:
    def __init__(self, session):
        self.parampr_actions = ParamProductClassifierActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.parampr_help()
        elif command == "add":
            return self.parampr_add(args[1:])
        elif command == "delete":
            return self.parampr_delete(args[1:])
        elif command == "show":
            return self.parampr_show(args[1:])
        elif command == "edit":
            return self.parampr_edit(args[1:])
        else:
            return "Неверная команда. Введите 'parampr help', чтобы увидеть доступные команды."

    def parampr_help(self):
        return (
            "parampr help\n"
            "parampr add          [product_id] [param_class_id] [value]\n"
            "parampr delete       [product_id] [param_class_id]\n"
            "parampr show         (product_id)\n"
            "parampr edit         [product_id] [param_class_id] [new_value]\n"
        )

    def parampr_add(self, args):
        if len(args) < 3:
            return "Ошибка: Пожалуйста, укажите идентификаторы продукта и параметра класса, а так же значение."
        product_id = args[0]
        param_class_id = args[1]
        value = args[2]
        return self.parampr_actions.add(product_id, param_class_id, value)

    def parampr_delete(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификаторы продукта и параметра класса для удаления."
        product_id = args[0]
        param_class_id = args[1]
        return self.parampr_actions.delete(product_id, param_class_id)

    def parampr_show(self, args):
        if len(args) < 1:
            return self.parampr_actions.show()
        else:
            product_id = args[0]
            return self.parampr_actions.show(product_id)

    def parampr_edit(self, args):
        if len(args) < 3:
            return "Ошибка: Пожалуйста, укажите идентификаторы продукта и параметра класса, а так же новое значение."
        product_id = args[0]
        param_class_id = args[1]
        new_value = args[2]
        return self.parampr_actions.edit(product_id, param_class_id, new_value)
