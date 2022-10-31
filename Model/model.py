from dataclasses import dataclass


@dataclass
class Sportsman:
    sportsman_name: str = 'sportsman_name'
    sportsman_last_name: str = 'sportsman_last_name'
    sportsman_patronymic: str = 'sportsman_patronymic'
    compound: str = 'compound'
    type_of_sport: str = 'type_of_sport'
    position: int = 0
    number_of_titles: int = 0
    category: str = 'category'

