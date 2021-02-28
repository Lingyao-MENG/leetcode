from math import *
import operator


def calcShannonEnt(dataSet):
    #函数功能：计算给定数据集信息熵
    numEntries = len(dataSet)
    labelCounts = {}          #字典存储 键：类别，值：类别的个数

    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    #计算 所有类别的信息*概率 之和
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            #reducedFeatVec 存储 去除给定特征值后的数据
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #计算每条数据共有多少个特征
    baseEntropy = calcShannonEnt(dataSet)  #计算原数据集的熵（混乱程度）
    bestInfoGain = 0.0                     #初始化 最好的信息增益
    bestFeature = -1
    for i in range(numFeatures):        #遍历所有特征，最后计算每个特征的信息增益，选取最好的
        featList = [example[i] for example in dataSet]  #创建对应特征的属性值列表
        uniqueVals = set(featList)       #得到当前特征下的不同的属性值集合
        newEntropy = 0.0           #初始化熵

        #计算当前特征划分后的数据子集的熵
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)

            infoGain = baseEntropy - newEntropy   #计算当前特征划分后的数据子集的信息增益

            if (infoGain > bestInfoGain):       #计算的信息增益如果比现有的大，则重新赋值。找到最好的信息增益
                bestInfoGain = infoGain
                bestFeature = i
    return bestFeature     #返回最有决定性的特征标识


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
        sortedClassCount = sorted(
            classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]               #结束递归的条件：数据集类别属于同一类
    if len(dataSet[0]) == 1:              #结束递归的条件：已没有用于划分的特征
        return majorityCnt(classList)

    bestFeat = chooseBestFeatureToSplit(dataSet)  #选择最好的特征
    bestFeatLabel = labels[bestFeat]

    myTree = {bestFeatLabel:{}}        #使用最好的特征初始化决策树
    del(labels[bestFeat])

    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)                             #得到最好特征对应的不同属性值集合
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)  #使用划分后的数据子集 和 剩下的特征列表  递归构建字典
    return myTree


def creatDataSet():
    dataSet = [[1, 1, 'maybe'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

myData, labels = creatDataSet()
print("数据集：{}\n 标签：{}".format(myData, labels))
print("该数据集下的香农熵为:{}".format(calcShannonEnt(myData)))
myData[0][-1] = 'yes'
print("数据为:{}\n 该数据集下的香农熵为:{}".format(myData, calcShannonEnt(myData)))

print("划分前的数据集：{}\n \n按照“离开水是否能生存”为划分属性，得到下一层待划分的结果为:\n{}--------{}".format(
    myData, splitDataSet(myData, 0, 0), splitDataSet(myData, 0, 1)))
chooseBestFeatureToSplit(myData)

print("决策树:{}".format(createTree(myData, labels)))

import matplotlib.pyplot as plt
from pylab import*

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def plotNode(nodeTxt, centerPt,parentPt, nodeType):
    mpl.rcParams['font.sans-serif']=['SimHei']
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def createPlot():
    fig = plt.figure(111, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False)
    plotNode(U'Decision Node',  (0.5, 0.1),(0.1, 0.5), decisionNode)
    plotNode(U'Leaf Node', (0.8, 0.1),(0.3, 0.8),  leafNode)
    plt.show()


# treePlotter.py
# 计算叶节点的个数

def getNumLeaves(myTree):
    numLeafs= 0
    # 截取到树字典中的key值
    #firstStr = str(myTree.keys())[13:-3]
    firstStr = eval(str(myTree.keys()).replace('dict_keys(','').replace(')',''))[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeaves(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs
# 计算树的深度


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = eval(str(myTree.keys()).replace('dict_keys(', '').replace(')', ''))[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


#测试深度计算和叶节点记述函数
def retrieveTree(i):
    listOftrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOftrees[i]

mytree =  retrieveTree(1)
print(getNumLeaves(mytree))
print(getTreeDepth(mytree))


# treePlotter.py
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)


def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getTreeDepth(myTree)
    firstStr =  eval(str(myTree.keys()).replace('dict_keys(','').replace(')',''))[0]
    cntrPt = (plotTree.xOff+(1.0 + float(numLeafs))/
              2.0/plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff +1.0/plotTree.totalW
            plotNode(secondDict[key],(plotTree.xOff,plotTree.yOff),cntrPt,leafNode)
            plotMidText((plotTree.xOff,plotTree.yOff),cntrPt,str(key))
    plotTree.yOff = plotTree.yOff +1.0/plotTree.totalD


def createPlot(inTree):
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    axprops = dict(xticks = [],yticks = [])
    createPlot.ax1 = plt.subplot(111,frameon = False,**axprops)
    plotTree.totalW = float(getNumLeaves(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5/plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree,(0.5,1.0),"")
    plt.show()


myTree = retrieveTree(0)
createPlot(myTree)








