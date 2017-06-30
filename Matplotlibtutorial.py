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
plt.plot(x, y, label="Normal Graph Line")

#This will plot x and y again, but with no line in between them, this time the points themselves will show up as red dots.
plt.plot(x, y, 'ro', label="Normal Graph Red Dots")


#This complicated piece of code is the most elegant way i could think og to auto generate a  line of best fit.
# The poly1dfunction can be altered to get lines of best fit in more dimensions.

#     | Makes your X   | This function call generates|                   |
#     | Variables in   | Y based on a 1 dimensinal   |                   |
#     | order, so  it  | polynomial fit algorithm    |Ignore,            |
#     | basically cleans| as described above          |Is Witchcraft      |
#     | x to desired   |                             |                   |
#     |  format        |                             |                   |
#           VV                   VV                       VV
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label="Line of best Fit")

# That last function is defaulted to drawing a line again, and the color numpy uses for a second line is orange,
# If line colors matter you can specify it, or matplotlib will automatically generate new uniqu colors for your lines.


#Here i will demonstrate some fomatting


plt.xlabel('X - Values')
plt.ylabel('Y - Value')
plt.title('This is the title of the first graph/figure. ')

#This displays the legend which displays the different labels for the lines,
# loc=best means location = best locaiton = non-busy area of the graph
plt.legend(loc='best')
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




# Histogram example!

plt.figure(3)

np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()



# Bar graph example!!!
plt.figure(4)
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()


# Example with lines and bar graphs  (removed histograms as they dont make sense to throw on top of each other. )
plt.figure(4)



x = np.arange(-4, 5, 1)

print(x)

y = np.array([8,4,2,1,0,1,2,4,8])
print(y)
plt.plot(x, y, label="Normal Graph")
plt.plot(x, y, 'ro', label="Normal Graph Red Dots")

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), label="Line of best Fit")

plt.bar(x, y)

plt.xlabel('X - Values')
plt.ylabel('Y - Value')
plt.title('This is the title of the first graph/figure. ')

#This displays the legend which displays the different labels for the lines,
# loc=best means location = best locaiton = non-busy area of the graph
plt.legend(loc='best')
plt.show()
