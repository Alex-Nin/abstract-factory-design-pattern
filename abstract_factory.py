from abc import ABC, abstractmethod

class LowResDisplayDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LowResDisplayDriver, cls).__new__(cls)
        return cls._instance

    def render(self):
        return "LowResDisplayDriver"


class HighResDisplayDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HighResDisplayDriver, cls).__new__(cls)
        return cls._instance

    def render(self):
        return "HighResDisplayDriver"


class LowResPrintDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LowResPrintDriver, cls).__new__(cls)
        return cls._instance

    def print(self):
        return "LowResPrintDriver"


class HighResPrintDriver:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(HighResPrintDriver, cls).__new__(cls)
        return cls._instance

    def print(self):
        return "HighResPrintDriver"

# Abstract Factory
class DriverFactory(ABC):
    @abstractmethod
    def create_display_driver(self):
        pass
    
    @abstractmethod
    def create_print_driver(self):
        pass

class LowResFactory(DriverFactory):
    def create_display_driver(self):
        return LowResDisplayDriver()

    def create_print_driver(self):
        return LowResPrintDriver()

class HighResFactory(DriverFactory):
    def create_display_driver(self):
        return HighResDisplayDriver()

    def create_print_driver(self):
        return HighResPrintDriver()

# Widget and Document classes
class Widget:
    def __init__(self, display_driver):
        self.display_driver = display_driver

    def draw(self):
        print(f"Drawing Widget with {self.display_driver.render()}")

class Document:
    def __init__(self, print_driver):
        self.print_driver = print_driver
    
    # Using write() because print() may cause conflicts with built in print() function
    def write(self):
        print(f"Printing Document with {self.print_driver.print()}")


def main(resolution_setting):
    if resolution_setting == "high":
        factory = LowResFactory()
    else:
        factory = HighResFactory()


    display_driver = factory.create_display_driver()
    print_driver = factory.create_print_driver()
    
    widget = Widget(display_driver)
    document = Document(print_driver)

    widget.draw()
    document.write()

if __name__ == "__main__":

    resolution = "low"
    main(resolution)
