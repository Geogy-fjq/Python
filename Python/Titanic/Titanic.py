# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:32:14 2018

@author: DELL
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

#读取数据
train_data=pd.read_csv('Data/train.csv',encoding='gbk')
test_data=pd.read_csv('Data/test.csv',encoding='gbk')

#总览数据
print("-" * 50)
train_data.info()
print("-" * 50)
test_data.info()
##绘制饼图查看总的存活比例
plt.figure(figsize=(6,6))
train_data['Survived'].value_counts().plot.pie(autopct = '%1.2f%%')

#加工数据
##查看缺失数据
print("-" * 50)
print('train的数据缺失情况为：\n',train_data.isnull().sum())
print("-" * 50)
print('test的数据缺失情况为：\n',test_data.isnull().sum())
##缺失值处理
###对于Embarked：使用众数对缺失值进行替换
train_data.Embarked[train_data.Embarked.isnull()] = train_data.Embarked.dropna().mode().values
print("-" * 50)
print('使用众数替换完成后,train的数据缺失情况为：\n',train_data.isnull().sum())
##对于Age:选择特征数据去预测年龄，使用随机森林模型预测年龄
###选择特征数据去预测年龄
age_pre=train_data[['Age','Survived','Parch','SibSp','Fare']]
age_pre_notnull=age_pre.loc[(train_data['Age'].notnull())]
age_pre_isnull=age_pre.loc[(train_data['Age'].isnull())]
X=age_pre_notnull.values[:,1:]
Y=age_pre_notnull.values[:,0]
###使用随机森林模型预测年龄
RFR=RandomForestRegressor(n_estimators=1000, n_jobs=-1)
RFR.fit(X,Y)
PreAge=RFR.predict(age_pre_isnull.values[:,1:])
train_data.loc[train_data['Age'].isnull(), ['Age']]=PreAge
print("-" * 50)
print('使用中位数替换完成后,train的数据缺失情况为：\n',train_data.isnull().sum())
##对Cabin中的缺失值赋值K0
train_data.Cabin[train_data.Cabin.isnull()]='K0'
print("-" * 50)
print('对Cabin中的缺失值赋值K0后,train的数据缺失情况为：\n',train_data.isnull().sum())

#探索性可视化（查看各个因素与是否生存的关系）
##绘制条形图查看'年龄段'与是否生存的关系
###查看年龄分布情况
print("-" * 50)
print('年龄分布情况为：\n',train_data['Age'].describe())
print("-" * 50)
###绘制条形图查看年龄分布
plt.figure(figsize=(16,5))
train_data['Age'].hist(bins=80)
plt.title('Age Distribution')
plt.xlabel('age')
plt.legend(['number'])
###查看各年龄的生存情况
train_data["Age_int"] = train_data["Age"].astype(int)
train_data.groupby(['Age_int','Survived'])['Survived'].count()
train_data[['Age_int','Survived']].groupby(['Age_int']).mean().plot.bar(figsize=(16,5))
###划分年龄段（儿童，青年，壮年，老年）
A= [0,13,20,65,100]
train_data['Age_Layer'] = pd.cut(train_data['Age'], A)
###查看各分段年龄的人的生存情况
train_data.groupby(['Age_Layer','Survived'])['Survived'].count()
train_data[['Age_Layer','Survived']].groupby(['Age_Layer']).mean().plot.bar(figsize=(7,5))

##绘制条形图查看'船票价格'与是否生存的关系
###绘制条形图查看船票价格分布
plt.figure(figsize=(16,5))
train_data['Fare'].hist(bins=50)
plt.title('Fare Distribution')
plt.xlabel('fare')
plt.legend(['number'])
###查看各船票价格的人的生存情况
train_data["Fare_int"] = train_data["Fare"].astype(int)
train_data.groupby(['Fare_int','Survived'])['Survived'].count()
train_data[['Fare_int','Survived']].groupby(['Fare_int']).mean().plot.bar(figsize=(16,5))
###船票价格分段
F= [0,40,90,270,520]
train_data['Fare_Layer'] = pd.cut(train_data['Fare'], F)
###查看各分段船票价格的人的生存情况
train_data.groupby(['Fare_Layer','Survived'])['Survived'].count()
train_data[['Fare_Layer','Survived']].groupby(['Fare_Layer']).mean().plot.bar(figsize=(7,5))

