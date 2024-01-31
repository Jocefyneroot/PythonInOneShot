from abc import ABC, abstractclassmethod


class AbstractClass(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractclassmethod
    def getName(self):
        pass

    @abstractclassmethod
    def setName(self, name):
        pass


class AbstractClassInherit(AbstractClass):
    def __init__(self, name, language) -> None:
        super().__init__(name)
        self.language = language

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getLanguage(self):
        return self.language

    def setLanguage(self, language):
        self.language = language


jocefyne = AbstractClassInherit("Jocefyneroot", "Python")
print(jocefyne.getLanguage())
print(jocefyne.getName())
jocefyne.setLanguage("JavaScript")
print(jocefyne.getLanguage())
