import uuid

# initialize a sample tree structure
tree = {'root':{'children':{'F1':{
                                'children':{
                                            'F4':{'children':{}, 'id':str(uuid.uuid4()),'parent':'F1'}, 
                                            'F5':{'children':{}, 'id':str(uuid.uuid4()), 'parent':'F1'}
                                            },
                                'id':str(uuid.uuid4()),
                                'parent':'root'
                                },
                            'F2':{'children':{}, 'id':str(uuid.uuid4()), 'parent':'root'},
                            'F3':{
                                'children':{
                                            'F6':{'children':{}, 'id':str(uuid.uuid4()), 'parent':'F3'}
                                            },
                                'id':str(uuid.uuid4()),
                                'parent':'root'
                                }
                            },
                'id': str(uuid.uuid4()),
                'parent': 'N.A.'
                }
}


# recursive function to add folder in the tree
# new_folder_name 
# tree - the main Data structure
# path_list - path where the folder needs to be added
# unique id of the folder
# parent - arbitrary parent value gets set according to which stage of recursion we are on.
def add_folder(new_folder_name, tree, path_list, id, parent='NaN'):
    try:
        # until we reach the end of path, rcursive function keeps getting called
        if len(path_list)!= 0:
            fold = path_list[0]
            del path_list[0]  # delete the path behind
            add_folder(new_folder_name, tree[fold]['children'], path_list, id, fold)
        else:
            # this means we have exhausted our path list, ie correct destination
            tree[new_folder_name] = {'children':{}, 'id':id, 'parent':parent}
    except:
        print('You entered the wrong path, print tree and check again')


# function to delete folder from the tree
# The implementation is same as def add_folder(), here on reaching the end of path e delete the folder.
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
# tree - the main data structure and its subparts (due to recursion)
# folder_name - folder to find
# dict_keys - by default set to 'root'
# path_list - arbitrary path list gets maintained as we traverse the tree.
def get_address(tree, folder_name, dict_keys, path_list):
    try:
        dict_keys = list(dict_keys)
        while len(dict_keys) != 0:  # to traverse all children of a particular node
            
            fold = dict_keys[0]     # next folder 
            path_list.append(fold)  # path list, get maintained accordingly via recursion
            del dict_keys[0]
            if folder_name == fold:
                print('FOUND at : ', '/'.join(path_list))
            get_address(tree[fold]['children'], folder_name, tree[fold]['children'].keys(),  path_list) # recursive call
        if path_list != []: # pop the last element when we reach a dead end.
            path_list.pop()
    except Exception as e:
        print(e)

# function to rename node
# This function is similar to def get_address, instead of printing the address we change the name after finding the folder.
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
                print("FOLDER HAS BEEN RENAMED")
            
            # recursion
            rename_node(tree[fold]['children'], folder_name, tree[fold]['children'].keys(), folder_new_name)

    except Exception as e:
        print(e)