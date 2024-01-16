from collections import defaultdict


class Vertex:
    def __init__(self) -> None:
        self._links = []

    @property
    def links(self):
        return self._links

    # @links.setter
    # def links(self, val):
    #     self._links.append(val)


class Link:
    def __init__(self, v1: Vertex, v2: Vertex, dist: int = 1) -> None:
        self._v1 = v1
        self._v2 = v2
        self._dist = dist

    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, val):
        self._v1 = val

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, val):
        self._v2 = val

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, val):
        self._dist = val

    def __eq__(self, __o) -> bool:
        return {self.v1, self.v2} == {__o.v1, __o.v2}


class LinkedGraph:
    def __init__(self) -> None:
        self._links = []
        self._vertex = []

    def add_vertex(self, v: Vertex):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link: Link):
        if link not in self._links:
            self._links.append(link)
        self.add_vertex(link.v1)
        self.add_vertex(link.v2)
        if link.v2 not in link.v1.links:
            link.v1.links.append(link.v2)

    def find_path(self, start_v, stop_v):

        if start_v == stop_v:
            return [[start_v], [(start_v, stop_v)]]

        neighbors = self._vertex[self._links.index(start_v)]
        for neighbor, weight in neighbors:
            if neighbor not in self._vertex:
                path, connections = self.find_path(start_v, stop_v)
                if path:
                    return [
                        path + [neighbor],
                        connections + [(start_v, neighbor, weight)],
                    ]

        return [[], []]


class Station(Vertex):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class LinkMetro(Link):
    def __init__(self, v1: Station, v2: Station, dist=1) -> None:
        super().__init__(v1, v2, dist)

    def __repr__(self) -> str:
        return f"{self.v1.name}->{self.v2.name}"


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

l1 = LinkMetro(v1, v2, 1)
l2 = LinkMetro(v2, v3, 1)
map_metro.add_link(l1)
map_metro.add_link(l2)
map_metro.add_link(LinkMetro(v2, v1, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
# print("...".join([str(x) for x in map_metro._links]))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.find_path(v1, v3)


# map_metro.add_link(LinkMetro(v1, v3, 1))

# map_metro.add_link(LinkMetro(v4, v5, 1))
# map_metro.add_link(LinkMetro(v6, v7, 1))

# map_metro.add_link(LinkMetro(v2, v7, 5))
# map_metro.add_link(LinkMetro(v3, v4, 3))
# map_metro.add_link(LinkMetro(v5, v6, 3))

# quit(-1)
map2 = LinkedGraph()
v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()

map2.add_link(Link(v1, v2))
map2.add_link(Link(v2, v3))
map2.add_link(Link(v2, v4))
map2.add_link(Link(v3, v4))
map2.add_link(Link(v4, v5))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert (
    len(map2._vertex) == 5
), "неверное число вершин в списке _vertex класса LinkedGraph"

map2.add_link(Link(v2, v1))
assert (
    len(map2._links) == 5
), "метод add_link() добавил связь Link(v2, v1), хотя уже имеется связь Link(v1, v2)"

path = map2.find_path(v1, v5)
s = sum([x.dist for x in path[1]])
assert (
    s == 3
), "неверная суммарная длина маршрута, возможно, некорректно работает объект-свойство dist"

assert issubclass(Station, Vertex) and issubclass(
    LinkMetro, Link
), "класс Station должен наследоваться от класса Vertex, а класс LinkMetro от класса Link"

map2 = LinkedGraph()
v1 = Station("1")
v2 = Station("2")
v3 = Station("3")
v4 = Station("4")
v5 = Station("5")

map2.add_link(LinkMetro(v1, v2, 1))
map2.add_link(LinkMetro(v2, v3, 2))
map2.add_link(LinkMetro(v2, v4, 7))
map2.add_link(LinkMetro(v3, v4, 3))
map2.add_link(LinkMetro(v4, v5, 1))

assert len(map2._links) == 5, "неверное число связей в списке _links класса LinkedGraph"
assert (
    len(map2._vertex) == 5
), "неверное число вершин в списке _vertex класса LinkedGraph"

path = map2.find_path(v1, v5)

assert str(path[0]) == "[1, 2, 3, 4, 5]", path[0]
s = sum([x.dist for x in path[1]])
assert s == 7, "неверная суммарная длина маршрута для карты метро"
