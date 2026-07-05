import pandas as pd

pd.set_option('display.max_columns', None) #Показывает ВСЕ колонки
pd.set_option('display.width', 1000) # Разрешить широкую таблицу

df = pd.read_csv('coffee_data.csv')

# print('Всего латте продано:', df['latte'].sum())
# print('Всего продано капучино:', df['cappuccino'].sum())
# print('Всего продано флет уайт', df['flat_white'].sum())

# print('Всего утилизировано молока:', df['milk_waste'].sum())

#3 Расчет процента отходов молока
# total_start = df['milk_start'].sum()
# total_waste = df['milk_waste'].sum()
# waste_percentage = (total_waste/total_start) * 100
#
# print(f'Процент отходов молока: {waste_percentage:.2f}%')

#4 Расчёт финансовой аналитики
print('---Финансовые показатели---')
revenue_latte = df['latte'].sum() * 180
revenue_cappuccino = df['cappuccino'].sum() * 150
revenue_flat_white = df['flat_white'].sum() * 170

total_revenue = revenue_latte + revenue_cappuccino + revenue_flat_white
print(f'Полная выручка кофейни: {total_revenue} руб.')
