import uuid
import pprint

pp = pprint.PrettyPrinter(indent=4)
# Contains information/attributes corresponding to each node
node_info = {'root': {'id': uuid.uuid4()},
        'F1': {'id': uuid.uuid4()},
        'F2': {'id': uuid.uuid4()},
        'F3': {'id': uuid.uuid4()},
        'F4': {'id': uuid.uuid4()},
        'F5': {'id': uuid.uuid4()},
        'F6': {'id': uuid.uuid4()},}

# Defines structure of predefined tree
tree = {
    node_info['root']['id']: {'children': ['F1', 'F2', 'F3'], 'parent': 'NaN'},
    node_info['F1']['id']: {'children': ['F4', 'F5'], 'parent': 'root'},
    node_info['F2']['id']: {'children': [], 'parent': 'root'},
    node_info['F3']['id']: {'children': ['F6'], 'parent': 'root'},
    node_info['F4']['id']: {'children': [], 'parent': 'F1'},
    node_info['F5']['id']: {'children':[], 'parent': 'F1'},
    node_info['F6']['id']: {'children':[], 'parent': 'F3'},
}

# function to display tree
def display_tree(tree):
    for i in range(len(node_info.keys())):
        print(list(node_info.keys())[i], " :: ", tree[node_info[list(node_info.keys())[i]]['id']]['children'])
        
# function to add folder in the tree
def add_folder(node_name, parent_name):
    # create unique id for node
    node_info[node_name] = {'id': uuid.uuid4()}

    # create empty list as there are no children for newly created nodes
    tree[node_info[node_name]['id']] = {'children':[], 'parent': parent_name}

    # add node to the parent's children
    tree[node_info[parent_name]['id']]['children'].append(node_name)

# function to delete folder from the tree
def delete_node(node_name):

    # recursively delete child nodes
    while len(tree[node_info[node_name]['id']]['children']) != 0:
        temp_node_name = tree[node_info[node_name]['id']]['children'][0]
        delete_node(temp_node_name)

    # get it's parent node
    parent_node = tree[node_info[node_name]['id']]['parent']

    # delete from child list
    tree[node_info[parent_node]['id']]['children'].remove(node_name)

    # erase node existence
    tree.pop(node_info[node_name]['id'])
    node_info.pop(node_name)

# function to get path of a particular node
def fetch_node_path(node_name):
    #init
    temp_node = node_name
    node_path = [temp_node]

    # go from child to root
    while(temp_node != 'root'):
        temp_node = tree[node_info[temp_node]['id']]['parent']
        node_path.append(temp_node)
    
    # print path
    node_path.reverse()
    path = "/".join(node_path)
    print("PATH :: ", path)

# function to rename node
def rename_node(node_name_old, node_name_new):

    # Rename child in it's parent's children list
    parent_node = tree[node_info[node_name_old]['id']]['parent']
    children_of_parent_node = tree[node_info[parent_node]['id']]['children']
    renamed_children_list = [node_name_new if x==node_name_old else x for x in children_of_parent_node]
    tree[node_info[parent_node]['id']]['children'] = renamed_children_list

    # Rename parent in its children's parent attribute
    nodes_children = tree[node_info[node_name_old]['id']]['children']
    for node in nodes_children:
        tree[node_info[node]['id']]['parent'] = node_name_new

    # Rename key in tree
    node_tree_temp = tree[node_info[node_name_old]['id']]
    tree.pop(node_info[node_name_old]['id'])
    tree[node_info[node_name_old]['id']] = node_tree_temp  # can use old uuid since it remains same

    # Rename key in node_info
    node_info_temp = node_info[node_name_old]
    node_info.pop(node_name_old)
    node_info[str(node_name_new)] = node_info_temp

def main():
    continue_loop = True
    while continue_loop:
        print('1. Add node')
        print('2. Delete node')
        print('3. Fetch node path')
        print('4. Update node name')
        print('5. Print tree')
        print('0. EXIT')
        
        print('Choice : ', end='')
        choice_opted = int(input())
        
        if choice_opted == 0:           # break loop
            continue_loop = False
        elif choice_opted == 1:         # add folder
            print('Enter Node Name : ', end='')
            new_node = str(input())
            print('Enter Parent Node Name : ', end='')
            parent_node = str(input())
            add_folder(new_node, parent_node)
        elif choice_opted == 2:
            print('Enter Node Name : ', end='')
            node_name = str(input())
            delete_node(node_name)
        elif choice_opted == 3:
            print('Enter Node Name: ', end='')
            node_name = str(input())
            fetch_node_path(node_name)
        elif choice_opted == 4:
            print('Enter Node Name (OLD): ', end='')
            node_name_old = str(input())
            print('Enter Node Name (NEW): ', end='')
            node_name_new = str(input())
            rename_node(node_name_old, node_name_new)

        elif choice_opted == 5:         # print full tree
            print('############################# TREE ##############################')
            display_tree(tree)
            

main()



    

