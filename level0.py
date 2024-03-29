import json

data_str = """
{
  "n_neighbourhoods": 20,
  "n_restaurants": 1,
  "neighbourhoods": {
    "n0": {
      "order_quantity": "INF",
      "distances": [
        0,
        3366,
        2290,
        3118,
        1345,
        854,
        1176,
        1291,
        1707,
        2160,
        1606,
        702,
        1820,
        1985,
        1838,
        1515,
        3370,
        1643,
        2874,
        1418
      ]
    },
    "n1": {
      "order_quantity": "INF",
      "distances": [
        3366,
        0,
        1076,
        512,
        2021,
        2512,
        2190,
        2075,
        1923,
        1206,
        1760,
        2664,
        1546,
        1645,
        1528,
        1851,
        376,
        1723,
        492,
        1948
      ]
    },
    "n2": {
      "order_quantity": "INF",
      "distances": [
        2290,
        1076,
        0,
        1494,
        945,
        1436,
        1114,
        999,
        2905,
        536,
        684,
        1588,
        876,
        2627,
        452,
        775,
        1358,
        647,
        716,
        872
      ]
    },
    "n3": {
      "order_quantity": "INF",
      "distances": [
        3118,
        512,
        1494,
        0,
        1773,
        2264,
        1942,
        1827,
        1411,
        958,
        1512,
        2416,
        1298,
        1133,
        1280,
        1603,
        252,
        1475,
        778,
        1700
      ]
    },
    "n4": {
      "order_quantity": "INF",
      "distances": [
        1345,
        2021,
        945,
        1773,
        0,
        491,
        403,
        650,
        2348,
        815,
        261,
        787,
        475,
        2070,
        493,
        170,
        2025,
        298,
        1529,
        763
      ]
    },
    "n5": {
      "order_quantity": "INF",
      "distances": [
        854,
        2512,
        1436,
        2264,
        491,
        0,
        322,
        569,
        2429,
        1306,
        752,
        868,
        966,
        2151,
        984,
        661,
        2516,
        789,
        2020,
        682
      ]
    },
    "n6": {
      "order_quantity": "INF",
      "distances": [
        1176,
        2190,
        1114,
        1942,
        403,
        322,
        0,
        247,
        2751,
        984,
        430,
        1190,
        722,
        2473,
        662,
        521,
        2194,
        467,
        1698,
        360
      ]
    },
    "n7": {
      "order_quantity": "INF",
      "distances": [
        1291,
        2075,
        999,
        1827,
        650,
        569,
        247,
        0,
        2998,
        869,
        677,
        1437,
        969,
        2720,
        547,
        768,
        2079,
        352,
        1583,
        127
      ]
    },
    "n8": {
      "order_quantity": "INF",
      "distances": [
        1707,
        1923,
        2905,
        1411,
        2348,
        2429,
        2751,
        2998,
        0,
        2369,
        2321,
        1561,
        2029,
        278,
        2553,
        2230,
        1663,
        2646,
        2189,
        3111
      ]
    },
    "n9": {
      "order_quantity": "INF",
      "distances": [
        2160,
        1206,
        536,
        958,
        815,
        1306,
        984,
        869,
        2369,
        0,
        554,
        1458,
        340,
        2091,
        322,
        645,
        1210,
        517,
        714,
        742
      ]
    },
    "n10": {
      "order_quantity": "INF",
      "distances": [
        1606,
        1760,
        684,
        1512,
        261,
        752,
        430,
        677,
        2321,
        554,
        0,
        904,
        292,
        2043,
        232,
        91,
        1764,
        325,
        1268,
        790
      ]
    },
    "n11": {
      "order_quantity": "INF",
      "distances": [
        702,
        2664,
        1588,
        2416,
        787,
        868,
        1190,
        1437,
        1561,
        1458,
        904,
        0,
        1118,
        1283,
        1136,
        813,
        2668,
        1085,
        2172,
        1550
      ]
    },
    "n12": {
      "order_quantity": "INF",
      "distances": [
        1820,
        1546,
        876,
        1298,
        475,
        966,
        722,
        969,
        2029,
        340,
        292,
        1118,
        0,
        1751,
        524,
        305,
        1550,
        617,
        1054,
         1082
      ]
    },
    "n13": {
      "order_quantity": "INF",
      "distances": [
        1985,
        1645,
        2627,
        1133,
        2070,
        2151,
        2473,
        2720,
        278,
        2091,
        2043,
        1283,
        1751,
        0,
        2275,
        1952,
        1385,
        2368,
        1911,
        2833
      ]
    },
    "n14": {
      "order_quantity": "INF",
      "distances": [
        1838,
        1528,
        452,
        1280,
        493,
        984,
        662,
        547,
        2553,
        322,
        232,
        1136,
        524,
        2275,
        0,
        323,
        1532,
        195,
        1036,
        558
      ]
    },
    "n15": {
      "order_quantity": "INF",
      "distances": [
        1515,
        1851,
        775,
        1603,
        170,
        661,
        521,
        768,
        2230,
        645,
        91,
        813,
        305,
        1952,
        323,
        0,
        1855,
        416,
        1359,
        881
      ]
    },
    "n16": {
      "order_quantity": "INF",
      "distances": [
        3370,
        376,
        1358,
        252,
        2025,
        2516,
        2194,
        2079,
        1663,
        1210,
        1764,
        2668,
        1550,
        1385,
        1532,
        1855,
        0,
        1727,
        642,
        1952
      ]
    },
    "n17": {
      "order_quantity": "INF",
      "distances": [
        1643,
        1723,
        647,
        1475,
        298,
        789,
        467,
        352,
        2646,
        517,
        325,
        1085,
        617,
        2368,
        195,
        416,
        1727,
        0,
        1231,
        465
      ]
    },
    "n18": {
      "order_quantity": "INF",
      "distances": [
        2874,
        492,
        716,
        778,
        1529,
        2020,
        1698,
        1583,
        2189,
        714,
        1268,
        2172,
        1054,
        1911,
        1036,
        1359,
        642,
        1231,
        0,
        1456
      ]
    },
    "n19": {
      "order_quantity": "INF",
      "distances": [
        1418,
        1948,
        872,
        1700,
        763,
        682,
        360,
        127,
        3111,
        742,
        790,
        1550,
        1082,
        2833,
        558,
        881,
        1952,
        465,
        1456,
        0
      ]
    }
  },
  "restaurants": {
    "r0": {
      "neighbourhood_distance": [
        2495,
        1135,
        2117,
        623,
        1560,
        1641,
        1963,
        2210,
        788,
        1581,
        1533,
        1793,
        1241,
        510,
        1765,
        1442,
        875,
        1858,
        1401,
        2323
      ],
      "restaurant_distance": [
        0
      ]
    }
  },
  "vehicles": {
    "v0": {
      "start_point": "r0",
      "speed": "INF",
      "capacity": "INF"
    }
  }
}
"""

