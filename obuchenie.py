import sys


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
        self.graph = {}

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
        self.__construct_graph()
        previous_nodes, shortest_path = self.__dijkstra_algorithm(start_v)

        path = []
        link_path = []
        node = stop_v

        while node != start_v:
            a = node
            path.append(node)
            node = previous_nodes[node]
            b = Link(v1=node, v2=a)
            for x in self._links:
                if b == x:
                    link_path.append(x)

        # Добавить начальный узел вручную
        path.append(start_v)
        path.reverse()
        return path, link_path

    def __construct_graph(self):
        for node in self._vertex:
            self.graph[node] = {}

        for link in self._links:
            self.graph[link.v1][link.v2] = link.dist

    def __get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self._vertex:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def __value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        return self.graph[node1][node2]

    def __dijkstra_algorithm(self, start_v):
        unvisited_nodes = self._vertex

        # Мы будем использовать этот словарь, чтобы сэкономить на посещении каждого узла и обновлять его по мере продвижения по графику
        shortest_path = {}

        # Мы будем использовать этот dict, чтобы сохранить кратчайший известный путь к найденному узлу
        previous_nodes = {}

        # Мы будем использовать max_value для инициализации значения "бесконечности" непосещенных узлов
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # Однако мы инициализируем значение начального узла 0
        shortest_path[start_v] = 0

        # Алгоритм выполняется до тех пор, пока мы не посетим все узлы
        while unvisited_nodes:
            # Приведенный ниже блок кода находит узел с наименьшей оценкой
            current_min_node = None
            for node in unvisited_nodes:  # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            # Приведенный ниже блок кода извлекает соседей текущего узла и обновляет их расстояния
            neighbors = self.__get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + self.__value(
                    current_min_node, neighbor
                )
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node

            # После посещения его соседей мы отмечаем узел как "посещенный"
            unvisited_nodes.remove(current_min_node)

        return previous_nodes, shortest_path


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
