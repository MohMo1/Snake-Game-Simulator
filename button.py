import turtle

class Button(turtle.Turtle):

  def __init__(self, x, y, width, height, text, on_click=None, bg_color='white', font_color=None):
    super().__init__(shape="square", visible=False)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.text = text
    self.on_click = on_click
    self.bg_color = bg_color
    self.font_color = font_color
    self.draw()

  def draw(self):
    # Draw the outline of the button
    self.penup()
    self.goto(self.x, self.y)
    self.pendown()
    if self.bg_color:
      self.fillcolor(self.bg_color)
    self.begin_fill()
    self.goto(self.x + self.width, self.y)
    self.goto(self.x + self.width, self.y + self.height)
    self.goto(self.x, self.y + self.height)
    self.goto(self.x, self.y)
    self.end_fill()
    self.penup()

    # Write the text inside the button
    self.goto(self.x + self.width / 2, self.y + self.height / 4)
    if self.font_color:
      self.color(self.font_color)
    self.write(self.text, align="center", font=("Arial", 16, "normal"))

  def is_clicked(self, x, y):
    # Check if the given x, y coordinates are inside the button
    if x > self.x and x < self.x + self.width and y > self.y and y < self.y + self.height:
      return True
    else:
      return False

  def handle_click(self, x, y):
    if self.on_click:
      self.on_click()