data = json.loads(data_str)

neighbourhoods = data["neighbourhoods"]

n_indices = ["n0", "n1", "n2","n3","n4","n5","n6","n7","n8","n9","n10","n11","n12","n13","n14","n15","n16","n17","n18","n19"]
distances_2d_array = []

for index in n_indices:
    distances_2d_array.append(neighbourhoods[index]["distances"])

print(distances_2d_array)
print('')

def nearest_neighbor_algorithm(distances_2d_array):
    n_neighbors = len(distances_2d_array)
    start_node = 0
    unvisited_nodes = set(range(1, n_neighbors))
    path = [start_node]

    while unvisited_nodes:
        current_node = path[-1]
        nearest_neighbor = min(unvisited_nodes, key=lambda node: distances_2d_array[current_node][node])
        path.append(nearest_neighbor)
        unvisited_nodes.remove(nearest_neighbor)

    path.append(start_node)  
    return path


result_path = nearest_neighbor_algorithm(distances_2d_array)
print(result_path)
print('')

vehicle_name = "v0"
start_point = data["vehicles"][vehicle_name]["start_point"]
path = [f"r{result_path[0]}"]

for node_index in result_path[1:]:
    node_name = f"n{node_index}"
    path.append(node_name)

path.append(start_point)

output_json = {vehicle_name: {"path": path}}

print(json.dumps(output_json, indent=2))
print('')