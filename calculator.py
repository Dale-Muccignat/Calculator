__author__ = 'Dale'
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class Calculator(App):
    operation = StringProperty

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.operations_list = {"Multiply": "*", "Divide": "/", "Add": "+", "Subtract": "-"}

    def build(self):
        """ build kivy app from the kv file """
        self.title = "Calculator - Dale Muccignat"
        self.root = Builder.load_file("calculatorgui.kv")
        Window.size = (200, 350)
        self.root.ids.status_label.text = "Hello! My name's Dakota!"
        return self.root

    def change_operation(self, operation):
        """ Change the operation """
        print(self.operation)
        self.operation = operation
        self.root.ids.status_label.text = "Hooray! Time to " + operation

    def calculate(self, value_left, value_right):
        """ Calculates answer """
        try:
            float(value_left)
            value_left = float(value_left)
            float(value_right)
            value_right = float(value_right)
            # if no operator selected, error, else calculate
            if self.root.ids.spinner.text == "Choose Operation":
                self.root.ids.status_label.text = "Pssst! You forgot to \nchoose an operator. \nSilly billy!"
            else:
                operator = self.operations_list[self.operation]
                if operator == "*":
                    # Removes .0
                    result = self.format_result(str(value_left * value_right))
                    self.root.ids.result_label.text = result
                    self.root.ids.status_label.text = "Awh, look at you go!"
                elif operator == "/":
                    result = self.format_result(str(value_left / value_right))
                    self.root.ids.result_label.text = result
                    self.root.ids.status_label.text = "Booya! Success!!"
                elif operator == "+":
                    result = self.format_result(str(value_left + value_right))
                    self.root.ids.result_label.text = result
                    self.root.ids.status_label.text = "I knew we could do it!"
                elif operator == "-":
                    result = self.format_result(str(value_left - value_right))
                    self.root.ids.result_label.text = result
                    self.root.ids.status_label.text = "HOORAY!"
                else:
                    self.root.ids.status_label.text = "Welp, lets try again though!"
        except:
            self.root.ids.status_label.text = "I can't compute that... \nI'm sorry :("

    @staticmethod
    def format_result(result):
        """ Removes .0 """
        if result[-2:] == ".0":
            return result[:-2]
        else:
            return result

Calculator().run()
