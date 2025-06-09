# Detector de Spam em E-mails

Projeto acadêmico desenvolvido como parte da disciplina de Inteligência Artificial do curso de **Ciência da Computação** na **Universidade Anhembi Morumbi**.

O objetivo deste projeto é demonstrar o funcionamento de um sistema básico de detecção de spam, utilizando técnicas de processamento de linguagem natural e aprendizado de máquina para identificar e classificar e-mails como **spam** ou **não spam**.

---

## 🧠 Funcionamento

O sistema funciona da seguinte forma:

1. **Carrega um conjunto de dados com e-mails rotulados** (spam ou ham).
2. **Limpa o texto dos e-mails**, removendo pontuação e palavras irrelevantes.
3. **Transforma os textos em números** usando TF-IDF (técnica de vetorização de texto).
4. **Treina um modelo de Regressão Logística** com esses dados.
5. Oferece uma **interface gráfica simples** para inserir ou colar um e-mail e ver o resultado da análise em tempo real.

---

## 🛠 Ferramentas Utilizadas

- **Codificado em Python**
- **Tkinter** – Para criar a interface gráfica
- **NLTK** – Para limpeza e tokenização do texto
- **Scikit-learn** – Para vetorização (TF-IDF) e treinamento do modelo
- **Pandas** – Para manipulação dos dados
