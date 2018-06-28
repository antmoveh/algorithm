"""
https://github.com/fxsjy/jieba
"""
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Model: " + "/".join(seg_list))  # 全模式
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Model: " + "/".join(seg_list))  # 精确模式
seg_list = jieba.cut("他来到了网易杭研大厦")
print(",".join(seg_list))  # 默认精确
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print(",".join(seg_list))  # 索引模式

"""
结巴分词配合多路查找树，可实现对用户输入内容进行敏感词过滤
实现及演示效果如下所示
"""

from typing import Dict, List
from collections import abc
import re

pattern = re.compile(
    r'([\`\~\!\@\#\$\%\^\&\*\(\)\+\=\|\{\}\'\:\;\'\,\.\<\>\/\?\~\！\@\#\￥\%\…\…\&\*\（\）\—\—\+\|\{\}\【\】\‘\；\：\”\“\’\。\，\、\？\ ])')


class MulSearchTree:

    def __init__(self):
        """根节点"""
        self.root = dict()

    """可迭代对象"""
    def build(self, items: List[str]):
        for item in items:
            self.add(item)

    """字符串 可迭代"""
    def add(self, item: str):
        node = self.root
        length = len(item)-1
        for i in range(len(item)):
            if item[i] not in node:
                node[item[i]] = (dict(), not bool(length-i))
            else:
                Next, flag = node[item[i]]
                node[item[i]] = (Next, not bool(length-i))
            node = node[item[i]][0]

    # 判断是否敏感词
    def judge_word(self, word: str):
        node = self.root
        for w in word:
            if w in node:
                if node[w][1]:
                    return True
                else:
                    node = node[w][0]
            else:
                return False
        return False

    # 判断单词列表
    def judge_list(self, words: List):
        resp = []
        for word in words:
            resp.append(self.judge_word(word))
        return resp

    # 另一种构建方法
    def build_method(self, items: List[str]):
        for item in items:
            self._add_method(self.root, item)

    # 递归方式，只能内部使用
    def _add_method(self, node: Dict, item: str):
        length = len(item)-1
        if length == -1:
            return
        if item[0] not in node:
            node[item[0]] = (dict(), not bool(length-1))
        else:
            Next, flag = node[item[0]]
            node[item[0]] = (Next, not bool(length - 1))
        node = node[item[0]][0]
        self._add_method(node, item[1:])

    def __iter__(self):
        return self._iter(self.root)

    def _iter(self, node: Dict):
        if len(node) == 0:
            return
        for k, v in node.items():
            yield k, v
            # if isinstance(v[0], abc.Mapping):
            #     self._iter(v[0])


if __name__ == "__main__":
    mst = MulSearchTree()
    words = ["的设", "计具有", "很强的可读性", "相比其他", "语言经常使用", "英文关", "键字", "其他", "语言",
             "的一些标点符号", "它具有比", "其他语言", "单"]
    # 构建或检查之前先使用正则表达式过滤特殊字符
    words = [re.sub(pattern, "", word) for word in words]
    # 两种构建方法，效果相同
    mst.build(words)
    # mst.build_method(words)

    one = mst.judge_word("哈哈")
    print(one)
    two = mst.judge_word("语言")
    print(two)
    three = mst.judge_list(["哈哈", "语言"])
    print(three)
    mst.add("哼哼哈嘿")
    for m in mst:
        print(m)