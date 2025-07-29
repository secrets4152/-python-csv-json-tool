import pandas as pd

# Criando os dados
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy", "Jack", 
             "Kevin", "Liam", "Mona", "Nina", "Oliver", "Paul", "Quincy", "Rachel", "Sam", "Tina"],
    "age": [30, 25, 35, 40, 28, 33, 26, 31, 27, 32, 
            38, 22, 29, 37, 41, 36, 30, 28, 34, 39],
    "city": ["New York", "London", "Paris", "Berlin", "Madrid", "Rome", "Toronto", "Sydney", "Dubai", "Tokyo", 
             "San Francisco", "Los Angeles", "Melbourne", "Amsterdam", "Boston", "Chicago", "Vancouver", "Seattle", "Boston", "Los Angeles"]
}

# Criando o DataFrame
df = pd.DataFrame(data)

# Salvando como .csv
df.to_csv("people_data.csv", index=False)
