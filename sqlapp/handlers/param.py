from classifier.paramactions import ParamClassifierActions

class ParamHandler:
    def __init__(self, session):
        self.param_actions = ParamClassifierActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.param_help()
        elif command == "add":
            return self.param_add(args[1:])
        elif command == "delete":
            return self.param_delete(args[1:])
        elif command == "show":
            return self.param_show(args[1:])
        else:
            return "Неверная команда. Введите 'param help', чтобы увидеть доступные команды."

    def param_help(self):
        return (
            "param help\n"
            "param add          [name] [short_name] (unit_id) (enum_cl_id)\n"
            "param delete       [param_id]\n"
            "param show         (param_id)\n"
        )

    def param_add(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите хотя бы название параметра и его короткое имя."
        name = args[0]
        short_name = args[1]
        unit_id = args[2] if len(args) > 2 else None
        enum_cl_id = args[3] if len(args) > 3 else None
        return self.param_actions.add(name, short_name, unit_id, enum_cl_id)

    def param_delete(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор параметра для удаления."
        param_id = args[0]
        return self.param_actions.delete(param_id)

    def param_show(self, args):
        if len(args) < 1:
            return self.param_actions.show()
        else:
            param_id = args[0]
            return self.param_actions.show(param_id)
