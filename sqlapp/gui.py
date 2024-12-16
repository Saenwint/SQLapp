import customtkinter
from customtkinter import CTkFont
from handlers.enumcl import EnumClassHandler
from handlers.enumpos import EnumPosHandler
from handlers.prod import ProdHandler
from handlers.prodcl import ProdClassHandler
from handlers.unit import UnitHandler
from handlers.param import ParamHandler
from handlers.paramcl import ParamClassHandler
from handlers.parampr import ParamProdHandler

class GuiApp(customtkinter.CTk):
    def __init__(self, session):
        super().__init__()

        self.handler_enumcl = EnumClassHandler(session)
        self.handler_enumpos = EnumPosHandler(session)
        self.handler_prod = ProdHandler(session)
        self.handler_prodcl = ProdClassHandler(session)
        self.handler_unit = UnitHandler(session)
        self.handler_param = ParamHandler(session)
        self.handler_paramcl = ParamClassHandler(session)
        self.handler_parampr = ParamProdHandler(session)
        
        # Настройка окна
        self.geometry("1000x600")
        self.title("SQLAB GUI interface")
        self.resizable(False, False)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)

        self.my_font = customtkinter.CTkFont(family="Courier New", size=18)

        # Создаем поле для ввода
        self.input_field = customtkinter.CTkEntry(master=self, width=80, font=self.my_font)
        self.input_field.grid(row=0, column=0, padx=5, pady=(20, 10), sticky="ew")
        self.input_field.insert(0, "Введите команду")
        self.input_field.bind('<FocusIn>', self.clear_placeholder)
        self.input_field.bind('<FocusOut>', self.restore_placeholder)
        self.input_field.bind('<Return>', self.run_command)

        # Создаем кнопку ввода
        self.btn_enter = customtkinter.CTkButton(master=self, text="Ввод", width=50, font=self.my_font, fg_color="purple")
        self.btn_enter.grid(row=0, column=1, padx=5, pady=(20, 10), sticky="w")
        self.btn_enter.bind("<Button-1>", self.run_command)

        self.output_frame = customtkinter.CTkFrame(master=self, border_color="grey", border_width=2)
        self.output_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.output_text = customtkinter.CTkTextbox(master=self.output_frame, wrap="word", width=60, height=20, font=self.my_font)
        self.output_text.pack(expand=True, fill="both", padx=5, pady=5)
        self.output_text.configure(state="disabled")

        self.output_text.tag_config("error", foreground="red")

        self.insert_output_text("Программа запущена\nДля начала работы с программой введите 'help'\n")


    def insert_output_text(self, text, tag=None):
        self.output_text.configure(state="normal")
        if tag:
            self.output_text.insert("end", text, tag)
        else:
            self.output_text.insert("end", text)
        self.output_text.configure(state="disabled")

    def clear_output_text(self):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")

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
        self.insert_output_text("Опции:\n")
        self.insert_output_text("prodcl help   [Классы продуктов]\n")
        self.insert_output_text("prod help     [Продукты]\n")
        self.insert_output_text("enumcl help   [Перечисления]\n")
        self.insert_output_text("enumpos help  [Позиции перечислений]\n")
        self.insert_output_text("unit help     [Единицы измерений]\n")
        self.insert_output_text("param help    [Параметры]\n")
        self.insert_output_text("paramcl help  [Параметры классов]\n")
        self.insert_output_text("parampr help  [Параметры продуктов]\n")
        self.insert_output_text("exit          [Выход из программы]\n")

    def run_command(self, event):        
        self.clear_output_text()

        option = self.input_field.get().strip()
        self.insert_output_text(f"Введена команда: {option}\n")

        if not option:
            self.insert_output_text("Введите команду 'help' для получения списка команд.\n")
            return

        command, args = self.process_input(option)

        if command == "exit":
            self.insert_output_text("Выход из интерфейса командной строки...\n")
            self.quit()
            return

        elif command == "help":
            self.help()

        elif command == "prodcl":
            result = self.handler_prodcl.handle(args)
            self.insert_output_text(result)

        elif command == "prod":
            result = self.handler_prod.handle(args)
            self.insert_output_text(result)

        elif command == "enumcl":
            result = self.handler_enumcl.handle(args)
            self.insert_output_text(result)

        elif command == "enumpos":
            result = self.handler_enumpos.handle(args)
            self.insert_output_text(result)

        elif command == "unit":
            result = self.handler_unit.handle(args)
            self.insert_output_text(result)

        elif command == "param":
            result = self.handler_param.handle(args)
            self.insert_output_text(result)

        elif command == "paramcl":
            result = self.handler_paramcl.handle(args)
            self.insert_output_text(result)

        elif command == "parampr":
            result = self.handler_parampr.handle(args)
            self.insert_output_text(result)

        else:
            self.insert_output_text("Недопустимая опция. Воспользуйтесь командой 'help' для помощи.\n")

        self.input_field.delete(0, 'end')

    def clear_placeholder(self, event):
        if self.input_field.get() == "Введите команду":
            self.input_field.delete(0, "end")

    def restore_placeholder(self, event):
        if not self.input_field.get():
            self.input_field.insert(0, "Введите команду")