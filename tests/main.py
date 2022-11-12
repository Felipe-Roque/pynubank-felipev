from pynubank import Nubank
import pandas as pd
import matplotlib

nu = Nubank()



# Recupera as compras feitas no cartão
transactions = nu.get_card_statements()

# Agrupa pelo campo "title" que é a categoria e soma os valores
df = pd.DataFrame(transactions).groupby(['title']).sum()

print(df)
# Plota o gráfico baseado no campo amount
#df['amount'].plot.pie(figsize=(6, 6), autopct='%.2f')