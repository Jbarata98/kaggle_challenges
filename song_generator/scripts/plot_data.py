import pandas as pd
import seaborn as sns
from typing import List
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from transformers import AutoTokenizer

# song distribution by album
def plot_wordcloud(data: pd.DataFrame, column_name: str, **kwargs) -> None:
    """
    Generate and display a word cloud for a specified column in a DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame containing the text data.
        column_name (str): The name of the column to generate the word cloud from.

    Returns:
        None
    """
    text_data = data[column_name].str.cat(sep=' ')
    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords = kwargs["stopwords"]).generate(text_data)

    # Create a Matplotlib figure and plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title("Word Cloud")
    plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import AutoTokenizer
from typing import Optional

def plot_token_distribution(data: pd.DataFrame, text_column: str, model_name: str = "gpt2", bins: int = 10) -> None:
    """
    Plot a token distribution histogram for a specified text column in a DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame containing the text data.
        text_column (str): The name of the column containing the text data to analyze and plot.
        model_name (str, optional): The name of the GPT-2 model used for tokenization (default is "gpt2").
        bins (int, optional): The number of bins in the histogram (default is 10).

    Returns:
        None
    """
    # Initialize the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize the text data and count tokens
    token_counts = [len(tokenizer.encode(text)) for text in data[text_column]]

    # Create a DataFrame for the token counts
    df = pd.DataFrame({"Token Count": token_counts})
    
    df = df.sort_values(by="Token Count")

    # Calculate the mean token count
    mean_token_count = df["Token Count"].mean()

    # Create a Seaborn histogram plot
    sns.set(style="whitegrid")
    sns.histplot(data=df, x="Token Count", bins=bins, kde=True)

    # Add a vertical line for the mean token count
    plt.axvline(x=mean_token_count, color='red', linestyle='--', label=f"Mean Token Count: {mean_token_count:.2f}")
    
    # Show the plot
    plt.xlabel("Token Count")
    plt.title("Token Distribution")
    plt.legend()
    plt.show()

