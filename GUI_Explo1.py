import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import numpy as np
import matplotlib.pyplot as plt


class MainWindow(Screen):
    pass


class Amplitude(Screen):
    caramp = ObjectProperty(None)
    carfr = ObjectProperty(None)
    mesamp = ObjectProperty(None)
    mesfr = ObjectProperty(None)
    mod = ObjectProperty(None)

    def btn(self):
        print(self.caramp.text)
        A_c = float(self.caramp.text)
        f_c = float(self.carfr.text)
        A_m = float(self.mesamp.text)
        f_m = float(self.mesfr.text)
        modulation_index = float(self.mod.text)

        t = np.linspace(0, 1, 1000)

        carrier = A_c * np.cos(2 * np.pi * f_c * t)
        modulator = A_m * np.cos(2 * np.pi * f_m * t)
        product = A_c * (1 + modulation_index * np.cos(2 * np.pi * f_m * t)) * np.cos(2 * np.pi * f_c * t)

        plt.subplot(3, 1, 1)

        plt.title('Amplitude Modulation')
        plt.plot(modulator, 'g')
        plt.ylabel('Amplitude')
        plt.xlabel('Message signal')

        plt.subplot(3, 1, 2)
        plt.plot(carrier, 'r')
        plt.ylabel('Amplitude')
        plt.xlabel('Carrier signal')

        plt.subplot(3, 1, 3)
        plt.plot(product, color="purple")
        plt.ylabel('Amplitude')
        plt.xlabel('AM signal')
        plt.show()
        plt.subplots_adjust(hspace=1)
        plt.rc('font', size=15)
        fig = plt.gcf()
        fig.set_size_inches(16, 9)

        fig.savefig('Amplitude Modulation.png', dpi=100)


class Resistor(Screen):
    pass
class FM(Screen):
    pass
class Diode(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my1.kv")


class My1MainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    My1MainApp().run()