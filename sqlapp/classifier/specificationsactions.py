from models.specification_line import SpecificationLine
from models.product import Product


class SpecificationActions:
    def __init__(self, session):
        self.session = session

    def add_line(self, product_id, component_id, quantity):
        try:
            new_line = SpecificationLine(product_id=product_id, component_id=component_id, quantity=quantity)
            self.session.add(new_line)
            self.session.commit()
            return "Строка спецификации успешно добавлена!"
        except Exception as e:
            self.session.rollback()
            return f"Ошибка: Не удалось добавить строку спецификации. {str(e)}"

    def delete_line(self, line_id):
        try:
            line = self.session.query(SpecificationLine).get(line_id)
            if line:
                self.session.delete(line)
                self.session.commit()
                return "Строка спецификации успешно удалена!"
            else:
                return "Строка спецификации не найдена."
        except Exception as e:
            self.session.rollback()
            return f"Ошибка: Не удалось удалить строку спецификации. {str(e)}"

    def show_lines(self, product_id):
        try:
            lines = self.session.query(SpecificationLine).filter_by(product_id=product_id).all()
            if lines:
                result = "Строки спецификации:\n"
                for line in lines:
                    result += f"{line}\n"
                return result
            else:
                return "Строки спецификации не найдены."
        except Exception as e:
            return f"Ошибка: Не удалось получить строки спецификации. {str(e)}"

    def find_all_lines(self, product_id):
        try:
            lines = self.session.query(SpecificationLine).filter_by(product_id=product_id).all()
            result = []
            for line in lines:
                result.append(str(line))
                result.extend(self.find_all_lines(line.component_id))
            return "\n".join(result)
        except Exception as e:
            return f"Ошибка: Не удалось найти все строки спецификации. {str(e)}"

    def calculate_summary_norms(self, product_id, resource_class_id):
        try:
            print(f"Calculating summary norms for product_id={product_id}, resource_class_id={resource_class_id}")
            
            lines = self.session.query(SpecificationLine).filter_by(product_id=product_id).all()
            print(f"Found {len(lines)} lines for product_id={product_id}")
            
            summary_norms = {}
            for line in lines:
                component = self.session.query(Product).get(line.component_id)
                print(f"Checking component_id={line.component_id}, component_class_id={component.prod_class_id}")
                
                if component.prod_class_id == resource_class_id:
                    print(f"Component_id={line.component_id} belongs to resource_class_id={resource_class_id}")
                    if component.id_product in summary_norms:
                        summary_norms[component.id_product] += line.quantity
                    else:
                        summary_norms[component.id_product] = line.quantity
            
            result = "Сводные нормы расхода:\n"
            for component_id, quantity in summary_norms.items():
                result += f"Компонент_ID={component_id}, Количество={quantity}\n"
            
            print(result)
            return result
        except Exception as e:
            return f"Ошибка: Не удалось рассчитать сводные нормы расхода. {str(e)}"