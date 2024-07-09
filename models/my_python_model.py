def model(dbt, session):

    my_sql_model_df = dbt.ref("customers")

    # final_df = ...  # stuff you can't write in SQL!

    return my_sql_model_df