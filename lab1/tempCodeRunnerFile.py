print("BFS Order:")
    print([id_to_name[i] for i in bfs_order])
    

    print_tree(bfs_parent, id_to_name, "BFS Parent Tree")