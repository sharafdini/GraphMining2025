# this a package named pgu version 001
country = 'IRAN'

def salam(c=None):
    if c==None:
        return f'Salam, How are you?, I am from IRAN'
    else: 
        return f'Salam, How are you?, I am from {c}' 

def _salam(c='IRAN'):
        return f'Salam, How are you?, I am from {c}'

class gigili:  
  def __init__(self, name='IRAN'):
    self.name = name

  def hi(self):
    print(f'Salam, esme man {self.name}')
  
  def bye(self):
      return self.name 
    

