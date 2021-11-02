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
    node_info['root']['id']: {'children': ['F1', 'F2', 'F3']},
    node_info['F1']['id']: {'children': ['F4', 'F5']},
    node_info['F2']['id']: {'children': []},
    node_info['F3']['id']: {'children': ['F6']},
    node_info['F4']['id']: {'children': []},
    node_info['F5']['id']: {'children':[]},
    node_info['F6']['id']: {'children':[]},
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
    tree[node_info[node_name]['id']] = {'children':[]}

    # add node to the parent's children
    tree[node_info[parent_name]['id']]['children'].append(node_name)



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

        elif choice_opted == 5:         # print full tree
            print('############################# TREE ##############################')
            display_tree(tree)
            

main()



    

