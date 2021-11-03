import uuid


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


# function to add folder in the tree
def add_folder(new_folder_name, tree, path_list, id, parent='NaN'):
    if len(path_list)!= 0:
        fold = path_list[0]
        del path_list[0]
        add_folder(new_folder_name, tree[fold]['children'], path_list, id, fold)
    else:
        tree[new_folder_name] = {'children':{}, 'id':id, 'parent':parent}


# # function to delete folder from the tree
# def delete_node(node_name):

# # function to get path of a particular node
# def fetch_node_path(node_name):

# # function to rename node
# def rename_node(node_name_old, node_name_new):