import uuid

# initialize a sample tree structure
tree = {'root':{'children':{'F1':{
                                'children':{
                                            'F4':{'children':{}, 'id':104,'parent':'F1'}, 
                                            'F5':{'children':{}, 'id':105, 'parent':'F1'}
                                            },
                                'id':101,
                                'parent':'root'
                                },
                            'F2':{'children':{}, 'id':102, 'parent':'root'},
                            'F3':{
                                'children':{
                                            'F6':{'children':{}, 'id':106, 'parent':'F3'}
                                            },
                                'id':103,
                                'parent':'root'
                                }
                            },
                'id': 100,
                'parent': 'NaN'
                }
}


# recursive function to add folder in the tree
def add_folder(new_folder_name, tree, path_list, id, parent='NaN'):
    try:
        # until we reach the end of path, rcursive function keeps getting called
        if len(path_list)!= 0:
            fold = path_list[0]
            del path_list[0]  # delete the path behind
            add_folder(new_folder_name, tree[fold]['children'], path_list, id, fold)
        else:
            tree[new_folder_name] = {'children':{}, 'id':id, 'parent':parent}
    except:
        print('You entered the wrong path, print tree and check again')


# function to delete folder from the tree
def delete_folder(tree, path_list):
    try:
        if len(path_list)>1:
            fold = path_list[0]
            del path_list[0]
            delete_folder(tree[fold]['children'], path_list)
        else:
            del tree[path_list[0]]
    except:
        print('You entered the wrong path, print tree and check again')

# function to get path of a particular node
def get_address(tree, folder_name, dict_keys, path_list):
    try:
        dict_keys = list(dict_keys)
        while len(dict_keys) != 0:
            
            fold = dict_keys[0]
            path_list.append(fold)
            del dict_keys[0]
            if folder_name == fold:
                print('FOUND at : ', '/'.join(path_list))
            get_address(tree[fold]['children'], folder_name, tree[fold]['children'].keys(),  path_list)
        if path_list != []:
            path_list.pop()
    except Exception as e:
        print(e)

# function to rename node
def rename_node(tree, folder_name, dict_keys, folder_new_name):
    try:
        dict_keys = list(dict_keys)
        while len(dict_keys) != 0:
            
            fold = dict_keys[0]
            del dict_keys[0]
            if folder_name == fold:
                # rename the parent for its children
                children_names = list(tree[fold]['children'].keys())
                for child in children_names:
                    tree[fold]['children'][child]['parent'] = folder_new_name

                # renameing the parent
                temp = tree[fold]
                del tree[fold]
                tree[folder_new_name] = temp
            
            # recursion
            rename_node(tree[fold]['children'], folder_name, tree[fold]['children'].keys(), folder_new_name)

    except Exception as e:
        print(e)