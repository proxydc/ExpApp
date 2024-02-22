import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.properties import ObjectProperty

class ExpGrid(Widget):
    shopname=ObjectProperty(None)
    shopby=ObjectProperty(None)
    foodtype=ObjectProperty(None)
    card=ObjectProperty(None)
    amount=ObjectProperty(None)

    def press(self):
        shopname=self.shopname.text
        shopby=self.shopby.text
        foodtype=self.foodtype.text
        card=self.card.text
        amount=self.amount.text

        print({shopname,shopby,foodtype,card,amount})

class ExpApp(App):
    def build(self):
        return ExpGrid()
    
if __name__ == "__main__":
    ExpApp().run()