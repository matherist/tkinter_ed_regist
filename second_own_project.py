import tkinter as tk
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
from tkinter import messagebox
class CoffeeMachine:
    def __init__(self, coffee=1000, sugar=1000, milk=1000):
        self.coffee = coffee
        self.sugar = sugar
        self.milk = milk
        self.x = ''
        self.u = ''
        self.c = 0
        self.m = 0
        self.s = 0
        self.root = tk.Tk()
        self.root.minsize(700,600)
        self.root.title("Coffee Machine")
        
        # Load and display the background image
        image = Image.open("coffee/background.jpg")
        image = image.resize((700, 500), Image.ANTIALIAS)  # Resize the image to fit the window
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create GUI elements
        entry_coffee = tk.IntVar()
        entry_sugar = tk.IntVar()
        entry_milk = tk.IntVar()


        self.label_coffee = tk.Label(self.root, text="Coffee:")
        self.label_coffee.pack()
        self.entry_coffee = tk.Entry(self.root, textvariable=entry_coffee)
        self.entry_coffee.pack()
        
        self.label_sugar = tk.Label(self.root, text="Sugar:")
        self.label_sugar.pack()
        self.entry_sugar = tk.Entry(self.root, textvariable=entry_sugar)
        self.entry_sugar.pack()
        
        self.label_milk = tk.Label(self.root, text="Milk:")
        self.label_milk.pack()
        self.entry_milk = tk.Entry(self.root, textvariable=entry_milk)
        self.entry_milk.pack()
        
        self.button_make_coffee = tk.Button(self.root, text="Make Coffee", command=self.make_coffee)
        self.button_make_coffee.pack()
        
        self.root.mainloop()

    
    def make_coffee(self):
        print(self.entry_coffee.get())
        self.coffee_u = int(self.entry_coffee.get())
        self.sugar_u = int(self.entry_sugar.get())
        self.milk_u = int(self.entry_milk.get())
        if self.coffee >= self.coffee_u and self.sugar >= self.sugar_u and self.milk >= self.milk_u:
            self.sub_coffee()
            self.sub_milk()
            self.sub_sugar()
            showinfo(title='Information', message="Bon appetite dear quest!")
        else:
            if (self.coffee - self.coffee_u < 0 and self.milk - self.milk_u < 0 and self.sugar - self.sugar_u < 0):
                showinfo(title='Information', message="Not enough ingredients :(")
            else:
                showinfo(title='Information', message="Choose another coffee :) ")

        self.label_sugar = tk.Label(self.root, text='Do you wanna fill ingredients (yes/no): ')
        self.label_sugar.pack()
        self.u = tk.StringVar()
        self.entry_x = tk.Entry(self.root, textvariable=self.u)
        self.entry_x.pack()
        self.entry_x_btn = tk.Button(self.root, text="send", command=self.check)
        self.entry_x_btn.pack()


    def info_was(self):
            showinfo(title='Information', message=(f"Coffee: {self.coffee}, Sugar: {self.sugar}, Milk: {self.milk}"))
    

    def check(self):
        self.fill_was = tk.Button(self.root, text="How many it?", command=self.info_was)
        self.fill_was.pack()
        self.x = str(self.u.get())
        self.y = self.x
        if self.y == "yes":
            self.fill()
            print(self.y)
        else:
            showinfo(title='Information', message="See you again!")
            print(self.y)
                
    def sub_coffee(self):
        self.coffee -= self.coffee_u
        return self.coffee
    
    def sub_sugar(self):
        self.sugar -= self.sugar_u
        return self.sugar
    
    def sub_milk(self):
        self.milk -= self.milk_u
        return self.milk
    
    def fill(self):
        self.c = tk.IntVar()
        self.m = tk.IntVar()
        self.s = tk.IntVar()

        self.fill_coffee = tk.Label(self.root, text="How much coffee do u wanna fill? ")
        self.fill_coffee.pack()
        self.fillc_coffee = tk.Entry(self.root, textvariable=self.c)
        self.fillc_coffee.pack()
        
        self.fill_sugar = tk.Label(self.root, text="How much sugar do u wanna fill? ")
        self.fill_sugar.pack()
        self.fills_sugar = tk.Entry(self.root, textvariable=self.s)
        self.fills_sugar.pack()
        
        self.fill_milk = tk.Label(self.root, text="How much milk do u wanna fill? ")
        self.fill_milk.pack()
        self.fillm_milk = tk.Entry(self.root, textvariable=self.m)
        self.fillm_milk.pack()

        self.fill_is = tk.Button(self.root, text="Fill", command=self.info_is)
        self.fill_is.pack()


    def info_is(self):
        self.coffee += int(self.c.get())
        self.sugar += int(self.s.get())
        self.milk += int(self.m.get())
        showinfo(title='Information', message=(f"Coffee: {self.coffee}, Sugar: {self.sugar}, Milk: {self.milk}"))
    
# Create an instance of CoffeeMachine
din = CoffeeMachine()
