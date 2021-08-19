import pandas as pd
from sklearn.model_selection import train_test_split

def prep_iris(iris):
    iris.drop(columns = ['species_id','measurement_id'], inplace = True)
    iris.rename(columns={'species_name':'species'}, inplace = True)
    df_dummy = pd.get_dummies(iris['species'], drop_first = True)
    iris = pd.concat([iris, df_dummy], axis = 1)
    
    return iris

def prep_titanic(titanic):
    titanic.embark_town.fillna('Southampton', inplace = True)
    dummy_df = pd.get_dummies(titanic[['sex','embark_town']], dummy_na=False, drop_first=[True, True])
    titanic = pd.concat([titanic, dummy_df], axis = 1)
    titanic.drop(columns = ['sex', 'embark_town','age', 'passenger_id', 'embarked','class','deck'], inplace = True)
    titanic.rename(columns = {'sibsp':'num_sib_and_sp', 'parch':'num_par_and_ch'}, inplace = True)

    return titanic

def train_validate_test_split(df, target, seed = 123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test
