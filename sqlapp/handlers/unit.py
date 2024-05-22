from classifier.unitactions import UnitActions

class UnitHandler:
    def __init__(self, session):
        self.unit_actions = UnitActions(session)

    def handle(self, args):
        if len(args) < 1:
            print("Неверная команда. Пожалуйста, укажите команду.")
            return

        command = args[0]
        if command == "help":
            return self.unit_help()
        elif command == "add":
            return self.unit_add(args[1:])
        elif command == "del":
            return self.unit_del(args[1:])
        elif command == "show":
            return self.unit_show(args[1:])
        else:
            return "Неверная команда. Введите 'unit help', чтобы увидеть доступные команды."

    def unit_help(self):
        return (
            "unit help\n"
            "unit add     [unit_name] [short_name]\n"
            "unit del     [unit_id]\n"
            "unit show    (unit_id)\n"
        )

    def unit_add(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите название единицы и короткое название."
        unit_name = args[0]
        short_name = args[1]
        return self.unit_actions.add(unit_name, short_name)

    def unit_del(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор единицы."
        unit_id = args[0]
        return self.unit_actions.delete(unit_id)

    def unit_show(self, args):
        if len(args) < 1:
            return self.unit_actions.show()
        else:
            unit_id = args[0]
            return self.unit_actions.show(unit_id)
