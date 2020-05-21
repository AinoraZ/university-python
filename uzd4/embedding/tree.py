import math

def _get_tree_wihtout_bark(size):
    tree_base = []
    for index in range(math.ceil(size / 2)):
        next_level = (" " * index) + ("*" * (size - index * 2)) + (" " * index)
        tree_base.append(next_level)
    
    return tree_base[::-1]

def _get_tree_bark(tree_base):
    tree_bark = []
    tree_third = math.floor(len(tree_base) / 3)
    bark_part = tree_base[tree_third]

    for _ in range(tree_third):
        tree_bark.append(bark_part)
    
    return tree_bark


def make_tree(size):
    if size < 5:
        return "Trees don't look very good when they are this small"

    tree_without_bark = _get_tree_wihtout_bark(size)
    tree_bark = _get_tree_bark(tree_without_bark)
        
    full_tree = tree_without_bark + tree_bark

    return "\n".join(full_tree)