from textblob import TextBlob
import os
import matplotlib.pyplot as plt

INPUT_FILE = os.path.join('inputs', 'sample_text.txt')
OUTPUT_FILE = os.path.join('outputs', 'analysis_results.txt')
PLOT_FILE = os.path.join('outputs', 'sentiment_plot.png')

def analyze_text():
    
    os.makedirs('outputs', exist_ok=True)
    
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        sentences = [line.strip() for line in f if line.strip()]
    
    
    results = []
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_f:
        out_f.write("ANÁLISE DE SENTIMENTOS\n======================\n")
        
        for i, sent in enumerate(sentences, 1):
            analysis = TextBlob(sent)
            polarity = analysis.sentiment.polarity
            results.append(polarity)
            
            
            if polarity > 0:
                sentiment = "POSITIVO 😊"
            elif polarity < 0:
                sentiment = "NEGATIVO 😠"
            else:
                sentiment = "NEUTRO 😐"
            

            out_f.write(f"\nFRASE {i}: {sent}\n")
            out_f.write(f"Sentimento: {sentiment} (Score: {polarity:.2f})\n")
    
    
    plt.figure(figsize=(10, 5))
    plt.bar(range(1, len(results)+1), results, color=['green' if x > 0 else 'red' if x < 0 else 'gray' for x in results])
    plt.title('Análise de Sentimento das Frases')
    plt.xlabel('Número da Frase')
    plt.ylabel('Polaridade')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.savefig(PLOT_FILE)
    plt.close()

    print(f"Análise concluída! Resultados salvos em {OUTPUT_FILE} e {PLOT_FILE}")

if __name__ == "__main__":
    analyze_text()
