import utils
from utils import rf
from threading import Thread


# 非決定性関数のエントリポイント関数
def nd_contains_main():

    testVals = [(rf('geneticString.txt'), 'yes'),
                ('T' * 100000, 'no'),
                ]
    for (inString, solution) in testVals:
        val = nd_contains_nana(inString)
        prefix = inString[:20]
        utils.tprint(prefix + '...', ':', val)
        assert val == solution


# 与えられた入力の中で４種類の異なる文字列を並列に探索する関数
def nd_contains_nana(in_string):

    # 探索する文字列
    strings = ['CACA', 'GAGA', 'TATA', 'AAAA']

    # スレッド格納変数(空リスト)
    threads = []

    # 他のスレッドで非決定的に計算された解を格納する
    nd_soln = utils.NonDetSolution()

    # 非決定計算を実行するスレッドを作成する
    for s in strings:

        # 起動時にfindString(s,inString,ndSoln)を実行するスレッドを作成する
        t = Thread(target=find_string, args=(s, in_string, nd_soln))

        # スレッドリストに新しく作成されたスレッドを追加する
        threads.append(t)

    solution = utils.waitForOnePosOrAllNeg(threads, nd_soln)

    return solution


def find_string(string,text, nd_soln):

    if string in text:
        nd_soln.setSolution('yes')


