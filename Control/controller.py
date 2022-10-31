import xml.sax
from Pars.pars import Reader, Writer
from Model.model import Sportsman


class DataBaseController:

    def __init__(self, file):
        self._reader = Reader()
        self._writer = Writer(file)
        self._list_of_sportsmen = list()
        self.read_from_file(file)

    def add_(self, sportsman):
        self._list_of_sportsmen.append(sportsman)

    def get_all_(self):
        return self._list_of_sportsmen

    def search_by_sportsman_fio_or_type_of_sport(self, inf):
        found_items = list()
        for i in self._list_of_sportsmen:
            if (i.sportsman_name == inf.split()[0] and i.sportsman_last_name == inf.split()[
                1] and i.sportsman_patronymic == inf.split()[2]) or i.type_of_sport == inf:
                found_items.append(i)
        return found_items

    def search_by_number_of_titles(self, number_of_titles):
        found_items = list()
        for i in self._list_of_sportsmen:
            if int(i.number_of_titles) == number_of_titles:
                found_items.append(i)
        return found_items

    def search_by_sportsman_fio_or_category(self, inf):
        found_items = list()
        for i in self._list_of_sportsmen:
            if (i.sportsman_name == inf.split()[0] and i.sportsman_last_name == inf.split()[
                1] and i.sportsman_patronymic == inf.split()[2]) or i.category == inf:
                found_items.append(i)
        return found_items

    def delete_by_sportsman_fio_or_type_of_sport(self, inf):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_sportsmen)):
            if (self._list_of_sportsmen[index].sportsman_name == inf.split()[0] and self._list_of_sportsmen[
                index].sportsman_last_name == inf.split()[1] \
                and self._list_of_sportsmen[index].sportsman_patronymic == inf.split()[2]) \
                    or self._list_of_sportsmen[index].type_of_sport == inf:
                self._list_of_sportsmen.remove(self._list_of_sportsmen[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_sportsman_fio_or_category(self, inf):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_sportsmen)):
            if (self._list_of_sportsmen[index].sportsman_name == inf.split()[0] and self._list_of_sportsmen[
                index].sportsman_last_name == inf.split()[1] \
                and self._list_of_sportsmen[index].sportsman_patronymic == inf.split()[2]) \
                    or self._list_of_sportsmen[index].category == inf:
                self._list_of_sportsmen.remove(self._list_of_sportsmen[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def delete_by_number_of_titles(self, input_):
        counter = 0
        index = 0
        for _ in range(len(self._list_of_sportsmen)):
            if int(self._list_of_sportsmen[index].number_of_titles) == int(input_):
                self._list_of_sportsmen.remove(self._list_of_sportsmen[index])
                counter += 1
            else:
                index += 1
        return True if counter > 0 else False

    def write_data_into_file(self):
        for i in self._list_of_sportsmen:
            self._writer.create_xml_sportsman({
                "sportsman_name": i.sportsman_name,
                "sportsman_last_name": i.sportsman_last_name,
                "sportsman_patronymic": i.sportsman_patronymic,
                "compound": i.compound,
                "type_of_sport": i.type_of_sport,
                "position": i.position,
                "number_of_titles": int(i.number_of_titles),
                "category": i.category,
            })
        self._writer.create_xml_file()

    def read_from_file(self, file):
        parser = xml.sax.make_parser()
        parser.setContentHandler(self._reader)
        parser.parse(file)
        for i in self._reader.data_table:
            self._list_of_sportsmen.append(Sportsman(
                i[0], i[1], i[2], i[3],
                i[4], i[5], i[6], i[7]
            ))
