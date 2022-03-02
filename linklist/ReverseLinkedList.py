# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, elem):
        self.elem = elem  # 保存数据
        self.next = None  # 没有确定下一个的时候，先设为空
#定义好了Node类，就可以根据Node类创建出Node的实例，创建实例是通过类名+()实现的：
#node =Node(100)
# 可以看到，变量node指向的就是一个Node的实例,每个object的地址都不一样，而Node本身则是一个类。
# 可以自由地给一个实例变量绑定属性，比如，给实例node绑定一个pre属性
# node.pre = 3

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去

# (object)，表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
# 注意：特殊方法“__init__”前后分别有两个下划线！！

#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：
'''
def __init__(self, elem):
        # self.elem = elem  # 把elem属性绑定到未来要创建的实例上，以后创建实例必须传elem
        self.next = None  # 没有确定下一个的时候，先设为空
    pass
''' 


class SingleLinkList(object):
    def __init__(self, node):
        self.head = node

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def appendList(self, lis):
        for data in lis:
            new_node = Node(data)
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = new_node

    def travel(self):
        # 换行的方法
        # cur游标，用来一定遍历节点
        # count记录数量
        # 默认值为零，比较好计算
        count = 0
        # cur游标，用来移动遍历节点
        cur = self.head
        while cur != None:
            print(cur.elem, '->', end='')
            count += 1
            cur = cur.next  # 每次移一位，
        print("None")
        return count

    @staticmethod
    def reverseList(lList):
        head = lList.head
        prev, curr = None,head
        while curr:
            # 要先存一下 curr.next的值，存成一个临时变量，然后就可以给curr.next重新赋值了
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        lList.head = prev
        return lList
    
    @staticmethod
    def reverseListByNode(head):
        prev, curr = None,head
        #原始 prev = None, curr = head = 4，cur.next = 5，第一轮，cur = 5 
        while curr:
            nxt = curr.next#原始nxt = 等于5，第一轮变6
            curr.next = prev#原始 curr.next = 5,第一轮curr.next = null
            prev = curr #prev原始等于null,第一轮等于4
            curr = nxt#curr,原始等于4，第一轮等于5
        return prev


if __name__ == '__main__':
    nd = Node(4)
    linkedList = SingleLinkList(nd)
    linkedList.append(5)
    linkedList.append(6)
    linkedList.append(7)
    #linkedList.appendList([8,9,10])
    #linkedList.travel()
   # reversedList = SingleLinkList.reverseList(linkedList)
   # reversedList.travel()
    # test reverseListByNode
    firstNode = SingleLinkList.reverseListByNode(linkedList.head)
    p = firstNode
    while p != None:
        print(p.elem)
        p = p.next
