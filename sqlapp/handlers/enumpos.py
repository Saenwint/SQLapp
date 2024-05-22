from classifier.enumpositionactions import EnumPositionActions

class EnumPosHandler:
    def __init__(self, session):
        self.enum_pos_actions = EnumPositionActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.enumpos_help()
        elif command == "add":
            return self.enumpos_add(args[1:])
        elif command == "delete":
            return self.enumpos_delete(args[1:])
        elif command == "show":
            return self.enumpos_show(args[1:])
        elif command == "swap":
            return self.enumpos_swap(args[1:])
        else:
            return "Неверная команда. Введите 'enumpos help', чтобы увидеть доступные команды."

    def enumpos_help(self):
        return (
            "enumpos help\n"
            "enumpos add          [название] [короткое_название] [идентификатор_классификатора] [тип_значения] [значение]\n"
            "enumpos delete       [идентификатор_позиции]\n"
            "enumpos show         (идентификатор_позиции)\n"
            "enumpos swap         [идентификатор_позиции1] [идентификатор_позиции2]"
        )

    def enumpos_add(self, args):
        if len(args) < 5:
            return "Ошибка: Пожалуйста, укажите название, короткое название, идентификатор классификатора, тип значения и значение."
        name = args[0]
        short_name = args[1]
        classifier_id = args[2]
        value_type = args[3]
        value = args[4]
        return self.enum_pos_actions.add(name, short_name, classifier_id, value_type, value)

    def enumpos_delete(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор позиции перечисления."
        pos_id = args[0]
        return self.enum_pos_actions.delete(pos_id)

    def enumpos_show(self, args):
        if len(args) < 1:
            return self.enum_pos_actions.show()
        else:
            pos_id = args[0]
            return self.enum_pos_actions.show(pos_id)

    def enumpos_swap(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите два идентификатора позиций перечисления для замены."
        pos_id1 = args[0]
        pos_id2 = args[1]
        return self.enum_pos_actions.swap(pos_id1, pos_id2)
