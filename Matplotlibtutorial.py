import matplotlib.pyplot as plt
import numpy as np

#in order to get this working you need to frst download and install matplotlib
#To do so open up a terminal and type "pip3 install matplotlib" and it should be handled for you

# IMPORTANT!!!! DOCUMENTATION FOR MATPLOTLIB.PYPLOT  https://matplotlib.org/users/pyplot_tutorial.html
# That link is a tutorial but it also contains a detailed listing of all of hte options for the functions such as plot etc in the chart.


x = np.arange(-4, 5, 1)

print(x)

y = np.array([8,4,2,1,0,1,2,4,8])
print(y)


# x and y should now represent the function y =  x ** 2 on the interval from -5 to 5


# Figures are individual graphcs/charts.  You add all elements to the same chart until you call
# This function again with a new figure name as a parameter.
plt.figure(0)


#plots just the x and y variables onto the graph, and connects them with a blue line by default.
plt.plot(x, y)

#This will plot x and y again, but with no line in between them, this time the points themselves will show up as red dots.
plt.plot(x, y, 'ro')


#This complicated piece of code is the most elegant way i could think og to auto generate a  line of best fit.
# The poly1dfunction can be altered to get lines of best fit in more dimensions.

#     | Makes your X   | This function call generates|                   |
#     | Variables in   | Y based on a 1 dimensinal   |                   |
#     | order, so  it  | polynomial fit algorithm    |Ignore,            |
#     | basically cleans| as described above          |Is Witchcraft      |
#     | x to desired   |                             |                   |
#     |  format        |                             |                   |
#           VV                   VV                       VV
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))

# That last function is defaulted to drawing a line again, and the color numpy uses for a second line is orange,
# If line colors matter you can specify it, or matplotlib will automatically generate new uniqu colors for your lines.


#Here i will demonstrate some fomatting


plt.xlabel('X - Values')
plt.ylabel('Y - Value')
plt.title('This is the title of the first graph/figure. ')
plt.show()

#There are many much more advanced functionalities of this matplotlib,
# however it is extremely complicated outside of these functionalities.
# Just ping me and let me knw what you want to do it its outside of the range of this tutorial,
# IT WILL SAVE YOU COUNTLESS HOURS OF FIGURING THIS SHIT OUT
# just trust me...data visualization is complex



#Here i am demonstrating that the tutorial form online has some cool demos too,
# This will plot a decaying cosign functino and it shows how to add subplots to the same figure.  essentailly how to
# put two graphs in the same window(this will hopefully make sense as you run the program. )

# NOTE: How the title and the x and y labels fit to this set of data, should help clarify why a subplot and a new figure are different.

plt.figure(1)
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)



plt.subplot(211)
plt.xlabel('X - Values')
plt.ylabel('Y - Value')
plt.title('This is the title of the SECOND graph, First Subplot. ')

plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)

plt.xlabel('X - Values')
plt.ylabel('Y - Value')
plt.title('This is the title of the SECOND graph, SECOND Subplot. ')

plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()

