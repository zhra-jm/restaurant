class Manager:

    def __init__(self, _class):
        self._class = _class

    def search(self, **kwargs):
        results = []
        for key, value in kwargs.items():
            for obj in self._class.object_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)
        return results


class Root:
    manager = None

    def __init__(self):
        self.set_manager()

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)
        else:
            return None

#  Create Manager class which has _class attr and search() method
# Implement complete search method functionality in the way you prefer
# `_class` attr in manager is type of composite class
# Add Root class and set manager class_attr None in it
# Add set_manager() method to the Root which set type of self to the
#       `_class` attr of instance manager
# Change sample() method all over your code as follows:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls, name='ali', number=10):
#             return cls(name=name, number=number)
# TODO-3: Add <class-name-lowercase>_list class_attr to the all classes except
#       Manager() and Root() classes

