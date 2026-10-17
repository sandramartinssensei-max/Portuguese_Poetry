import pandas as pd
import numpy as np

# Carregar o dataset base que criaste
df_base = pd.read_csv('poesia_contemporanea_portugal.csv')

# Vamos usar uma técnica de expansão controlada para gerar 500 linhas simuladas e realistas
np.random.seed(42)
n_linhas_alvo = 500

# Listas de apoio para simulação realista baseada no ecossistema literário português
temas = ['Matéria/Corpo', 'Solidão/Noite', 'Quotidiano/Doméstico', 'Natureza/Mar', 'Existencialismo/Fúria', 'Tempo/Finitude', 'Identidade/Corpo']
keywords_pool = ['ferro', 'cinza', 'casa', 'mar', 'noite', 'tempo', 'silêncio', 'pedra', 'luz', 'mão', 'raiz', 'esquina']

dados_expandidos = []

for i in range(n_linhas_alvo):
    # Escolher uma linha base aleatoriamente para manter a consistência do autor
    base_row = df_base.sample(n=1).iloc[0]
    
    id_poema_novo = 200 + i
    ano_pub_novo = np.randint(1960, 2025)
    tema_novo = np.random.choice(temas)
    kw_novo = f"{np.random.choice(keywords_pool)}, {np.random.choice(keywords_pool)}"
    
    linha = {
        'id_poeta': base_row['id_poeta'],
        'nome_poeta': base_row['nome_poeta'],
        'genero': base_row['genero'],
        'ano_nascimento': base_row['ano_nascimento'],
        'concelho_origem': base_row['concelho_origem'],
        'num_livros_publicados': base_row['num_livros_publicados'],
        'concursos_vencidos': base_row['concursos_vencidos'],
        'id_poema': id_poema_novo,
        'titulo_poema': f"Composição #{i+1}",
        'ano_publicacao': ano_pub_novo,
        'tema_principal': tema_novo,
        'palavras_chave': kw_novo,
        'texto_amostra': f"Excerto simulado de poesia focado em {tema_novo.lower()}..."
    }
    dados_expandidos.append(linha)

# Criar o novo DataFrame completo com 500 linhas
df_final = pd.DataFrame(dados_expandidos)

# Guardar o resultado final pronto a usar no Tableau e GitHub
df_final.to_csv('poesia_portuguesa_500_linhas.csv', index=False)
print("Dataset de 500 linhas gerado com sucesso!")
