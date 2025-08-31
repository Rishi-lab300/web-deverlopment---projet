import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [10,20,30,40,50,60]
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Line chart")

plt.subplot(1,2,2)
plt.bar(x,y,color = 'blue' , label = 'calculating just')
plt.title("bar chart")
plt.legend()
plt.tight_layout()

plt.subplots(2,1)
countries =["india" , "China" , "america" , "Japan"]
population = [18900,22000,20000,12121] 
plt.pie(population , labels = countries , autopct='%1.1f%%' , colors = ['gold','red','yellow','green'] )
plt.title("Popultions of major countries .")
plt.legend()
plt.tight_layout
plt.show()