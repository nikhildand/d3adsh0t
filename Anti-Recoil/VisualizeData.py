import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import statistics
import ast
import math

def ParseRawData(ConfigFile):

    Count = 1
    BulletsData = {1 : [], 2 : []}
    File = open(ConfigFile, 'r')
    Lines = File.read().split('\n')
    for Line in Lines:
        if Line != '':
            ParsedLine = ast.literal_eval(Line)
            BulletsData[Count].append(ConvertPlotType(RelativeMouseMovement(ParsedLine)))
        else:
            Count += 1

    return BulletsData

def RelativeMouseMovement(Set):

    RelativeSet = []
    for i in range(len(Set) - 1):
        X = Set[i + 1][0] - Set[i][0]
        Y = Set[i + 1][1] - Set[i][1]
        RelativeSet.append((X, Y))

    return RelativeSet

def ConvertPlotType(RelativeSet):
    X = [val[0] for val in RelativeSet]
    Y = [val[1] for val in RelativeSet]
    PlotData = [X, Y]
    return PlotData

def ScatterXVariation(Data):

    ModifData = {2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : [], 10 : []}
    ConstantY = [0] * 20
    for Bullet in range(2, 11):
        for val in Data:
            ModifData[Bullet].append(val[0][Bullet - 2])

    '''
    _MeanX = MeanMovement(ModifData)

    plt.figure(figsize = [10, 8])
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.scatter(ModifData[i + 2], ConstantY)
        plt.plot([_MeanX[i], _MeanX[i]], [-0.04, 0.04], color = 'purple')
        plt.title('Bullet : {} - {}'.format(i + 1, i + 2), fontsize = 8)
        plt.yticks([])
    '''

    return ModifData

def ScatterYVariation(Data):

    ModifData = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}
    ConstantX = [0] * 20
    for Bullet in range(2, 11):
        for val in Data:
            ModifData[Bullet].append(val[1][Bullet - 2])

    '''
    _MeanY = MeanMovement(ModifData)

    plt.figure(figsize=[8, 10])
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.scatter(ConstantX, ModifData[i + 2])
        plt.plot([-0.05, 0.05], [_MeanY[i], _MeanY[i]], color = 'purple')
        plt.title('Bullet : {} - {}'.format(i + 1, i + 2), fontsize=8)
        plt.xticks([])
    '''

    return ModifData

def MeanMovement(BulletData):

    MeanMouseMovement = []
    for Bullet in range(2, 11):
        MeanMouseMovement.append(statistics.mean(BulletData[Bullet]))

    return MeanMouseMovement

MeanX = []
MeanY = []
MoveXDirec = []
MoveYDirec = []
ParsedData = ParseRawData('Vandal.txt')
for i in range(2):
    MeanX.append(MeanMovement(ScatterXVariation(ParsedData[i + 1])))
    MeanY.append(MeanMovement(ScatterYVariation(ParsedData[i + 1])))
for i in range(9):
    MoveXDirec.append(math.ceil((MeanX[0][i] + MeanX[1][i]) / 2))
    MoveYDirec.append(math.ceil((MeanY[0][i] + MeanY[1][i]) / 2))
print()
for i in range(9):
    print('(', -1 * MoveXDirec[i], ',', -1 * MoveYDirec[i], ')', end=' ')
print()