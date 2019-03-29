import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

shopping_list = [['豆奶','莴苣'],
	        ['莴苣','尿布','葡萄酒','甜菜'],
	        ['豆奶','尿布','葡萄酒','橙汁'],
	        ['莴苣','豆奶','尿布','葡萄酒'],
	        ['莴苣','豆奶','尿布','橙汁']]
shopping_df = pd.DataFrame(shopping_list)

df_arr = shopping_df.stack().groupby(level=0).apply(list).tolist()

te = TransactionEncoder()	# 定义模型
df_tf = te.fit_transform(df_arr)
# df_01 = df_tf.astype('int')			# 将 True、False 转换为 0、1 # 官方给的其它方法
# df_name = te.inverse_transform(df_tf)		# 将编码值再次转化为原来的商品名
df = pd.DataFrame(df_tf,columns=te.columns_)


frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)
frequent_itemsets.sort_values(by='support',ascending=False,inplace=True)

association_rule = association_rules(frequent_itemsets,metric='confidence',min_threshold=0.9)	# metric可以有很多的度量选项，返回的表列名都可以作为参数
association_rule.sort_values(by='leverage',ascending=False,inplace=True)    #关联规则可以按leverage排序
print(association_rule)


