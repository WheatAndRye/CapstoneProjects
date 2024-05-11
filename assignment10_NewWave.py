class Game:
    def __init__(self, title, genre, developer, year):
        self._title = str(title)
        self._genre = str(genre)
        self._developer = str(developer)
        self._year = int(year)

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre

    def get_developer(self):
        return self._developer

    def get_year(self):
        return self._year

class Console:
    def __init__(self, name):
        self._name = str(name)
        self._catalog = {}

    def get_name(self):
        return self._name

    def get_catalog(self):
        return self._catalog

    def add_game(self, game):
        self._catalog[game.get_title()] = game

    def delete_game(self, title):
        if title in self._catalog:
            del self._catalog[title]

class Availability:
    def __init__(self):
        self._consoleList = []

    def add_console(self, console):
        self._consoleList.append(console)

    def delete_console(self, name):
        for console in self._consoleList:
            if console.get_name == name:
                self._consoleList.remove(console)

    def where_to_play(self, title):
        ret = []
        added_titles = set()
        for console in self._consoleList:
            catalog = console.get_catalog()
            if title in catalog:
                game = catalog[title]
                if game.get_title() not in added_titles:
                    ret.append(f"{game.get_title()} ({game.get_year()})")
                    added_titles.add(game.get_title())
                ret.append(console.get_name())
        return ret

game_1 = Game('Wild Arms', 'Weird Western RPG', 'Media.Vision', 1996)
game_2 = Game('Fallout', 'Sci-Fi RPG', 'Interplay', 1997)
game_3 = Game('Dead Space', 'Survival Horror Shooter', 'Visceral Games', 2007)
game_4 = Game('Stardew Valley', 'Farming Simulator', 'Concerned Ape', 2016)
game_5 = Game('Galerians', 'Survival Horror', 'Polygon Magic', 1999)
game_6 = Game('Fallout: New Vegas', 'Sci-Fi RPG', 'Obsidian', 2010)
game_7 = Game('Viva Pinata', 'Pinata Management Simulator', 'Rare', 2006)


console_1 = Console('PC')
console_1.add_game(game_2)
console_1.add_game(game_3)
console_1.add_game(game_6)

console_2 = Console('Playstation 1')
console_2.add_game(game_1)
console_2.add_game(game_4)
console_2.delete_game('Stardew Valley')
console_2.add_game(game_5)

console_3 = Console('Xbox 360')
console_3.add_game(game_3)
console_3.add_game(game_6)
console_3.add_game(game_7)

play_guide = Availability()
play_guide.add_console(console_2)
play_guide.add_console(console_1)
play_guide.add_console(console_3)
play_guide.delete_console('Playstation 1')
search_results = play_guide.where_to_play('Fallout: New Vegas')
print(search_results)




