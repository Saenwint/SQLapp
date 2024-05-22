from handlers.enumcl import EnumClassHandler
from handlers.enumpos import EnumPosHandler
from handlers.prod import ProdHandler
from handlers.prodcl import ProdClassHandler
from handlers.unit import UnitHandler
from handlers.param import ParamHandler
from handlers.paramcl import ParamClassHandler
from handlers.parampr import ParamProdHandler

class CLInterface:
    def __init__(self, session):
        self.handler_enumcl = EnumClassHandler(session)
        self.handler_enumpos = EnumPosHandler(session)
        self.handler_prod = ProdHandler(session)
        self.handler_prodcl = ProdClassHandler(session)
        self.handler_unit = UnitHandler(session)
        self.handler_param = ParamHandler(session)
        self.handler_paramcl = ParamClassHandler(session)
        self.handler_parampr = ParamProdHandler(session)

    def process_input(self, option):
        processed_args = []

        in_quotes = False

        current_arg = ""

        for char in option:
            if char == '"':
                in_quotes = not in_quotes
            elif char == " " and not in_quotes:
                if current_arg:
                    processed_args.append(current_arg)
                    current_arg = ""
            else:
                current_arg += char

        if current_arg:
            processed_args.append(current_arg)

        command = processed_args[0]
        arguments = processed_args[1:]

        return command, arguments

    def help(self):
        print("Опции:")
        print("prodcl help")
        print("prod help")
        print("enumcl help")
        print("enumpos help")
        print("unit help")
        print("param help")
        print("paramcl help")
        print("parampr help")
        print("exit")

    def startcli(self):
        print("Запущен интерфейс командной строки.")
        print("Управление справочником. Введите 'help' для списка команд.")

        while True:
            option = input("\033[94m>>\033[0m ")

            command, args = self.process_input(option)

            if command == "exit":
                print("Выход из интерфейса командной строки...")
                break

            elif command == "help":
                self.help()

            elif command == "prodcl":
                self.handler_prodcl.handle(args)

            elif command == "prod":
                self.handler_prod.handle(args)

            elif command == "enumcl":
                self.handler_enumcl.handle(args)

            elif command == "enumpos":
                self.handler_enumpos.handle(args)

            elif command == "unit":
                self.handler_unit.handle(args)

            elif command == "param":
                self.handler_param.handle(args)

            elif command == "paramcl":
                self.handler_paramcl.handle(args)

            elif command == "parampr":
                self.handler_parampr.handle(args)

            else:
                print("Недопустимая опция. Воспользуйтесь командой 'help' для помощи.")
