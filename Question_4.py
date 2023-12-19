import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from collections import Counter

df = pd.read_csv("winemag-data-130k-clean.csv")

df.dropna(subset=["continent", "points", "price"], inplace=True)

nltk.download("stopwords")

THRESHOLD = 90
color_palette = {
    "Asia": "#4477AA",
    "Europe": "#66CCEE",
    "Africa": "#228833",
    "North America": "#CCBB44",
    "South America": "#EE6677",
    "Oceania": "#AA3377",
    "Tous": "#FFA500",
}
stop = set(
    stopwords.words("english") + list(string.punctuation) + ["but", "with", "drink"]
)

df["description"] = df["description"].str.lower()
df["description"] = df["description"].str.replace("wine", "", regex=False)
df["description"] = df["description"].apply(
    lambda x: " ".join([word for word in x.split() if word not in stop])
)
df_positive = df[df["points"] >= THRESHOLD]

vectorizer = CountVectorizer(stop_words="english")

continents = df["continent"].unique().tolist()
continents.append("Tous")

fig4 = make_subplots(rows=1, cols=1)

continent_top_words = {
    continent: Counter() for continent in continents if continent != "Tous"
}

for continent in continents:
    if continent != "Tous":
        df_continent = df_positive[df_positive["continent"] == continent]
        word_counts_continent = vectorizer.fit_transform(df_continent["description"])
        word_counts_continent_df = pd.DataFrame(
            word_counts_continent.toarray(), columns=vectorizer.get_feature_names_out()
        )
        word_freq_continent = word_counts_continent_df.sum().sort_values(
            ascending=False
        )
        top_words = word_freq_continent.head(10).index.tolist()
        continent_top_words[continent].update(top_words)

        fig4.add_trace(
            go.Bar(
                x=word_freq_continent.head(10),
                y=word_freq_continent.head(10).index,
                orientation="h",
                name=continent,
                marker_color=color_palette[continent],
                visible=False,
            )
        )

all_top_words_counter = Counter(
    word for counter in continent_top_words.values() for word in counter
)
top_10_overall = [word for word, count in all_top_words_counter.most_common(10)]

fig4.add_trace(
    go.Bar(
        x=[all_top_words_counter[word] for word in top_10_overall],
        y=top_10_overall,
        orientation="h",
        name="Tous",
        marker_color=color_palette["Tous"],
        visible=True,
    )
)

buttons = []
for continent in continents:
    label_continent = {
        "Asia": "Asie",
        "Europe": "Europe",
        "Africa": "Afrique",
        "North America": "Amérique du Nord",
        "South America": "Amérique du Sud",
        "Oceania": "Océanie",
    }.get(continent, continent)
    visible_traces = [continent == c for c in continents]
    title = (
        f"Mots les plus fréquents dans les critiques positives ({label_continent})"
        if label_continent != "Tous"
        else "Mots les plus fréquents dans les critiques positives (Tous les continents)"
    )
    buttons.append(
        dict(
            label=label_continent,
            method="update",
            args=[{"visible": visible_traces}, {"title": title}],
        )
    )
buttons.reverse()
fig4.update_layout(
    title="Mots les plus fréquents dans les critiques positives (Tous les continents)",
    updatemenus=[
        {
            "buttons": buttons,
            "direction": "down",
            "pad": {"r": 10, "t": 10},
            "showactive": True,
            "x": 0.0,
            "xanchor": "left",
            "y": 1.2,
            "yanchor": "top",
        }
    ],
    yaxis_title="Mots",
    xaxis_title="Fréquence d'apparition",
)

fig4.show()
