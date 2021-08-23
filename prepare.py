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

def prep_telco(customers):
    customers.drop_duplicates(inplace = True)
    #Convert total_charges to float
    customers.total_charges = customers.total_charges.str.strip()
    customers.total_charges = customers.total_charges.str.replace('[$,]','')
    customers.total_charges = pd.to_numeric(customers['total_charges'])
    #Select the categorical columns that need dummy variables (ignoring passenger_id)
    cat_cols = customers.select_dtypes('object').columns[1:]
    #Create dummy variables for categorical variables and concat
    dummy_df = pd.get_dummies(customers[cat_cols], dummy_na = False, drop_first = True)
    customers = pd.concat([customers, dummy_df], axis = 1)
    #Drop unnecessary columns
    customers.drop(columns = cat_cols, inplace = True)
    customers.drop(columns = ['customer_id','phone_service_Yes','contract_type_id', 'contract_type_id.1', 'internet_service_type_id', 'internet_service_type_id.1', 'payment_type_id', 'payment_type_id.1'], inplace = True)
    
    return customers


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
