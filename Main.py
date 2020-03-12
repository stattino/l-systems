from LSystem import *
import numpy as np
import matplotlib.pyplot as plt
from pylab import get_current_fig_manager


hilbertcurve = LSystem("Hilbert curve", "X", ["X=-YF+XFX+FY-", "Y=+XF-YFY-FX+"], starting_angle=0, angle_increment=90)
levy_c = LSystem("Levy C curve", "F", ["F=+F--F+"], starting_angle=0, angle_increment=45)
cantor = LSystem("Cantor set", "AB", ["A=ABA", "B=BBB"], starting_angle=0, angle_increment=90)
sierpinsky = LSystem("Sierpinsky triangle", "F-G-G", ["F=F-G+F+G-F", "G=GG"], starting_angle=0, angle_increment=120)
koch = LSystem("Koch curve", "F", ["F=F+F-F-F+F"], starting_angle=0, angle_increment=90)
algae = LSystem("Algae growth", "A", ["A=AB", "B=A"], starting_angle=0, angle_increment=20)
dragon = LSystem("Dragon curve", "FX", ["X=X+YF+", "Y=-FX-Y"], starting_angle=90, angle_increment=90)

#levy_c.test_system()
#sierpinsky.test_system()
#koch.test_system()
#algae.test_system()
#dragon.test_system()

#dragon.age_system(10)
#dragon.easy_plot()

#koch.age_system(4)
#koch.easy_plot()

sierpinsky.age_system(2)
sierpinsky.easy_plot()
sierpinsky.age_system(2)
sierpinsky.easy_plot()
sierpinsky.age_system(2)
sierpinsky.easy_plot()

#algae.age_system(4)
#algae.easy_plot()

#levy_c.age_system(10)
#levy_c.easy_plot()

#hilbertcurve.age_system(5)
#hilbertcurve.easy_plot()
plt.show()