##绘制条形图查看'性别'与是否生存的关系
train_data.groupby(['Sex','Survived'])['Survived'].count()
train_data[['Sex','Survived']].groupby(['Sex']).mean().plot.bar(figsize=(7,5))

##绘制条形图查看'船舱等级'与是否生存的关系
train_data.groupby(['Pclass','Survived'])['Survived'].count()
train_data[['Pclass','Survived']].groupby(['Pclass']).mean().plot.bar(figsize=(7,5))

##绘制条形图查看'是否有船舱号'与是否生存的关系
train_data.loc[train_data.Cabin.isnull(), 'Cabin'] = 'K0'
train_data['Have_Cabin'] = train_data['Cabin'].apply(lambda x: 0 if x == 'K0' else 1)
train_data.groupby(['Have_Cabin','Survived'])['Survived'].count()
train_data[['Have_Cabin','Survived']].groupby(['Have_Cabin']).mean().plot.bar(figsize=(7,5))

##绘制条形图查看'港口号'与是否生存的关系
train_data.groupby(['Embarked','Survived'])['Survived'].count()
train_data[['Embarked','Survived']].groupby(['Embarked']).mean().plot.bar(figsize=(7,5))

##绘制条形图查看'称呼'与是否生存的关系
##从名字中提取各种称呼并分类
train_data['Title']=train_data['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
train_data['Title']=train_data['Title'].replace(['Dr','Rev','Col','Major','Lady','Sir','Jonkheer','Don','the Countess','Capt','Dona'],'Rare')
train_data['Title']=train_data['Title'].replace(['Mlle','Ms'],'Miss')
train_data['Title']=train_data['Title'].replace('Mme','Mrs')
train_data.groupby(['Title','Survived'])['Survived'].count()
train_data[['Title','Survived']].groupby(['Title']).mean().plot.bar(figsize=(7,5))

##绘制饼图查看'是否有父母/子女'与是否生存的关系
Parch=train_data[train_data['Parch'] != 0]
NoParch=train_data[train_data['Parch'] == 0]
p=plt.figure(figsize=(11,5))
ax1=p.add_subplot(1,2,1)
Parch['Survived'].value_counts().plot.pie(labels=['No Survived', 'Survived'], autopct = '%1.1f%%')
plt.xlabel('Parch')
ax2=p.add_subplot(1,2,2)
NoParch['Survived'].value_counts().plot.pie(labels=['No Survived', 'Survived'], autopct = '%1.1f%%')
plt.xlabel('NoParch')
plt.show()

##绘制饼图查看'是否有兄弟姐妹/配偶'与是否生存的关系
Sibsp=train_data[train_data['SibSp'] != 0]
NoSibsp=train_data[train_data['SibSp'] == 0]
p=plt.figure(figsize=(11,5))
ax1=p.add_subplot(1,2,1)
Sibsp['Survived'].value_counts().plot.pie(labels=['No Survived', 'Survived'], autopct = '%1.1f%%')
plt.xlabel('Sibsp')
ax2=p.add_subplot(1,2,2)
NoSibsp['Survived'].value_counts().plot.pie(labels=['No Survived', 'Survived'], autopct = '%1.1f%%')
plt.xlabel('NoSibsp')
plt.show()





#读取数据
train_data=pd.read_csv('D:/Data/train.csv',encoding='gbk')
test_data=pd.read_csv('D:/Data/test.csv',encoding='gbk')
#特征工程
##将训练集和测试集合并
test_data['Survived']=0
combined_data=train_data.append(test_data)
print("-" * 70)
print('combined数据的缺失情况为：\n',combined_data.isnull().sum())
##缺失值处理
###对于Embarked和Fare：使用众数对缺失值进行替换
combined_data.Embarked[combined_data.Embarked.isnull()] = combined_data.Embarked.dropna().mode().values
combined_data.Fare[combined_data.Fare.isnull()] = combined_data.Fare.dropna().mode().values
###对于Age:选择特征数据去预测年龄，使用随机森林模型预测年龄
age_pre=combined_data[['Age','Survived','Parch','SibSp','Fare']]
age_pre_notnull=age_pre.loc[(combined_data['Age'].notnull())]
age_pre_isnull=age_pre.loc[(combined_data['Age'].isnull())]
X=age_pre_notnull.values[:,1:]
Y=age_pre_notnull.values[:,0]
RFR=RandomForestRegressor(n_estimators=1000, n_jobs=-1)
RFR.fit(X,Y)
PreAge=RFR.predict(age_pre_isnull.values[:,1:])
combined_data.loc[combined_data['Age'].isnull(), ['Age']]=PreAge
###对Cabin中的缺失值赋值K0
combined_data.Cabin[combined_data.Cabin.isnull()]='K0'
print("-" * 70)
print('缺失值插值完成后,combined数据的缺失情况为：\n',combined_data.isnull().sum())
##从名字中提取各种称呼Title,并对Title分类和赋值
combined_data['Title']=combined_data['Name'].apply(lambda x: x.split(',')[1].split('.')[0].strip())
print("-" * 70)
print('combined中Title为：\n',combined_data.Title.value_counts())
###对Title进行重新分类
combined_data['Title']=combined_data['Title'].replace(['Dr','Rev','Col','Major','Lady','Sir','Jonkheer','Don','the Countess','Capt','Dona'],'Rare')
combined_data['Title']=combined_data['Title'].replace(['Mlle','Ms'],'Miss')
combined_data['Title']=combined_data['Title'].replace('Mme','Mrs')
print("-" * 70)
print('combined中分类后Title为：\n',combined_data.Title.value_counts())
###对Title进行数值化处理
title={"Mr":1,"Miss":2,"Mrs":3,"Master":4,"Rare":5}
combined_data['Title']=combined_data['Title'].map(title)
combined_data['Title']=combined_data['Title'].fillna(0)
print("-" * 70)
print('combined中转换为数值型后Title为：\n',combined_data.Title.value_counts())
##对性别进行数值化处理
combined_data['Sex']=combined_data['Sex'].map({'female':1,'male':0}).astype(int)
##对登船港口进行数值化处理
combined_data['Embarked']=combined_data['Embarked'].map({'C':1,'Q':2,'S':3}).astype(int)
##对Fare中的团体票进行人均化处理
combined_data['Fare']=combined_data['Fare']/(combined_data['Fare'].groupby(by=combined_data['Ticket']).transform('count'))
##将SibSp和Parch重新分类为Alone(1:有人陪伴，0：无人陪伴)
combined_data['FamilySize']=combined_data['SibSp']+combined_data['Parch']
combined_data['Alone']=1
combined_data.loc[combined_data['FamilySize']==0,'Alone']=0
##将Ticket中的字母和数字分开，为数字的部分为一类
combined_data['Ticket']=pd.factorize(combined_data['Ticket'].str.split(' ').str[0])[0]
##将Cabin重新分类(1:有，0：无)
combined_data['Cabin']=combined_data['Cabin'].apply(lambda x: 0 if x=='K0' else 1)
##舍去影响不大的因素:Name、Parch、PassengerId、SibSp
combined_data=combined_data[['Age','Fare','Pclass','Sex','Embarked','Alone','Cabin','Ticket','Survived']]

#模型建立——数据处理
##查看原先数据和联合数据的形状
print("-" * 70)
print('train数据的形状为：',train_data.shape)
print('test数据的形状为：',test_data.shape)
print('combined数据的形状为：',combined_data.shape)
##划分训练集和测试集
train_data1=pd.DataFrame(combined_data[:891]) 
test_data1=pd.DataFrame(combined_data[891:]) 
train_dataX=train_data1.drop(['Survived'],axis=1)#训练集
train_dataY=train_data1['Survived']#原训练集中的Survived单独成集
test_dataX=test_data1.drop(['Survived'],axis=1)#测试集
##获得数据和特征名
trainX_data=train_dataX.values#训练集数据
trainX_feature=train_dataX.columns.values#训练集特征名
testX_data=test_dataX.values#测试集数据
testX_feature=test_dataX.columns.values#测试集特征名
print("-" * 70)
print('训练集的特征名为：\n'+str(trainX_feature))
print("-" * 70)
print('训练集的数据为：\n'+str(trainX_data))
print("-" * 70)
print('测试集的特征名为：\n'+str(testX_feature))
print("-" * 70)
print('测试集的数据为：\n'+str(testX_data))

##离差标准化Age和Fare
Scaler=MinMaxScaler().fit(trainX_data[:,(0,1)])#生成规则
trainX_data[:,(0,1)]=Scaler.transform(trainX_data[:,(0,1)])#将规则应用于训练集
testX_data[:,(0,1)]=Scaler.transform(testX_data[:,(0,1)])#将规则应用于测试集
print("-" * 70)
print('离差标准化Age和Fare后的训练集为：\n',trainX_data)
print("-" * 70)
print('离差标准化Age和Fare后的测试集为：\n',testX_data)
print("-" * 70)

#建立模型
##定义通用函数框架
def fit_model(alg,parameters):
    scorer=make_scorer(roc_auc_score)#使用roc_auc_score作为评分标准
    grid=GridSearchCV(alg,parameters,scoring=scorer,cv=5)#使用网格搜索，出入参数
    grid=grid.fit(trainX_data,train_dataY)#训练模型
    print(grid.best_params_)#输出最佳参数
    return grid #返回训练好的模型
##列出需要使用的算法
alg1=SVC(probability=True,random_state=120)#SVM模型
alg2=KNeighborsClassifier(n_jobs=-1)#KNN模型
alg3=DecisionTreeClassifier(random_state=120)#决策树模型
alg4=RandomForestClassifier(random_state=120)#随机森林模型
alg5=GradientBoostingClassifier(random_state=120)#梯度提升树模型
#列出需要调整的参数范围
parameters1={"C":range(5,15),"gamma":[0.6,0.7,0.8,0.9]}
parameters2={'leaf_size':range(1,5),'n_neighbors':range(1,5)}
parameters3={'max_depth':range(1,5),'min_samples_split':[0.3,0.35,0.4,0.45,0.5]}
parameters4={'max_depth':range(1,15),'min_samples_split':[0.05,0.1,0.15,0.2,0.25],'n_estimators':range(10,100,10)}
parameters5={'max_depth':range(5,15),'min_samples_split':[0.05,0.1,0.15,0.2,0.25,0.3,0.35],'n_estimators':range(10,100,10)}
##调参
clf1=fit_model(alg1,parameters1)
clf2=fit_model(alg2,parameters2)
clf3=fit_model(alg3,parameters3)
clf4=fit_model(alg4,parameters4)
clf5=fit_model(alg5,parameters5)
##定义一个保存函数，将预测的结果保存为可以提交的格式
def save(clf,i):
    pred=clf.predict(testX_data)
    sub=pd.DataFrame({'PassengerId':test_data['PassengerId'],'Survived': pred})
    sub.to_csv("Titanic_result{}.csv".format(i), index=False)
##调用函数，完成这5个模型的预测
i=1
for clf in [clf1,clf2,clf3,clf4,clf5]:
    save(clf,i)
    i=i+1
##预测模型准确率
print('预测SVM模型的准确率为：',round(clf1.score(trainX_data,train_dataY),2))
print('预测KNN模型的准确率为：',round(clf2.score(trainX_data,train_dataY),2))
print('预测决策树模型的准确率为：',round(clf3.score(trainX_data,train_dataY),2))
print('预测随机森林模型的准确率为：',round(clf4.score(trainX_data,train_dataY),2))
print('预测梯度提升树模型的准确率为：',round(clf5.score(trainX_data,train_dataY),2))
##定义投票函数
def major(i):
    vote=0
    for clf in [clf1,clf2,clf3,clf4,clf5]:
        pred=clf.predict(testX_data[i:i+1])
        vote=vote+pred
    if vote>2:
        result=1
    else:
        result=0
    return result  
##调用投票函数，并将结果进行保存
L=range(testX_data.shape[0])
pred=list(map(major,L))
sub=pd.DataFrame({'PassengerId':test_data['PassengerId'],'Survived': pred})
sub.to_csv("Data/Titanic_result6.csv", index=False)







