from classifier.enumclassifieractions import EnumClassifierActions

class EnumClassHandler:
    def __init__(self, session):
        self.enum_cl_actions = EnumClassifierActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.enumcl_help()
        elif command == "add":
            return self.enumcl_add(args[1:])
        elif command == "delete":
            return self.enumcl_delete(args[1:])
        elif command == "show":
            return self.enumcl_show(args[1:])
        elif command == "parent":
            return self.enumcl_parent(args[1:])
        elif command == "children":
            return self.enumcl_children(args[1:])
        elif command == "positions":
            return self.enumcl_positions(args[1:])
        elif command == "chpar":
            return self.enumcl_chpar(args[1:])
        elif command == "swap":
            return self.enumcl_swap(args[1:])
        elif command == "setunit":
            return self.enumcl_setunit(args[1:])
        else:
            return "Неверная команда. Введите 'enumcl help', чтобы увидеть доступные команды."

    def enumcl_help(self):
        return (
            "enumcl help\n"
            "enumcl add          [название] (идентификатор_родителя)\n"
            "enumcl delete       [идентификатор_класса]\n"
            "enumcl show         (идентификатор_класса)\n"
            "enumcl parent       [идентификатор_класса]\n"
            "enumcl children     [идентификатор_класса]\n"
            "enumcl positions    [идентификатор_класса]\n"
            "enumcl chpar        [идентификатор_класса] [новый_идентификатор_родителя]\n"
            "enumcl swap         [идентификатор_класса1] [идентификатор_класса2]\n"
            "enumcl setunit      [идентификатор_класса] [идентификатор_ЕИ]"
        )

    def enumcl_add(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите название."
        name = args[0]
        parent_id = args[1] if len(args) > 1 else None
        return self.enum_cl_actions.add(name, parent_id)

    def enumcl_delete(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор классификатора перечисления."
        class_id = args[0]
        return self.enum_cl_actions.delete(class_id)

    def enumcl_show(self, args):
        if len(args) < 1:
            return self.enum_cl_actions.show()
        else:
            class_id = args[0]
            return self.enum_cl_actions.show(class_id)

    def enumcl_parent(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор классификатора перечисления."
        class_id = args[0]
        return self.enum_cl_actions.parent(class_id)

    def enumcl_children(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор классификатора перечисления."
        class_id = args[0]
        return self.enum_cl_actions.children(class_id)

    def enumcl_positions(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор классификатора перечисления."
        class_id = args[0]
        return self.enum_cl_actions.positions(class_id)

    def enumcl_chpar(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор классификатора перечисления и новый идентификатор родителя."
        class_id = args[0]
        new_parent_id = args[1]
        return self.enum_cl_actions.change_parent(class_id, new_parent_id)

    def enumcl_swap(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите два идентификатора классификаторов перечисления для замены."
        class_id1 = args[0]
        class_id2 = args[1]
        return self.enum_cl_actions.swap(class_id1, class_id2)
    
    def enumcl_setunit(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор класса и единицы измерения."
        class_id = args[0]
        unit_id = args[1]
        return self.enum_cl_actions.set_unit(class_id, unit_id)