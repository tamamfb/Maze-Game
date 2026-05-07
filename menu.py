import turtle

class MenuItem:
    """Menu button item"""
    def __init__(self, x, y, width, height, text, color, callback):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.callback = callback
        self.is_selected = False
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)
    
    def draw(self):
        """Draw button"""
        self.pen.clear()
        self.pen.setheading(0)
        
        # Button border
        if self.is_selected:
            border_color = "gold"
            border_width = 3
        else:
            border_color = "gray"
            border_width = 2
        
        self.pen.penup()
        self.pen.goto(self.x - self.width/2, self.y + self.height/2)
        self.pen.pendown()
        self.pen.pensize(border_width)
        self.pen.color(border_color)
        
        # Draw rectangle (top-left to bottom-right)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        self.pen.right(90)
        self.pen.forward(self.width)
        self.pen.right(90)
        self.pen.forward(self.height)
        
        # Button text (centered in button)
        self.pen.penup()
        self.pen.goto(self.x, self.y - 7)
        self.pen.color(self.color)
        self.pen.write(self.text, align="center", font=("Arial", 14, "bold"))
    
    def select(self):
        """Select button"""
        self.is_selected = True
        self.draw()
    
    def deselect(self):
        """Deselect button"""
        self.is_selected = False
        self.draw()
    
    def click(self):
        """Execute callback"""
        self.callback()


class Menu:
    """Main menu system"""
    def __init__(self, wn):
        self.wn = wn
        self.items = []
        self.selected_index = 0
        self.background = turtle.Turtle()
        self.background.hideturtle()
        self.background.penup()
        self.background.speed(0)
        self.title = turtle.Turtle()
        self.title.hideturtle()
        self.title.penup()
        self.title.speed(0)
    
    def add_item(self, x, y, text, color, callback):
        """Add menu item"""
        item = MenuItem(x, y, 200, 50, text, color, callback)
        self.items.append(item)
        return item
    
    def draw_title(self, title_text):
        """Draw menu title"""
        self.title.clear()
        self.title.goto(0, 150)
        self.title.color("lime")
        self.title.write(title_text, align="center", font=("Arial", 28, "bold"))
    
    def draw_footer(self, footer_text):
        """Draw menu footer"""
        footer = turtle.Turtle()
        footer.hideturtle()
        footer.penup()
        footer.speed(0)
        footer.goto(0, -250)
        footer.color("gray")
        footer.write(footer_text, align="center", font=("Arial", 10, "normal"))
    
    def draw(self):
        """Draw all menu items"""
        self.background.clear()
        self.background.penup()
        self.background.goto(-400, 300)
        self.background.pendown()
        self.background.color("darkblue")
        
        for _ in range(2):
            self.background.forward(800)
            self.background.right(90)
            self.background.forward(600)
            self.background.right(90)
        
        for item in self.items:
            item.draw()
    
    def select_next(self):
        """Select next item"""
        if self.items:
            self.items[self.selected_index].deselect()
            self.selected_index = (self.selected_index + 1) % len(self.items)
            self.items[self.selected_index].select()
    
    def select_prev(self):
        """Select previous item"""
        if self.items:
            self.items[self.selected_index].deselect()
            self.selected_index = (self.selected_index - 1) % len(self.items)
            self.items[self.selected_index].select()
    
    def click_selected(self):
        """Click selected item"""
        if self.items:
            self.items[self.selected_index].click()
    
    def select_first(self):
        """Select first item"""
        if self.items:
            for item in self.items:
                item.is_selected = False
            self.selected_index = 0
            self.items[self.selected_index].select()
    
    def cleanup(self):
        """Clean up menu"""
        self.background.clear()
        self.title.clear()
        for item in self.items:
            item.pen.clear()
        self.items.clear()
