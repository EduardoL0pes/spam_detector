import tkinter as tk
from tkinter import messagebox
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# ========== Funções de Limpeza de Texto ==========
def clean_text(text):
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = nltk.word_tokenize(text.lower())
    stop_words = set(stopwords.words('portuguese'))  # Pode trocar de idioma se necessário.
    cleaned = [word for word in tokens if word not in stop_words]
    return ' '.join(cleaned)

# ========== Carregar Dados e Treinar Modelo (uma única vez) ==========
df = pd.read_csv('spam_data.csv.txt')
df['clean_text'] = df['text'].apply(lambda x: clean_text(x))

tfidf = TfidfVectorizer(max_features=3000)
X = tfidf.fit_transform(df['clean_text'])
y = df['label'].map({'ham': 0, 'spam': 1})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X, y)

# ========== Função de Classificação ==========
def classify_email():
    raw_text = input_text.get("1.0", tk.END).strip()
    if not raw_text:
        result_label.config(text="Digite um e-mail para análise.")
        return

    cleaned = clean_text(raw_text)
    vectorized = tfidf.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    if prediction == 1:
        result_label.config(text="⚠️ Este e-mail parece ser SPAM!", fg="red")
    else:
        result_label.config(text="✅ Este e-mail parece seguro (não spam).", fg="green")

# ========== Criar Interface Gráfica ==========
root = tk.Tk()
root.title("Detector de Spam - Sistema Local")
root.geometry("600x400")
root.resizable(False, False)

title_label = tk.Label(root, text="Digite ou cole o conteúdo do e-mail:", font=("Arial", 14))
title_label.pack(pady=10)

input_text = tk.Text(root, height=10, width=70, wrap='word', font=("Arial", 12))
input_text.pack(pady=10)

analyze_button = tk.Button(root, text="Analisar E-mail", command=classify_email, font=("Arial", 12), bg="blue", fg="white")
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, justify="center")
result_label.pack(pady=10)

footer_label = tk.Label(root, text="© 2025 - Sistema de Detecção de Spam", font=("Arial", 10), fg="gray")
footer_label.pack(side="bottom", pady=10)

# ========== Rodar Aplicação ==========
root.mainloop()