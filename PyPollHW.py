import pandas as pd 

def process_data(in_csv_path):
    election1 = pd.read_csv(in_csv_path)
    df = pd.DataFrame(election1, columns = ['Candidate'])
    df = pd.DataFrame(election1['Candidate'].value_counts())
    df = df.rename(columns={'Candidate': 'Candidate_Votes'})

    df['total_votes'] = df.Candidate_Votes.sum()
    df['total_won'] = df['Candidate_Votes']/df['total_votes']*100
    df.index.rename('Candidate', inplace=True)
    df.reset_index(inplace=True)
    
    Winner = df["Candidate"].max()
    print("Winner: {}". format(Winner))

    return df

election_results1 = process_data('/Users/hanna/Downloads/election_data_1.csv')
print(election_results1)



election_results2 = process_data('/Users/hanna/Downloads/election_data_2.csv')
print(election_results2)


