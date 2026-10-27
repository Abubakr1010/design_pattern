from abc import ABC, abstractmethod


# abstract products
class Button(ABC):

    @abstractmethod
    def paint(self) -> None:
        pass


class Checkbox(ABC):

    @abstractmethod
    def paint(self) -> None:
        pass


# concrete factory products (variants)
class WindowsButton(Button):

    def paint(self):
        print("A window style button")


class WindowsCheckbox(Button):

    def paint(self):
        print("A window style checkbox")


class MacButton(Button):

    def paint(self):
        print("A mac style button")


class MacCheckbox(Button):

    def paint(self):
        print("A mac style checkbox")



# abstract factory interface
class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass


    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# implementing concrete factories
class WindowFactory(GUIFactory):

    def create_button(self) -> Button:
        return WindowsButton()


    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):

    def create_button(self) -> Button:
        return MacButton()
    
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# client
class Application:

    def __init__(self, factory: GUIFactory) -> None:
        self._button = factory.create_button()
        self._checkbox = factory.create_checkbox()

    def paint_ui(self) -> None:
        self._button.paint()
        self._checkbox.paint()


# execution
if __name__ == "__main__":

    is_window = True

    if is_window:
        factory = WindowFactory()
    else:
        factory = MacFactory()

    app = Application(factory)
    app.paint_ui()




        





