import pandas as pd

def prep_iris(iris):
    iris.drop(columns = ['species_id','measurement_id'], inplace = True)
    iris.rename(columns={'species_name':'species'}, inplace = True)
    df_dummy = pd.get_dummies(iris['species'], drop_first = True)
    iris = pd.concat([iris, df_dummy], axis = 1)
    
    return iris