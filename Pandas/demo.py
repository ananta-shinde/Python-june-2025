import pandas as pd

df = pd.read_csv("customers.csv")
print(df.shape)
print(df.columns)
def getListCustomersPersonalInfo():
    print(df.loc[0:10,['Customer Id', 'First Name', 'Last Name','City']])

def getCustomersByCity(city):
    print(df[df["City"]==city])


getListCustomersPersonalInfo()
getCustomersByCity()


