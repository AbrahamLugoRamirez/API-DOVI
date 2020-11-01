class Plot:
    
  def __init__(self, y, x, title="title"):
    self.y_label, self.y_value = y
    self.x_label, self.x_value = x
    self.title = title

  def histogram(self, figsize=(32, 40)):
    plt.figure(figsize=figsize)
    plt.barh(self.y_value, self.x_value)
    plt.title(self.title)
    plt.xlabel(self.x_label)
    plt.ylabel(self.y_label)

    # Setting values to each bar
    for index, value in enumerate(self.x_value):
      plt.text(y=index, x=value, s=value)

    plt.show()