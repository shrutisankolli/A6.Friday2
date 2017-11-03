import networkx as nx


class BuildingGraph():
    def __init__(self):
        # building = {building_name:{mail_address, mail_code}}
        self.buildings = {'Foreign Language Buildings': {'address': '707 S. Matthews Ave., Urbana', 'code': '164', 'access':'S. Matthews Avenue'},
                          'Davenport Hall': {'address': '607 S. Mathews, Urbana', 'code': '148', 'access':'S. Matthews Avenue'},
                          'Atmospheric Science Bldg': {'address': '103 S. Gregory, Urbana', 'code': '223', 'access': 'S. Matthews Avenue'},
                          'Observatory': {'address': '901 S. Mathews, Urbana', 'code': '190', 'access': 'S. Matthews Avenue'},
                          'Undergrad Library': {'address': '1408 W. Gregory, Urbana', 'code': '522', 'access': 'W. Gregory'},
                          'Armory': {'address': '505 E. Armory, Champaign', 'code': '532', 'access': 'S. 5th'},
                          'Ice Arena': {'address': '406 E. Armory, Champaign', 'code': '525', 'access': 'E. Armory'},
                          'Main Library': {'address': '1408 W. Gregory, Urbana', 'code': '522', 'access': 'E. Armory'},
                          'Lincoln Hall': {'address': '702 S. Wright, Urbana', 'code': '456', 'access': 'S. Wright Street'},
                          'Gregory Hall': {'address': '810 S. Wright, Urbana', 'code': '462','access': 'S. Wright Street'},
                          'Psych Bldg': {'address': '603 E. Daniel, Champaign', 'code': '716', 'access': 'S. 6th Street'},
                          'Library & Information Sci': {'address': '501 E. Daniel, Champaign', 'code': '493', 'access': 'E. Daniel Street'},
                          'SPEECH AND HEARING SCIENCE': {'address': '901 S. Sixth, Champaign', 'code': '482', 'access': 'S. 6th Street'},
                          'Illini Union BookStore': {'address': '807 S. Wright, Champaign', 'code': '323', 'access': 'S. Wright Street'},
                          'Coble Hall': {'address': '801 S. Wright, Champaign', 'code': '322', 'access': 'S. Wright Street'},
                          'Illini Hall': {'address': '721 S. Wright, Champaign', 'code': '374', 'access': 'S Wright Street'},
                          'Arcade Bldg': {'address': '620 E. John, Champaign', 'code': '303', 'access': 'S. Wright Street'},
                          'School of Nursing': {'address': '905 S. Goodwin, Urbana', 'code': '186', 'access': 'S. Goodwin Avenue'},
                          'Burrill Hall': {'address': '407 S. Goodwin, Urbana', 'code': '114', 'access': 'S Matthews Avenue'},
                          'Medical Sciences Building': {'address': '506 S. Mathews, Urbana', 'code': '714', 'access': 'S Matthews Avenue'},
                          'Chem & Life Sci Lab (CLSL)': {'address': '601 S. Goodwin, Urbana', 'code': '123', 'access': 'S Goodwin Avenue'}

                          }

        # intersection = [street_name-street_name]
        self.intersections = ['S. Goodwin-W.Gregory', 'S. Goodwin-W. Green Street', 'W. Green Street-S. Matthews Avenue',
                              'E. Green Street-S. Wright Street-W. Green Street', 'E. Green-S. 6th Street',
                              'S. 6th Street-E. Daniel Street'
                              'E. Daniel-S. Wright Street', 'S. 5th Street-E. Daniel', 'S 5th Street-E. Armory Avenue',
                              'S 6th Street-E. Armory Avenue', 'S. Wright Street-E. Armory Avenue',
                              'S. 6th Street-E. Gregory',
                              'S. Goodwin Avenue-W. Oregon Street']

        # edge = {building_name:{adjacent_node:{distance, street_name, street_direction}}}
        self.edges = {'Foreign Language Buildings': {
            'S.Goodwin-W.Gregory': {'distance': 100, 'name': 'S.Goodwin', 'direction': 'East'},
            'S.Goodwin-W.Green Street': {'distance': 200, 'name': 'S.Goodwin', 'direction': 'West'}},
                      'S.Goodwin-W.Gregory': {
                          'Davenport Hall': {'distance': 400, 'name': 'W.Gregory', 'direction': 'North'}},
                      'S.Goodwin-W.Green Street': {
                          'Davenport Hall': {'distance': 200, 'name': 'W.Green', 'direction': 'South'}}

                      }

    def add_building_nodes(self, G):
        for name, attributes in self.buildings.items():
            G.add_node(name, address = attributes['address'], code = attributes['code'], access = attributes['access'])
        return (G)

    def add_intersection_nodes(self, G):
        for name in self.intersections:
            G.add_node(name)
        return (G)

    def add_edges(self, G):
        for node, adjacent in self.edges.items():
            for adjacent_node, adjacent_info in adjacent.items():
                G.add_edge(node, adjacent_node, distance=adjacent_info['distance'], name=adjacent_info['name'],
                           direstion=adjacent_info['direction'])
        return (G)

H = nx.DiGraph()
Buildings = BuildingGraph()
H = Buildings.add_building_nodes(H)
H = Buildings.add_intersection_nodes(H)
H = Buildings.add_edges(H)
print(H.adj)
print(nx.shortest_path(H, 'Foreign Language Buildings', 'Davenport Hall', weight = 'distance'))