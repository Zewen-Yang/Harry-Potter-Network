# Define a function that filters out non-character entities
def filter_entity(ent_list, character_df):
    # Extract the list of first names from the character DataFrame, cleaning up the data first
    firstname_list = list(character_df.Character_firstname
                          .str.replace('Mr\. ','', regex=True)
                          .str.replace('Mrs\. ','', regex=True)
                          .str.replace('Aunt','', regex=True)
                          .str.replace('Miss','', regex=True)
                          .str.replace('Uncle','', regex=True)
                         ) 
    # Return a new list containing only those entities that are in the character DataFrame or the first name list
    return [ent for ent in ent_list 
            if ent in list(character_df.Character) 
            or ent in firstname_list
           ]
