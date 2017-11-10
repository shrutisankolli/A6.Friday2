import networkx as nx
import pandas as pd
from pandas import DataFrame as df

class BuildingGraph():
    def __init__(self):
        # building = {building_name:{mail_address, mail_code}}
        self.buildings = {'Foreign Language Buildings': {'address': '707 S. Matthews Ave., Urbana', 'code': '164', 'access':'S. Matthews Avenue'},
                          'Davenport Hall': {'address': '607 S. Mathews, Urbana', 'code': '148', 'access':'S. Matthews Avenue'},
                          'Atmospheric Science Bldg': {'address': '103 S. Gregory, Urbana', 'code': '223', 'access': 'S. Matthews Avenue'},
                          'Observatory': {'address': '901 S. Mathews, Urbana', 'code': '190', 'access': 'S. Matthews Avenue'},
                          'Undergrad Library': {'address': '1408 W. Gregory, Urbana', 'code': '522', 'access': 'W. Gregory'},
                          'Armory': {'address': '505 E. Armory, Champaign', 'code': '532', 'access': 'E. Armory'},
                          'Ice Arena': {'address': '406 E. Armory, Champaign', 'code': '525', 'access': 'S. 5th Street'},
                          'Lincoln Hall': {'address': '702 S. Wright, Urbana', 'code': '456', 'access': 'S. Wright Street'},
                          'Gregory Hall': {'address': '810 S. Wright, Urbana', 'code': '462','access': 'S. Wright Street'},
                          'Psych Bldg': {'address': '603 E. Daniel, Champaign', 'code': '716', 'access': 'S. 6th Street'},
                          'Library & Information Sci': {'address': '501 E. Daniel, Champaign', 'code': '493', 'access': 'E. Daniel Street'},
                          'SPEECH AND HEARING SCIENCE': {'address': '901 S. Sixth, Champaign', 'code': '482', 'access': 'E. Daniel Street'},
                          'Illini Union BookStore': {'address': '807 S. Wright, Champaign', 'code': '323', 'access': 'S. Wright Street'},
                          'Coble Hall': {'address': '801 S. Wright, Champaign', 'code': '322', 'access': 'S. Wright Street'},
                          'Illini Hall': {'address': '721 S. Wright, Champaign', 'code': '374', 'access': 'S Wright Street'},
                          'Arcade Bldg': {'address': '620 E. John, Champaign', 'code': '303', 'access': 'S. Wright Street'},
                          'School of Nursing': {'address': '905 S. Goodwin, Urbana', 'code': '186', 'access': 'S. Goodwin'},
                          'Burrill Hall': {'address': '407 S. Goodwin, Urbana', 'code': '114', 'access': 'S. Goodwin'},
                          'Medical Sciences Building': {'address': '506 S. Mathews, Urbana', 'code': '714', 'access': 'S Matthews Avenue'},
                          'Chem & Life Sci Lab (CLSL)': {'address': '601 S. Goodwin, Urbana', 'code': '123', 'access': 'S Goodwin'},
                          'Altgeld Hall': {'address': '1409 W. Green, Urbana', 'code': '382', 'access': 'S. Wright Street'}
                          }

        # intersection = [street_name-street_name]
        self.intersections = ['S. Goodwin-W. Gregory', 'S. Goodwin-W. Green Street', 'W. Green Street-S. Matthews Avenue',
                              'E. Green Street-S. Wright Street-W. Green Street', 'E. Green-S. 6th Street',
                              'S. 6th Street-E. Daniel',
                              'E. Daniel-S. Wright Street', 'S. 5th Street-E. Daniel',
                              'S 6th Street-E. Armory', 'S. Wright Street-E. Armory',
                              'S. 6th Street-E. Gregory',
                              'S. Goodwin-W. Oregon Street']

        # edge = {building_name:{adjacent_node:{distance, street_name, street_direction}}}
        self.edges = {
            'Foreign Language Buildings': {
                'Davenport Hall': {'distance': 370, 'name': 'S. Matthews Avenue', 'direction': 'North'},
                'Observatory': {'distance': 378, 'name': 'S. Matthews Avenue', 'direction': 'South'}},
            'Davenport Hall':{
                'Foreign Language Buildings':{'distance': 370, 'name': 'S. Matthews Avenue', 'direction': 'South'},
                'Medical Sciences Building':{'distance': 430, 'name': 'S. Matthews Avenue', 'direction': 'North'}},
            'Atmospheric Science Bldg':{
                'Medical Sciences Building':{'distance': 266, 'name': 'S. Matthews Avenue', 'direction': 'South'},
                'W. Green Street-S. Matthews Avenue':{'distance': 420, 'name': 'S. Matthews Avenue', 'direction': 'North'}},
            'Observatory':{
                'Foreign Language Buildings':{'distance': 378, 'name': 'S. Matthews Avenue', 'direction': 'North'}},
            'Undergrad Library':{
                'S. Goodwin-W. Gregory':{'distance': 941, 'name': 'W. Gregory', 'direction': 'East'},
                'Main Library':{'distance': 490, 'name': 'W. Gregory', 'direction': 'West'}},
            'Armory':{
                'S 6th Street-E. Armory':{'distance': 456, 'name': 'E. Armory', 'direction': 'East'},
                'Ice Arena':{'distance': 154, 'name': 'E. Armory', 'direction': 'North'}},
            'Ice Arena':{
                'Armory':{'distance': 154, 'name': 'S. 5th Street', 'direction': 'South'},
                'S. 5th Street-E. Daniel':{'distance': 775, 'name': 'S. 5th Street', 'direction': 'North'}},
            'Main Library':{
                'Undergrad Library':{'distance': 490, 'name': 'E. Gregory', 'direction': 'East'},
                'S. 6th Street-E. Gregory':{'distance': 360, 'name': 'E. Gregory', 'direction': 'West'}},
            'Lincoln Hall':{
                'E. Daniel-S. Wright Street':{'distance': 509, 'name': 'S. Wright Street', 'direction': 'North'},
                'Gregory Hall':{'distance': 402, 'name': 'S. Wright Street', 'direction': 'South'}},
            'Gregory Hall':{
                'Lincoln Hall':{'distance': 402, 'name': 'S. Wright Street', 'direction': 'North'},
                'S 6th Street-E. Armory':{'distance': 405, 'name': 'S. Wright Street', 'direction': 'West'}},
            'Psych Bldg':{
                'S 6th Street-E. Armory':{'distance': 743, 'name': 'S. 6th Street', 'direction': 'South'},
                'S. 6th Street-E. Daniel':{'distance': 180, 'name': 'S. 6th Street', 'direction': 'North'}},
            'Library & Information Sci':{
                'S. 5th Street-E. Daniel':{'distance': 129, 'name': 'E. Daniel', 'direction': 'West'},
                'SPEECH AND HEARING SCIENCE':{'distance': 250, 'name': 'E. Daniel', 'direction': 'East'}},
            'SPEECH AND HEARING SCIENCE':{
                'Library & Information Sci':{'distance': 250, 'name': 'E. Daniel', 'direction': 'West'},
                'S. 6th Street-E. Daniel':{'distance': 90, 'name': 'E. Daniel', 'direction': 'East'}},
            'Illini Union BookStore':{
                'E. Daniel-S. Wright Street':{'distance': 117, 'name': 'S. Wright Street', 'direction': 'South'},
                'Coble Hall':{'distance': 157, 'name': 'S. Wright Street', 'direction': 'North'}},
            'Coble Hall':{
                'Illini Union BookStore':{'distance': 157, 'name': 'S. Wright Street', 'direction': 'South'},
                'Illini Hall':{'distance': 268, 'name': 'S. Wright Street', 'direction': 'North'}},
            'Illini Hall':{
                'Coble Hall':{'distance': 268, 'name': 'S. Wright Street', 'direction': 'South'},
                'Arcade Bldg':{'distance': 121, 'name': 'S. Wright Street', 'direction': 'North'}},
            'Arcade Bldg':{
                'Illini Hall':{'distance': 121, 'name': 'S. Wright Street', 'direction': 'South'},
                'E. Green Street-S. Wright Street-W. Green Street':{'distance': 192, 'name': 'S. Wright Street', 'direction': 'North'}},
            'School of Nursing':{
                'S. Goodwin-W. Green Street':{'distance':433,'name': 'S. Goodwin Ave', 'direction': 'South'},
                'Burill Hall':{'distance': 435, 'name': 'S. Goodwin Ave', 'direction': 'South'}},
            'Burill Hall':{
                'School of Nursing':{'distance':197, 'name': 'S. Goodwin Ave', 'direction': 'South'},
                'Medical Sciences Building':{'distance':99999, 'name': 'S. Goodwin Ave', 'direction': 'South'}},
            'Medical Sciences Building':{
                'Burill Hall':{'distance':99999, 'name': 'S. Goodwin Ave', 'direction': 'South'},
                'Chemical and Life Sciences Laboratory':{'distance':15, 'name': 'S. Goodwin Ave', 'direction': 'South'}},
            'Chemical and Life Sciences Laboratory':{
                'Medical Sciences Building':{'distance':15, 'name': 'S. Goodwin Ave', 'direction': 'South'},
                'S. Goodwin Ave-W. Oregon Street':{'distance':387, 'name': 'S. Goodwin Ave', 'direction': 'South'}},
            'S. Goodwin Ave-W. Oregon Street':{
                'Chemical and Life Sciences Laboratory':{'distance':387, 'name': 'S. Goodwin Ave', 'direction': 'South'},
                'S. Goodwin-W. Gregory':{'distance':1000, 'name': 'S. Goodwin Ave', 'direction': 'South'}},
            'S. Goodwin-W. Gregory':{
                'S. Goodwin Ave-W. Oregon Street':{'distance':1000, 'name': 'S. Goodwin Ave', 'direction': 'South'},
                'UGL':{'distance':876, 'name': 'W. Gregory', 'direction': 'West'}},
            'S. 6th Street-E. Gregory':{
                'UGL':{'distance':850, 'name': 'W. Gregory', 'direction': 'West'},
                'Armory':{'distance':915, 'name': 'S. 6th Street', 'direction': 'West'}},
            'S 6th Street-E. Armory Avenue':{
                'Armory':{'distance':95, 'name': 'S. 6th Street', 'direction': 'North'},
                'S 5th Street-E. Armory Avenue':{'distance':456, 'name': 'E. Armory Avenue', 'direction': 'West'}},
            'S 5th Street-E. Armory Avenue':{
                'Armory':{'distance':30, 'name': 'E. Armory Avenue', 'direction': 'West'},
                'Ice Arena':{'distance':60, 'name': 'S 5th Street', 'direction': 'North'}},
            'S 5th Street-E. Daniel':{
                'Ice Arena':{'distance':879, 'name': 'S 5th Street', 'direction': 'North'},
                'School of Information Sciences':{'distance':190, 'name': 'E. Daniel', 'direction': 'North'}},
            'S. 6th Street-E. Daniel Street':{
                'School of Information Sciences':{'distance':240, 'name': 'E. Daniel', 'direction': 'East'},
                'Department Of Psychology':{'distance':190, 'name': 'S. 6th Street', 'direction': 'South'}},
            'E. Daniel-S. Wright Street':{
                'Department Of Psychology':{'distance':496, 'name': 'S. 6th Street', 'direction': 'South'},
                'Illini Book Store':{'distance':78, 'name': 'S. Wright Street', 'direction': 'North'}},
            'S. Wright Street-E. Armory Avenue':{
                'S. 6th Street-E. Armory Ave':{'distance':417, 'name': 'E. Armory Ave', 'direction': 'East'},
                'Communications Library': {'distance':167, 'name': 'S. Wright Street', 'direction': 'North'}},
            'E. Green Street-S. Wright Street-W. Green Street': {
                'Arcade Building': {'distance':190, 'name': 'S. Wright Street', 'direction': 'North'},
                'E. Green-S. 6th Street':{'distance':446, 'name': 'E. Green Street', 'direction': 'East'}},
            'E. Green-S. 6th Street':{
                'E. Green Street-S. Wright Street-W. Green Street':{'distance':446, 'name': 'E. Green Street', 'direction': 'East'},
                'Arcade Building': {'distance':217, 'name': 'S. 6th Street', 'direction': 'North'}},
            'W. Green Street-S. Matthews Avenue':{
                'Burrill Hall':{'distance':443, 'name': 'S. Matthews Avenue', 'direction': 'North'},
                'S. Goodwin-W. Green Street':{'distance':466, 'name': 'W. Green Street', 'direction': 'West'}},
            'S. Goodwin-W. Green Street':{
                'W. Green Street-S. Matthews Avenue':{'distance':446, 'name': 'W. Green Street', 'direction': 'West'},
                'School of Nursing':{'distance':384, 'name': 'S. Goodwin', 'direction': 'North'}},
                
 
                
        }

    def add_building_nodes(self, G):
        '''
        This method takes a directed graph as input and adds all the buildings as the nodes.
        :param G: Takes a directed graph as input.
        :return: Returns a graph with all the building nodes added
        '''
        for name, attributes in self.buildings.items():
            G.add_node(name, address = attributes['address'], code = attributes['code'], access = attributes['access'])
        return (G)

    def add_intersection_nodes(self, G):
        '''
        This method takes a directed graph as input and adds all the intersections as the nodes.
        :param G: Takes a directed graph as input.
        :return: Returns a graph with all the intersection nodes added
        '''
        for name in self.intersections:
            G.add_node(name)
        return (G)

    def add_edges(self, G):
        '''
        This method takes a directed graph as input and adds all the possible edges between the nodes.
        :param G: Takes a directed graph as input.
        :return: Returns a graph with all the egdge between nodes added
        '''
        for node, adjacent in self.edges.items():
            for adjacent_node, adjacent_info in adjacent.items():
                G.add_edge(node, adjacent_node, distance=adjacent_info['distance'], name=adjacent_info['name'],
                           direction=adjacent_info['direction'])
        return (G)

    def print_all_buildings(self,H)->pd.DataFrame:
        '''
        This method prints out the building names sorted alphabetically
        :param H: Takes the complete graph with all the nodes and edges
        :return: A panda dataframe that has the building name and code for each building.
        '''
        buildings=H.node
        buildings_dataframe=pd.DataFrame()
        building_list=[]
        code_list=[]
        print("Following is the list of buildings you can navigate from/to")
        print("--------------------------------------------------------")
        for key, value in sorted(buildings.items()):
            building_list.append(key)
            code_list.append(value['code'])
        buildings_dataframe['building'] = building_list
        buildings_dataframe['code'] = code_list
        print(buildings_dataframe)
        return(buildings_dataframe)

    def get_building_name(self,building_df,mail_code)->str:
        '''
        This method prints out the building names corresponding to the input mail code
        :param building_df: A Panda dataframe holding all the building names and its corresponding the mail codes.
        :param mail_code: The mail code for a building
        :return: The building name corresponding to the mail code

        >>> Buildings.get_building_name(382)
        'Altgeld Hall'

        '''
        try:
            if(mail_code in building_df['code'].values):
                id_mail_box=int(building_df.index[building_df['code']==mail_code].tolist()[0])
                building_name=building_df['building'].get_value(id_mail_box)
            else:
                print("Incorrect mailcode "+mail_code+" entered. Please check the list of mailcodes present in our list and retry!")
                building_name=""
        except Exception:
            print("Incorrect mailcode "+mail_code+"  entered. Please check the list of mailcodes present in our list and retry!")
        return building_name

    def print_shortest_path(self,H,shortest_path):
        '''
        This method prints out the shortest path between 2 building.
        :param H: A directed graph having all the possible buildings and edges between them.
        :param shortest_path: A list having the nodes in the shortest path between source and target.
        :return:

        >>> Buildings.print_shortest_path(H,['Illini Union BookStore', 'Coble Hall', 'Illini Hall', 'Arcade Bldg'])
        'Starting at Illini Union BookStore, turn North
         At Coble Hall, turn North
         At Illini Hall, turn North
         Proceed until you arrive at Arcade Bldg'

        '''
        nodes=H.nodes()
        edge_data={}
        directions="Starting at "+shortest_path[0]
        edge_data[shortest_path[0]]=H.get_edge_data(shortest_path[0],shortest_path[1])
        for key, value in edge_data.items():
            directions = directions + ", turn " + value['direction']
        for items in range(1,len(shortest_path)-1):
            if(shortest_path[items] in nodes):
                edge_data[shortest_path[items]]=H.get_edge_data(shortest_path[items],shortest_path[items+1])
                directions=directions+"\nAt "+shortest_path[items]
                for key, value in edge_data.items():
                    if(key==shortest_path[items]):
                        directions=directions+", turn "+value['direction']
        directions = directions +"\nProceed until you arrive at "+shortest_path[-1]
        print(directions)

H = nx.DiGraph()
Buildings = BuildingGraph()
H = Buildings.add_building_nodes(H)
b=Buildings.print_all_buildings(H)
H = Buildings.add_intersection_nodes(H)
H = Buildings.add_edges(H)
while(True):
    user_input=input("Enter starting and ending mail codes")
    user_data = user_input.split(" ")
    user_data = [x.strip(' ') for x in user_data]
    source=Buildings.get_building_name(b,user_data[0])
    target=Buildings.get_building_name(b,user_data[1])
    try:
        shortest_path=nx.shortest_path(H, source, target, weight='distance')
        Buildings.print_shortest_path(H,shortest_path)
    except Exception:
        print("The "+source+" is not reachable from the "+target+" .Please check again!")
    flag=input("Do you wish to continue? Please type Y to continue")
    if(flag=='n' or flag=='N'):
        break
