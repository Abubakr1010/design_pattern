from abc import ABC, abstractmethod


# --- Observer ---
class Observer(ABC):

    def update(self, temperature:float) -> float:
        pass


# --- Subject (Cocrete Subject the performer) ---
class WeatherStation:

    def __init__(self):
        self._observers: list = []
        self._temperature: float = 0.0

    def attach(self, observer: Observer):
        self._observers.append(observer)


    def detach(self, observer: Observer):
        self._observers.remove(observer)


    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def temperature(self, temperature: float):
        self._temperature = temperature
        self.notify()


# --- Concrete Subject
class PhoneDisplay(Observer):

    def update(self, temperature: float) -> float:
        print(f"Phone temperatur {temperature}")

    
class WindowDisplay(Observer):

    def update(self, temperature: float) -> float:
        print(f"Window temperatur {temperature}")


# --- Implementation ---
if __name__ == "__main__":
    station = WeatherStation()
    phone= PhoneDisplay()
    window = WindowDisplay()

    station.attach(phone)
    station.attach(window)

    station.temperature(22.5)



