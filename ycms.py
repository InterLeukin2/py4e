import itertools

# 提供的字段列表（去除重复的字段）
fields = [
    "fnd17_oxlcxspebq", "fnd17_shsoutbs", "fnd28_value_05191q", "fnd28_value_05192q", "fnd28_value_05301q", 
    "fnd28_value_05302", "fnd17_pehigh", "fnd17_pelow", "fnd17_priceavg150day", "fnd17_priceavg200day", 
    "fnd17_priceavg50day", "fnd17_pxedra", "fnd17_tbea", "fnd28_newa3_value_18191a", "fnd28_newa3_value_18198a", 
    "fnd28_value_02300a", "mdl175_ebitda", "mdl175_pain"
]

# 去除字段列表中的重复项
fields = list(set(fields))

# 计算所有不同的字段对（有顺序的排列）
permutations = itertools.permutations(fields, 2)

# 初始化计数器
count = 0

# 遍历所有字段对
for a, b in permutations:
    # 输出 Alpha 表达式
    print(f'ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500)')
    count += 1

# 输出组合的总数
print(f'\n总组合数: {count}')