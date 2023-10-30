class Oven:
  """ Magical oven that can combine ingredients at 
  different temperatures to craft special materials. """
  
  def __init__(self):
    self.ingredients: list = []
    self.output: str = None


  def add(self, item):
    """ Add an ingredient to be combined """
    self.ingredients.append(item)


  def freeze(self):
    """ Freeze the ingredients """
    self.output = "snow"


  def boil(self, temperature: float = 100):
    """ Boil the ingredients """
    if (
          "lead" in self.ingredients
          and "mercury" in self.ingredients
          and temperature >= 5000
      ):
          self.output = "gold"
    elif (
          "cheese" in self.ingredients
          and "dough" in self.ingredients
          and "tomato" in self.ingredients
      ):
          self.output = "pizza"
    else:
          self.output = "boiled " + ", ".join(self.ingredients)


  def wait(self):
    """ Combine the ingredients with no change in temperature """
    self.output = "mixing " + ", ".join(self.ingredients)


  def get_output(self):
    """ Get the result of crafting materials"""
    return self.output
