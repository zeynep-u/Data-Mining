import numpy as np
import pandas as pd
from faker import Faker


# create faker object
fake = Faker()




# creating a list to hold the datas for the dataset
data = []


# with this for we create 500 random and fake datas for every column
for i in range(500):
    names = fake.unique.first_name()
    last_names = fake.unique.last_name()
    jobs = fake.job()
    self_employed = np.random.choice(['Y','N'])
    age = np.random.randint(0,150)
    weight =  np.random.uniform(0.5,200)
    height = np.random.randint(0, 270)
    data.append([i+1, names, last_names, jobs, self_employed, age, weight, height])




# creating data frame
df = pd.DataFrame(data, columns=['Id', 'First name', 'Last name', 'Job', 'Self-employed', 'Age', 'Weight', 'Height'])


# check if it is good
print(df)


# creating BMI column with using Weight and Height column
df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)


# with this function decide the bmi level for every row in the data set
def bmi_level(bmi):
    if bmi < 18.5:
        return 'too little'
    elif 18.5 <= bmi < 25:
        return 'just right'
    elif 25 <= bmi < 30:
        return 'too much'
    else:
        return 'definitely too much'
   
# applying BMI Level column to data set
df['BMI Level'] = df['BMI'].apply(bmi_level)


# save the data set as mydataBMI as csv file
df.to_csv('mydataBMI.csv', index=False)


# writing the first and the last 7 records of the data set
print("First seven records: \n", df.head(7))


print("Last seven records: \n", df.tail(7))
