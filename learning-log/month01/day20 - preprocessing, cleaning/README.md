# day 20
 - Pandas fundamental: <br>
```
- loc and iloc:  helps to retrieve the specific data
:df.loc[row_index(0:4)] / df.loc[row_index,['name_of_the_columns']]
: df.iloc[row_index,column_index]

-Filterin and sorting:
result = df[(df['marks']>40) & (df['marks']<50)] & and  | or  ~ not
df_sorted = df.sort_values(by='marks',ascending=False)

-Grouping using groupby(): suppose you want the average marks of each department.
result = df.groupby("Department")['Marks'].mean()
result = df.groupby("Department")['Marks'].agg(['mean','max','min','count'])

-Data Cleaning:
 isna(), notna(), sum(), any(), dropna(),fillna() 
 
- Handling missing values:
 : if numerical use median, if categorical use mode

- handle inconsistent data
- outlier
```
- Feature Preprocessing:
```
- ordinal encoding, label encoding and onehot encoding

```
- Data Leakage and Preprocessing Pipelines:
	 
