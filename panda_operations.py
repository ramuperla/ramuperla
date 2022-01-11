import pandas as pd

user_details=[{"First_Name":"RamaKrishna","Last_Name":"Perla","Age":32,"Profession":"Software"},
              {"First_Name":"Manikanta","Last_Name":"Perla","Age":29,"Profession":"CA"}]

#Converting list to data_frame
data=pd.DataFrame(user_details)

#Addition of row to data_frame
new_user=[{"First_Name":"Renuka","Last_Name":"Perla","Age":31,"Profession":"CA"}]
new_user_to_df=pd.DataFrame(new_user)
final_data_frame=pd.concat([data,new_user_to_df],ignore_index=True)

#Addition of column to data_frame
Full_Name=final_data_frame["First_Name"]+" "+final_data_frame["Last_Name"]
final_data_frame["Full_Name"]=Full_Name


#Select specific rows from data_frame based on a condition
new_df=final_data_frame.loc[final_data_frame["Age"]<30]


#Select specific columns from data_frame
#method1 using column index
print(new_df[new_df.columns[1:]])
#method2 using column name
print(new_df[["Full_Name","Age"]])

#Append dataframe to existing xls
with pd.ExcelWriter('Family_Details.xlsx',mode="a", engine="openpyxl") as writer:
    new_df.to_excel(writer,sheet_name="Family_Details.xlsx")