import matplotlib.pyplot as plt
'''x= [1,2,3,4,5,6]
y = [i**2 for i in x]
plt.plot(x,y , linestyle = ":" , linewidth = 2.5 , marker = "*" , label ="welcome")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.title("Line squares chart")
plt.show()'''
product = ["TV" , "Washing machine" , "Computer" , "led"]
sales = [1400,1300,800,900]
plt.bar(product , sales , color = "skyblue" )
plt.xlabel("product")
plt.ylabel("sales")
plt.title("Sale of 2030")
plt.grid()
plt.show()