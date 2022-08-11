import pandas as pd
class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):

        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        Remove rows that has column names.
        This error originated from the data collection stage.
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count'].index
        self.df = df.drop(unwanted_rows, inplace=True)
        self.df = df[df['polarity'] != 'polarity']

        # self.drop_duplicate(self.df)
        return self.df

    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        self.df = self.df.drop_duplicates().drop_duplicates(subset='original_text') # self.df.drop_duplicates(subset='original_text')
        
        
        return df


    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """

        self.df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
        
        self.df = self.df[self.df['created_at'] >= '2020-12-31' ]
        
        return self.df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df['polarity'] = pd.to_numeric(self.df['polarity'], errors='coerce')

        self.df['retweet_count'] = pd.to_numeric(self.df['retweet_count'], errors='coerce')

        self.df['favorite_count'] = pd.to_numeric(self.df['favorite_count'], errors='coerce')
        
        return self.df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        self.df = self.df.query("lang == 'en' ")
        
        return self.df


if __name__ == "__main__":
    tweets_json = pd.read_json("./data/africa_twitter_data - Copy.json", lines=True)
    cleaner = Clean_Tweets(tweets_json)

    df = cleaner.drop_unwanted_column(cleaner.df)
    df = cleaner.drop_duplicate(df)
    df = cleaner.convert_to_numbers(df)
    df = cleaner.convert_to_datetime(df)
    df = cleaner.remove_non_english_tweets(df)

    df.to_csv('cleaned_tweet_data.csv', index=False)
    df.to_json('data/cleaned_tweet_data.json')

