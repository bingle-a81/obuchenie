class Vertex:
    def __init__(self) -> None:
        self._links = []

    @property
    def links(self):
        print(self._links)
        return self._links

    @links.setter
    def links(self, val):
        self._links.append(val)


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
        a = {self.v1, self.v2}
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
        link.v1.links.append(v2)
        # link.v2.links.append(v1)

    def find_path(self, start_v, stop_v):
        pass


class Station(Vertex):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist=1) -> None:
        super().__init__(v1, v2, dist)


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 1))
# print(map_metro._vertex)
# print(map_metro._vertex[1].links)

quit(-1)
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))
