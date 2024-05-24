from typehint_rev import *
daffy_test = Duck()
alert(daffy_test)
alert_duck(daffy_test)
alert_bird(daffy_test)

woody = Bird()
alert(woody)
alert_duck(woody) #needs Duck type but passes argument of type Bird
alert_bird(woody)