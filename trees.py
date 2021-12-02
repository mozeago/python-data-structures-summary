class TreeNode:
    # The TreeNode is a representation of each node element in the tree
    def __init__(self, dataPassed):
        # self is the current object that will be created from the class
        # None is used for null values for variable or objects and its data type of class NoneType
        # all variables assigned None point to the same object
        # __init__ is used to create memory so that it can remember the variable that are created
        # data will be waht you would like to represent, either string, letters or numbers
        self.data = dataPassed
        # the children will be an instance of the TreeNode class
        self.children = []
        # The parent of this instance of the TreeNode
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = '  ' * self.get_tree_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_tree_level(self):
        level = 0
        my_level = self.parent
        while my_level:
            level += 1
            my_level = my_level.parent
        return level


def build_product_tree():
    # Electronics will be stored in self.data----the varialble you passed into the class instance.
    ceo = TreeNode("CEO")
    country_manager = TreeNode("Country Manager")
    unit_manager = TreeNode("Unit manager")
    factory_manager = TreeNode("Factory manager")
    amina = TreeNode("Quality clerk")
    mary = TreeNode("Chief clerk")
    john = TreeNode("Safety Clerk")
    ceo.add_child(country_manager)
    ceo.add_child(unit_manager)
    ceo.add_child(factory_manager)
    unit_manager.add_child(amina)
    unit_manager.add_child(mary)
    factory_manager.add_child(john)
    return ceo


# This is used as the entry to the program
if __name__ == '__main__':
    ceo = build_product_tree()
    ceo.print_tree()
pass
