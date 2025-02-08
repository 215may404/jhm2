import pandas as pd
import matplotlib pyplot as plt
data = {
  'Month' : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
  'Sales' : [380,400,660,800,900,1200,1600,2200,1500,1100,600,250]
}
df = pd.DataFrame(data)
filename = 'sales.csv'
df.to_csv(filename, index = False)
plt.bar(Month,Sales,color = 'green',wide = 0.5)
plt.title("Bar Chart of Ice-cream sales")
plt.xlabel("Month")
plt.ylabel("Sales(in thousand dollars)") 
plt.savefig("Ice-cream_sales.png")
