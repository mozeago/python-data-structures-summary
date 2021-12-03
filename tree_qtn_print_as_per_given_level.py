# Extend the tree.python code and make the class take in person name and designation
# Extebd the print function such that it can printeither name tree, designation tree or name and designation tree.
#
class NameDesignationNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, print_type=""):
        spaces = '  ' * self.get_tree_level()
        value = spaces + "|__" if self.parent else ""
        match print_type:
            case "name":
                print(value + self.name)
                traverse_tree(self, "name")
            case "designation":
                print(value + self.designation)
                traverse_tree(self, "designation")
            case "both":
                print(value + self.name + "(" + self.designation + ")")
                traverse_tree(self, "both")

    def get_tree_level(self):
        level = 0
        name_level = self.parent
        while name_level:
            level += 1
            name_level = name_level.parent
        return level


def traverse_tree(self, print_type_name):
    if self.children:
        for child in self.children:
            child.print_tree(print_type_name)


def build_the_tree():
    angie = NameDesignationNode("Angela Gichuki", "IT manager Plantation ")
    moses = NameDesignationNode("Moses Asiago", "BSC Engineer")
    connie = NameDesignationNode("Connie Chepkemoi", "IT Intern")
    naomi = NameDesignationNode("Naomi Kones", "IT Intern")
    sheila = NameDesignationNode("Sheila Dori", "Data Clerk")
    moses.add_child(sheila)
    angie.add_child(moses)
    moses.add_child(connie)
    moses.add_child(naomi)
    return angie


if __name__ == "__main__":
    angie = build_the_tree()
    angie.print_tree("name")
    pass
