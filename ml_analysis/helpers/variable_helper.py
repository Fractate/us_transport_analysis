def derive_variables(df):
    # set more complex variables based on default ACS data
    df['population_density'] = df['ACS19_5yr_B01001001'] / df['Geo_AREALAND']
    return