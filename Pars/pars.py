import xml.dom.minidom as minidom
import xml.sax


class Reader(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.data_table = []
        self.sportsman_data = []
        self.parser = xml.sax.make_parser()

    def startElement(self, name, attrs):
        self.current = name
        if name == "sportsman":
            pass

    def characters(self, content):
        if self.current == "sportsman_name":
            self.sportsman_name = content
        elif self.current == "sportsman_last_name":
            self.sportsman_last_name = content
        elif self.current == "sportsman_patronymic":
            self.sportsman_patronymic = content
        elif self.current == "compound":
            self.compound = content
        elif self.current == "type_of_sport":
            self.type_of_sport = content
        elif self.current == "position":
            self.position = content
        elif self.current == "number_of_titles":
            self.number_of_titles = content
        elif self.current == "category":
            self.category = content

    def endElement(self, name):
        if self.current == "sportsman_name":
            self.sportsman_data.append(self.sportsman_name)
        elif self.current == "sportsman_last_name":
            self.sportsman_data.append(self.sportsman_last_name)
        elif self.current == "sportsman_patronymic":
            self.sportsman_data.append(self.sportsman_patronymic)
        elif self.current == "compound":
            self.sportsman_data.append(self.compound)
        elif self.current == "type_of_sport":
            self.sportsman_data.append(self.type_of_sport)
        elif self.current == "position":
            self.sportsman_data.append(self.position)
        elif self.current == "number_of_titles":
            self.sportsman_data.append(self.number_of_titles)
        elif self.current == "category":
            self.sportsman_data.append(self.category)
        if len(self.sportsman_data) == 8:
            self.data_table.append(tuple(self.sportsman_data))
            self.sportsman_data = []
        self.current = ""


class Writer:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dom_tree = minidom.Document()
        self.rows = []

    def create_xml_sportsman(self, data):
        book = self.dom_tree.createElement("sportsman")

        for value in data:
            temp_child = self.dom_tree.createElement(value)
            book.appendChild(temp_child)
            node_text = self.dom_tree.createTextNode(str(data[value]))
            temp_child.appendChild(node_text)

        self.rows.append(book)

    def create_xml_file(self):
        pass_table = self.dom_tree.createElement("pass_table")
        for sportsman in self.rows:
            pass_table.appendChild(sportsman)
        self.dom_tree.appendChild(pass_table)
        self.dom_tree.writexml(open(self.file_name, 'w'),
                               indent="  ",
                               addindent="  ",
                               newl='\n')
        self.dom_tree.unlink()


d = Reader()
print(d)
