from classifier.productactions import ProductActions

class ProdHandler:
    def __init__(self, session):
        self.product_actions = ProductActions(session)

    def handle(self, args):
        if len(args) < 1:
            return "Недопустимая команда. Пожалуйста, укажите команду."

        command = args[0]
        if command == "help":
            return self.prod_help()
        elif command == "add":
            return self.prod_add(args[1:])
        elif command == "del":
            return self.prod_del(args[1:])
        elif command == "show":
            return self.prod_show(args[1:])
        elif command == "setprod":
            return self.prod_setprod(args[1:])
        elif command == "setenum":
            return self.prod_setenum(args[1:])
        elif command == "showbyprod":
            return self.prod_show_byprod(args[1:])
        elif command == "showbyenum":
            return self.prod_show_byenum(args[1:])
        elif command == "checkcl":
            return self.prod_checkcl(args[1:])
        else:
            return "Недопустимая команда. Введите 'prod help', чтобы увидеть доступные команды."

    def prod_help(self):
        return (
            "prod help\n"
            "prod add            [product_name] (prod_class_id) (enum_class_id)\n"
            "prod del            [product_id]\n"
            "prod show           (product_id)\n"
            "prod showbyprod     [prod_class_id]\n"
            "prod showbyenum     [enum_class_id]\n"
            "prod setclass       [product_id] [prod_class_id]\n"
            "prod setenum        [product_id] [enum_class_id]\n"
            "prod checkcl        [product_id] [prod_class_id]\n"
        )

    def prod_add(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите хотя бы название продукта."
        product_name = args[0]
        prod_class_id = args[1] if len(args) > 1 else None
        enum_class_id = args[2] if len(args) > 2 else None
        return self.product_actions.add(product_name, prod_class_id, enum_class_id)

    def prod_del(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта."
        product_id = args[0]
        return self.product_actions.delete(product_id)

    def prod_show(self, args):
        if len(args) < 1:
            return self.product_actions.show()
        else:
            product_id = args[0]
            return self.product_actions.show(product_id)

    def prod_setprod(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта и идентификатор класса продукта."
        product_id = args[0]
        prod_class_id = args[1]
        return self.product_actions.set_class(product_id, prod_class_id)

    def prod_setenum(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта и идентификатор класса перечисления."
        product_id = args[0]
        enum_class_id = args[1]
        return self.product_actions.set_enum(product_id, enum_class_id)

    def prod_show_byprod(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор класса продукта."
        prod_class_id = args[0]
        return self.product_actions.show_by_prod_class(prod_class_id)

    def prod_show_byenum(self, args):
        if len(args) < 1:
            return "Ошибка: Пожалуйста, укажите идентификатор класса перечисления."
        enum_class_id = args[0]
        return self.product_actions.show_by_enum_class(enum_class_id)

    def prod_checkcl(self, args):
        if len(args) < 2:
            return "Ошибка: Пожалуйста, укажите идентификатор продукта и идентификатор класса продукта."
        product_id = args[0]
        prod_class_id = args[1]
        return self.product_actions.check_class(product_id, prod_class_id)
