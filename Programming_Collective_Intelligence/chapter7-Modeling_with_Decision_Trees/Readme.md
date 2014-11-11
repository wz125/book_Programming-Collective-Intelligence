Modeling with Decision Trees 决策树模型
==

+ 根据某一特征将数据分成两个数据集，主要目的是增加纯度
+使用“[信息熵](http://zh.wikipedia.org/zh-cn/%E7%86%B5_(%E4%BF%A1%E6%81%AF%E8%AE%BA))”计算纯度
+ 针对每一列中每个列值做熵的值计算，并记录没列最大熵值。第一次计算全部的熵，后续按照树状递归计算子树的熵；
+ 决策树一个主要应用是对可观测商品价格在不同特征作用下的理解
+ 决策树可以同时接受分类和数值数据
+ 决策树处理大数据量性能问题明显；只能处理简单判断分类；


> *Entropy(熵):在集合论中，熵代表的是集合的无序程度，即信息差异度。*
> *CART (Classification and Regression Trees) 分类回归数*

**Example logger:**
```python
Recursive Tree Building
+current_score=1.50524081494 所有数据的熵平均值
++rows=[ 全部数据集]
+col=0 按照第一列分类
col=0 value=(direct) gain=0.0409491944517 best_gain=0.0 True
col=0 value=digg gain=0.0929944817249 best_gain=0.0409491944517 True
col=0 value=google gain=0.393422983787 best_gain=0.0929944817249 True
col=0 value=slashdot gain=0.26517495061 best_gain=0.393422983787 False
col=0 value=kiwitobes gain=0.0929944817249 best_gain=0.393422983787 False
+col=1 按照第二列分类
col=1 value=New Zealand gain=0.0409491944517 best_gain=0.393422983787 False
col=1 value=UK gain=0.00685528675433 best_gain=0.393422983787 False
col=1 value=USA gain=0.0177239987079 best_gain=0.393422983787 False
col=1 value=France gain=0.0358798771737 best_gain=0.393422983787 False
+col=2
col=2 value=yes gain=0.206445874249 best_gain=0.393422983787 False
col=2 value=no gain=0.206445874249 best_gain=0.393422983787 False
+col=3
col=3 value=12 gain=0.0 best_gain=0.393422983787 False
col=3 value=18 gain=0.0409491944517 best_gain=0.393422983787 False
col=3 value=19 gain=0.17903575564 best_gain=0.393422983787 False
col=3 value=21 gain=0.354842567659 best_gain=0.393422983787 False
col=3 value=23 gain=0.294736717803 best_gain=0.393422983787 False
col=3 value=24 gain=0.127625566196 best_gain=0.393422983787 False
+best_gain=0.393422983787 best_criteria=(0, 'google') 最后选择gain最大的分类点第0列 google
>>current_score=1.37095059445 对第0列=google?拆分成两个数据集
>>row=['google', 'France', 'yes', 23, 'Premium']
>>row=['google', 'UK', 'no', 21, 'Premium']
>>row=['google', 'USA', 'no', 24, 'Premium']
>>row=['google', 'UK', 'no', 18, 'None']
>>row=['google', 'UK', 'yes', 18, 'Basic']
+col=0
col=0 value=google gain=0.0 best_gain=0.0 False
+col=1
col=1 value=USA gain=0.170950594455 best_gain=0.0 True
col=1 value=UK gain=0.419973094022 best_gain=0.170950594455 True
col=1 value=France gain=0.170950594455 best_gain=0.419973094022 False
+col=2
col=2 value=yes gain=0.419973094022 best_gain=0.419973094022 False
col=2 value=no gain=0.419973094022 best_gain=0.419973094022 False
+col=3
col=3 value=24 gain=0.170950594455 best_gain=0.419973094022 False
col=3 value=18 gain=0.0 best_gain=0.419973094022 False
col=3 value=21 gain=0.970950594455 best_gain=0.419973094022 True
col=3 value=23 gain=0.419973094022 best_gain=0.970950594455 False
+best_gain=0.970950594455 best_criteria=(3, 21)
>>current_score=0.0
>>row=['google', 'France', 'yes', 23, 'Premium']
>>row=['google', 'UK', 'no', 21, 'Premium']
>>row=['google', 'USA', 'no', 24, 'Premium']
+col=0 对0列，都为Premium
col=0 value=google gain=0.0 best_gain=0.0 False
+col=1 对1列 都为Premium
col=1 value=USA gain=0.0 best_gain=0.0 False
col=1 value=UK gain=0.0 best_gain=0.0 False
col=1 value=France gain=0.0 best_gain=0.0 False
+col=2
col=2 value=yes gain=0.0 best_gain=0.0 False
col=2 value=no gain=0.0 best_gain=0.0 False
+col=3
col=3 value=24 gain=0.0 best_gain=0.0 False
col=3 value=21 gain=0.0 best_gain=0.0 False
col=3 value=23 gain=0.0 best_gain=0.0 False
+best_gain=0.0 best_criteria=None 所有的都正确，到达叶节点
+decisionnode:{'Premium': 3}  
```
