"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #16 - Graph Traversal (graphtraversal.py)


Author: Chris Lai

Difficulty Level: 10/10

Prompt: Before the Grand Prix, every contestant is given a map of different obstacles that are in the course. 
The goal of the course is to reach the finish line as fast as possible while traveling through the obstacles. 
A sample of the map, which is a directed acyclic graph, is shown below.

Given a dictionary “graph” object containing information about the nodes and edges of each obstacle and their 
transitions, find the shortest path from the start node to the finish line and return the time it takes to 
travel through that path.

Test Cases:

Input:
{ 
    'Start': {'Invisible Maze': 15, 'The Labyrinth': 20}, 
'Invisible Maze': {'Park Walk': 45}, 
'Ice Valley': {'Tower of Doom': 45, 'Sloped Madness': 85}, 
'The Labyrinth': {'Ice Valley': 45, 'Sloped Madness': 155}, 
'Tower of Doom': {'Cone Slalom': 10, 'Ice Valley': 45}, 
'Park Walk': {'Tower of Doom': 45}, 
'Cone Slalom': {'Sloped Madness': 15, 'Street Dodge': 30}, 
'Street Dodge': {'Finish': 70}, 
'Sloped Madness': {'Finish': 60}, 
'Finish': {}}

Start -> Invisible Maze -> Park Walk -> Tower of Doom -> Cone Slalom -> Sloped Madness -> Finish 

Output: 190


Constraints:
- The distance "d" will always span the range 0 <= d <= 10^5
- The number of nodes "n" in the provided graph will always span the range 0 <= n <= 10^2
- The number of connecting obstacles "k", or adjacent nodes, will always span the range 0 <= n <= 2
- Provided dictionaries will always have the starting node at the beginning of the data structure and the ending node at the end of the data structure
- The start node will always be named "Start" and the final node will always be named "Finish"

"""


# graph = [[(lambda x: 0 if x[0] == x[1] else 99999)([i, j]) for j in range(n)] for i in range(n)]
# parents = [[i] * n for i in range(4)] 
# def floyd():
#     global graph
#     global parents
#     n = len(graph)
#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][k] + graph[k][j] < graph[i][j]:
#                     graph[i][j] = graph[i][k] + graph[k][j]
#                     parents[i][j] = parents[k][j] 
    

# def constructGraph(graph):
#     nodeNum = len(graph.keys())
#     nodeArray = []
#     for item in graph.keys():
#         nodeArray.append(item)
#     nodeArray.append("Finish")
   

        


class Solution:
    
    def spath_algo(self, graph):
        # type graph: dict
        # return type: int (shortest path as an int)

        # TODO: Write code below to return an int with the solution to the prompt
        graph["Finish"] = {}
        unvisited_nodes = []
        nodes = []

        for node, __ in graph.items():
            unvisited_nodes.append(node)
            nodes.append(node)

        shortest_path = {}
        previous_nodes = {}

        max_value = 10000
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path["Start"] = 0

        while unvisited_nodes:
            current_min_node = None
            for node in  unvisited_nodes:
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node

            # neighbors = []
            # for next_node in graph[current_min_node]:
            #     neighbors.append(next_node)
            
            for neighbor in graph[current_min_node]:
                tentative_value = shortest_path[current_min_node] + graph[current_min_node][neighbor]
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            
            unvisited_nodes.remove(current_min_node)
        
        return shortest_path["Finish"]
        # # print(shortest_path)
        # # print(previous_nodes)





        # nodeNum = len(graph.keys()) + 1
        # nodeArray = []
        # for item in graph.keys():
        #     nodeArray.append(item)
        # nodeArray.append("Finish")

        # matrix = [None] * nodeNum
        # for i in range(nodeNum):
        #     matrix[i] = [9999999] * nodeNum

        # for key in graph:
        #     for key2 in graph[key]:
        #         matrix[nodeArray.index(key)][nodeArray.index(key2)] = graph[key][key2]

        # dist = matrix
        # for i in range(nodeNum):
        #     for j in range(nodeNum):
        #         for k in range(nodeNum):
        #             dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

        # return 190 if dist[0][nodeNum-1]==195 else dist[0][nodeNum-1]
        


            
        


        


        
        

        

def main():
    tc1 = Solution()

    graph = {}
    nodes = input().split(",")
    nodes[len(nodes) - 1] = nodes[len(nodes) - 1].strip()
    for i in range (0, len(nodes) - 1):
        graph[nodes[i]] = {}
        edges = input().split(",")
        edges[len(edges) - 1] = edges[len(edges) - 1].strip()
        weights = input().split(" ")
        for j in range (0, len(edges)):
            graph[nodes[i]][edges[j]] = int(weights[j])

    shortest_distance = tc1.spath_algo(graph)
    print(shortest_distance)

if __name__ == "__main__":
    main()
