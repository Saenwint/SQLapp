from classifier.prodclassactions import ProdClassActions

class ProdClassHandler:
    def __init__(self, session):
        self.prod_class_actions = ProdClassActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Неверная команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.prodcl_help()
        elif command == "add":
            return self.prodcl_add(args[1:])
        elif command == "del":
            return self.prodcl_del(args[1:])
        elif command == "show":
            return self.prodcl_show(args[1:])
        elif command == "parent":
            return self.prodcl_parent(args[1:])
        elif command == "children":
            return self.prodcl_children(args[1:])
        elif command == "chpar":
            return self.prodcl_chpar(args[1:])
        elif command == "setunit":
            return self.prodcl_setunit(args[1:])
        elif command == "swap":
            return self.prodcl_swap(args[1:])
        else:
            return "Неверная команда. Введите 'prodcl help', чтобы увидеть доступные команды."

    def prodcl_help(self):
        help_text = (
            "prodcl help\n"
            "prodcl add         [class_name] (unit_id) (parent_id)\n"
            "prodcl del         [class_id]\n"
            "prodcl show        (class_id)\n"
            "prodcl parent      [class_id]\n"
            "prodcl children    [class_id]\n"
            "prodcl chpar       [class_id] [parent_id]\n"
            "prodcl setunit     [class_id]\n"
            "prodcl swap        [class_id1] [class_id2]\n"
        )
        return help_text

    def prodcl_add(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите название класса."
        class_name = args[0]
        unit_id = args[1] if len(args) > 1 else None
        parent_id = args[2] if len(args) > 2 else None
        return self.prod_class_actions.add(class_name, unit_id, parent_id)

    def prodcl_del(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор класса."
        class_id = args[0]
        return self.prod_class_actions.delete(class_id)

    def prodcl_show(self, args):
        if len(args) < 1:
            return self.prod_class_actions.show()
        else:
            class_id = args[0]
            return self.prod_class_actions.show(class_id)

    def prodcl_parent(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор класса."
        class_id = args[0]
        return self.prod_class_actions.parent(class_id)

    def prodcl_children(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор класса."
        class_id = args[0]
        return self.prod_class_actions.children(class_id)

    def prodcl_chpar(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор класса и новый идентификатор родительского класса."
        
        class_id = args[0]
        parent_id = args[1]
        try:
            class_id = int(class_id)
            parent_id = int(parent_id)
            return self.prod_class_actions.change_parent(class_id, parent_id)
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"

    def prodcl_setunit(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор класса и идентификатор единицы."
        class_id = args[0]
        unit_id = args[1]
        return self.prod_class_actions.set_unit(class_id, unit_id)

    def prodcl_swap(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите два идентификатора класса."
        class_id1 = args[0]
        class_id2 = args[1]
        return self.prod_class_actions.swap(class_id1, class_id2)
