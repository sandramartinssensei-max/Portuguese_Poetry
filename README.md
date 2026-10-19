# Poesia portuguesa
Visão Geral do Projeto
Este repositório explora um *corpus* estruturado de poesia portuguesa, integrando dados demográficos de autores, metadados editoriais, processamento de texto e Análise Exploratória de Dados. 

## Principais Dimensões de Análise
1. **Representação de Género:** Distribuição de publicações e reconhecimento em concursos literários ao longo do tempo.
2. **Distribuição Temática:** Mapeamento de tópicos recorrentes e o seu peso e evolução na literatura.
3. **Análise Geográfica:** Mapeamento por concelhos do impacto cultural e publicação regional em Portugal.
   
## Painéis Interativos (Tableau Public)

Abaixo podes navegar e interagir diretamente com os painéis construídos para explorar os diferentes níveis da análise:
| Painel / Dashboard | Descrição & Foco Analítico | Acesso Direto |
| :--- | :--- | :---: |
| **01. Painel Género** | Análise comparativa da distribuição de temas principais, número de publicações e impacto no tempo cruzados com o género do autor. | [**Ver Painel 1**](https://public.tableau.com/views/PoesiaPortuguesa/Gnero?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link) |
| **02. Painel Tema** | *Heatmap* de temáticas principais e seu peso espaço-social. | [**Ver Painel 2**](https://public.tableau.com/app/profile/sandra.martins/viz/Poesiaportuguesa-paineltema/Painel-Tema) |
| **03. Painel Concelho** | Visão local, mais concretamente, a nível de concelho cruzada com número de publicações, concursos vencidos e temas abordados. | [**Ver Painel 3**](https://public.tableau.com/app/profile/sandra.martins/viz/PoesiaPortuguesa-PainelConcelho/PainelConcelho) |

---

## Tecnologias e Ferramentas Utilizadas
* **Python (`pandas`, `matplotlib`, `seaborn`):** Limpeza e tratamento de dados brutos, análise exploratória e estruturação de métricas.
* **Tableau Public:** Construção de painéis e *dashboards* interativos e dinâmicos.

---

## 📁 Estrutura do Repositório
* `data/` — Datasets e bases de dados tratadas (`.csv` / `.xlsx`).
* `scripts/` — Scripts em Python para tratamento de dados e análise exploratória.
* `README.md` — Documentação global do projeto.
