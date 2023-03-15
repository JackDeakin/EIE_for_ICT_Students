import pandas as pd

# Load the CSV file into a pandas DataFrame
articles_df = pd.read_csv('articles.csv')

# Define the keywords to search for
keywords = ['teaching strategy', 'assessment strategy', 'entrepreneurship education', 'teaching effectiveness']

# Check if each row contains any of the keywords in the 'Title' or 'Abstract' columns
articles_df['Relevance'] = articles_df.apply(lambda row: any(keyword in str(row['Title']).lower() or (isinstance(row['Abstract'], str) and keyword in row['Abstract'].lower()) for keyword in keywords), axis=1)

# Filter the DataFrame to only include relevant articles
relevant_articles = articles_df[articles_df['Relevance'] == True]

# Save the relevant articles to a new CSV file
relevant_articles.to_csv('relevant_articles.csv', index=False)

print(f"Found {len(relevant_articles)} relevant articles and saved them to relevant_articles.csv.")

