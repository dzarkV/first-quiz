class Oven:
  def __init__(self):
    self.ingredients: list = []
    self.output: str = None

  def add(self, item):
    self.ingredients.append(item)

  def freeze(self):
    self.output = "snow"

  def boil(self, temperature: float = 100):
    if "lead" in self.ingredients and "mercury" in self.ingredients and temperature >= 5000:
        self.output = "gold"
    elif "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
        self.output = "pizza"
    else:
        self.output = "boiled " + ", ".join(self.ingredients)

  def wait(self):
    self.output = "mixing " + ", ".join(self.ingredients)

  def get_output(self):
    return self.output