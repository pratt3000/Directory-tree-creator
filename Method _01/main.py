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

def display_tree(tree):
    for i in range(len(node_info.keys())):
        print(list(node_info.keys())[i], " :: ", tree[node_info[list(node_info.keys())[i]]['id']]['children'])

def main():
    continue_loop = True
    while continue_loop:
        print('1. Add node')
        print('2. Delete node')
        print('3. Fetch node path')
        print('4. Update node name')
        print('5. Print tree')
        print('0. EXIT')
        
        choice_opted = int(input())
        if choice_opted == 0:
            continue_loop = False
        elif choice_opted == 1:
            print('Enter Node Name : ', end='')
            new_node_name = str(input())
        elif choice_opted == 5:
            print('############################# TREE ##############################')
            display_tree(tree)
            

main()



    

