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
        prev = self.dijkstra(start_v, stop_v)
        # path = [stop_v]
        # while prev[path[0]] is not None:
        #     path.append(prev[path[0]])
        #     path[0] = prev[path[0]]
        # path.reverse()
        return path

    def dijkstra(self, start_v, stop_v):
        number_of_stations = len(self._links)
        # Инициализируем граф
        graph = defaultdict(list)
        # Заполняем граф: вершина -> (стоимость, вершина куда можем прийти)
        for x in self._links:
            a, b, cost = x.v1, x.v2, x.dist
            graph[a] += [(cost, b)]
        # Инициализируем список вершин для посещения
        nodes_to_visit = []
        # Добавляем нашу исходную с расстоянием равным нулю
        nodes_to_visit.append((0, start_v))
        # Инициализируем список уникальных значений для хранения вершин которые уже посетили
        visited = set()
        # Заполняем расстояния до всех остальных вершие
        min_dist = {
            self._links[i].v1: float("inf") for i in range(1, number_of_stations)
        }
        # Заполняем расстояние до текущей вершины
        min_dist[start_v] = 0
        # Проходимся по всем вершинам которые нужно посетить
        # Проходимся до тех пор, пока такие вершины есть
        while len(nodes_to_visit):
            # Берем самую близкую вершину к нам
            # cost - стоимость попадания, node - название вершины
            cost, node = min(nodes_to_visit)
            # Удаляем эту вершину из списка вершин для посещения
            nodes_to_visit.remove((cost, node))
            # Проверяем что мы в нее еще не заходили (если вдруг мы сначала добавили (9,7), а потом (6,7)
            if node in visited:
                continue
            # Добавляем в список посещенных
            visited.add(node)
            # Проходимся по всем соединенным вершинам
            # n_cost - стоимость попадания из текущей вершины, n_node - прикрепленная вершина, в которую хотим попасть
            for n_cost, n_node in graph[node]:
                print(min_dist["Чистые пруды"])
                # Проверяем нашли ли мы оптимальный путь
                if cost + n_cost < min_dist[n_node] and n_node not in visited:
                    # Если нашли то обновляем значение расстояния
                    min_dist[n_node] = cost + n_cost
                    # И добавляем эту вершину в список вершин для посещения
                    nodes_to_visit.append((cost + n_cost, n_node))

        # Выводим ответ
        print(min_dist[stop_v])


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
