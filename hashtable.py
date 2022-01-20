class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.routes_dictionary = {}
        for start_city, end_city in self.edges:
            if start_city in self.routes_dictionary:
                self.routes_dictionary[start_city].append(end_city)
            else:
                self.routes_dictionary[start_city] = [end_city]

        print("Graph Dictionary:-->", self.routes_dictionary)


if __name__ == "__main__":
    routes = [
        ("Mumbai", "paris"),
        ("Mumbai", "dubai"),
        ("paris", "new york"),
        ("dubai", "new york"),
        ("new york", "toronto"),
    ]
    routes = Graph(routes)
