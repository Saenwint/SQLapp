from classifier.paramclassactions import ParamClassClassifierActions

class ParamClassHandler:
    def __init__(self, session):
        self.paramcl_actions = ParamClassClassifierActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.paramcl_help()
        elif command == "add":
            return self.paramcl_add(args[1:])
        elif command == "delete":
            return self.paramcl_delete(args[1:])
        elif command == "set":
            return self.paramcl_set(args[1:])
        elif command == "show":
            return self.paramcl_show(args[1:])
        elif command == "showbyclass":
            return self.paramcl_show_by_class(args[1:])
        else:
            return "Неверная команда. Введите 'param help', чтобы увидеть доступные команды."

    def paramcl_help(self):
        return (
            "paramcl help\n"
            "paramcl add          [param_id] [prodclass_id] (min_value) (max_value)\n"
            "paramcl delete       [param_class_id]\n"
            "paramcl set          [param_class_id] (min_value) (max_value)\n"
            "paramcl show         (param_class_id)\n"
            "paramcl showbyclass  [prodclass_id]\n"
        )

    def paramcl_add(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите хотя бы идентификатор параметра и класса."
        paramcl_id = args[0]
        prodclass_id = args[1]
        min_value = args[2] if len(args) > 2 else None
        max_value = args[3] if len(args) > 3 else None
        return self.paramcl_actions.add(paramcl_id, prodclass_id, min_value, max_value)

    def paramcl_delete(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор параметра класса для удаления."
        paramcl_id = args[0]
        return self.paramcl_actions.delete(paramcl_id)

    def paramcl_set(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор параметра класса и значения для установки."
        paramcl_id = args[0]
        min_value = args[1] if len(args) > 1 else None
        max_value = args[2] if len(args) > 2 else None
        return self.paramcl_actions.set_paramcl(paramcl_id, min_value, max_value)

    def paramcl_show(self, args):
        if len(args) < 1:
            return self.paramcl_actions.show()
        else:
            paramcl_id = args[0]
            return self.paramcl_actions.show(paramcl_id)
    
    def paramcl_show_by_class(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор класса продукта."
        prodcl_id = args[0]
        return self.paramcl_actions.show_by_class(prodcl_id)
