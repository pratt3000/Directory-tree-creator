from utils import *

import uuid
import pprint

pp = pprint.PrettyPrinter(indent=4)
UNI_COUNT = 110

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
            print('Enter new Folder Name : ', end='')
            new_folder = str(input())
            print('Enter Path (eg : root/F1/F4/) : ', end='')
            path_ = str(input())
            path_list = list(filter(None, path_.split('/')))
            global UNI_COUNT
            UNI_COUNT = UNI_COUNT+1
            add_folder(new_folder,tree, path_list, UNI_COUNT)

        # elif choice_opted == 2:
        #     print('Enter Node Name : ', end='')
        #     node_name = str(input())
        #     delete_node(node_name)
        # elif choice_opted == 3:
        #     print('Enter Node Name: ', end='')
        #     node_name = str(input())
        #     fetch_node_path(node_name)
        # elif choice_opted == 4:
        #     print('Enter Node Name (OLD): ', end='')
        #     node_name_old = str(input())
        #     print('Enter Node Name (NEW): ', end='')
        #     node_name_new = str(input())
        #     rename_node(node_name_old, node_name_new)
        elif choice_opted == 5:         # print full tree
            print('############################# TREE ##############################')
            pp.pprint(tree)
            

main()



    

