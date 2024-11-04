import pandas as pd

file_path = r'E:\hash Agile\python\data.csv'  
try:
    data = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
except FileNotFoundError:
    print("The file path is incorrect or the file does not exist.")
    exit()

collections = {}

def createCollection(p_collection_name):
    global collections
    collections[p_collection_name] = pd.DataFrame()
    print(f"Collection '{p_collection_name}' created.")

def indexData(p_collection_name, p_exclude_column):
    global collections
    if p_collection_name in collections and collections[p_collection_name].empty:
        if p_exclude_column in data.columns:
            collections[p_collection_name] = data.drop(columns=[p_exclude_column])
            print(f"Data indexed in '{p_collection_name}', excluding column '{p_exclude_column}'.")
        else:
            print(f"Column '{p_exclude_column}' does not exist in the data.")
    else:
        print(f"Collection '{p_collection_name}' does not exist or already has data.")

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        if p_column_name in collections[p_collection_name].columns:
            results = collections[p_collection_name][collections[p_collection_name][p_column_name] == p_column_value]
            print(f"Search results in '{p_collection_name}' where {p_column_name} = {p_column_value}:\n{results}")
        else:
            print(f"Column '{p_column_name}' does not exist in '{p_collection_name}'.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")

def getEmpCount(p_collection_name):
    if p_collection_name in collections:
        count = collections[p_collection_name].shape[0]
        print(f"Employee count in '{p_collection_name}': {count}")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")

def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        if 'EmployeeID' in collections[p_collection_name].columns:
            collections[p_collection_name] = collections[p_collection_name][collections[p_collection_name]['EmployeeID'] != p_employee_id]
            print(f"Employee with ID '{p_employee_id}' deleted from '{p_collection_name}'.")
        else:
            print(f"Column 'EmployeeID' does not exist in '{p_collection_name}'.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")

def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        if 'Department' in collections[p_collection_name].columns:
            department_counts = collections[p_collection_name]['Department'].value_counts()
            print(f"Department counts in '{p_collection_name}':\n{department_counts}")
        else:
            print(f"Column 'Department' does not exist in '{p_collection_name}'.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")

if __name__ == "__main__":
    v_nameCollection = 'Surendhar'
    v_phoneCollection = '5625'

    createCollection(v_nameCollection)
    createCollection(v_phoneCollection)
    getEmpCount(v_nameCollection)
    indexData(v_nameCollection, 'Department')
    indexData(v_phoneCollection, 'Gender')
    getEmpCount(v_nameCollection)
    delEmpById(v_nameCollection, 'E02003')
    getEmpCount(v_nameCollection)
    searchByColumn(v_nameCollection, 'Department', 'IT')
    searchByColumn(v_nameCollection, 'Gender', 'Male')
    searchByColumn(v_phoneCollection, 'Department', 'IT')
    getDepFacet(v_nameCollection)
    getDepFacet(v_phoneCollection)
