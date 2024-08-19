import pandas as pd

data={
    'animal':['cat','cat','dog','snake','dog','cat','snake','cat','dog','dog'],
    'age':[2,3,4,0.5,4,5,6,3,7,3],
    'visits':[1,2,4,5,2,1,2,6,2,5]
}
df1=pd.DataFrame(data)
print(df1)
filtered_df = df1[df1['age'] > 3]
print('Filter data By age is greter than 3:--  \n',filtered_df)
print('Filter data By age is greter than 3 with 2 columns:--  \n',filtered_df[['animal','visits']])

replace_value=df1.replace({'snake': 'cow'})
print(replace_value)
data2={
    'animal':['snake','snake'],
    'age':[2,4],
    'visits':[1,2,]
}
df2=pd.DataFrame(data2)
df_combined =  pd.concat([df1, df2], ignore_index=True)
print('df_combined \n', df_combined)