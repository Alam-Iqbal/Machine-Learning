import numpy as np 
import matplotlib.pyplot as plt 
  
def coefficient(x, y):  
    n = np.size(x) 
    mx, my = np.mean(x), np.mean(y) 
    xy = np.sum(y*x) - n*my*mx 
    xx = np.sum(x*x) - n*mx*mx 
    C1 = xy / xx 
    C0 = my - C1*mx 
    return(C0, C1) 
  
def plotregressionline(x, y, b): 
    plt.scatter(x, y, color = "r",marker = "o", s = 50)   
    y_pred = b[0] + b[1]*x   
    plt.plot(x, y_pred, color = "g")   
    plt.xlabel('x') 
    plt.ylabel('y') 
    plt.show() 
  
def main(): 
    x = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
    b = coefficient(x, y) 
    print("Estimated coefficients:\nC0 = {}   \nC1 = {}".format(b[0], b[1])) 
    plotregressionline(x, y, b) 
  
if __name__ == "__main__": 
    main() 
