class Node(object):
    def __init__(self, elem):
        self.elem = elem  # 保存数据
        self.next = None  # 没有确定下一个的时候，先设为空
    pass
#node =Node(100)


class SingleLinkList(object):
    # 单链表类的具体对象的操作
    # 对象方法，不是类方法，需要构造
    # private Node _head
    def __init__(self, node):
        self._head = node  # 头节点信息，是单链表SingleLinkList(object)所维护的，
        # 调用的人关注方法就可以，不需要知道头节点的具体信息
        # 内在的函数去使用，私有属性

    # 链表是否为空

    def is_empty(self):
        return self._head == None

    def length(self):
        pass
        # 遍历整个链表

    def travel(self):
        # 换行的方法
        # cur游标，用来一定遍历节点
        # count记录数量
        # 默认值为零，比较好计算
        count = 0
        # cur游标，用来移动遍历节点
        cur = self._head
        while cur != None:
            print(cur.elem, '->', end='')
            count += 1
            cur = cur.next  # 每次移一位，
        print("None")
        return count
    # 在链表头部添加元素

    def add(self, item):
        node = Node(item)
        node.next = self._head  # 先指向head,这样可以保留原来的元素
        self._head = node

    # 在链表尾部添加元素
        pass

    def append(self, data):
        new_node = Node(data)
        cur = self._head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    # 在指定节点添加

    def insert(self, pos, item):
        pass
     # 删除节点,remove删除具体的元素

    def remove(self, item):
        pass

     # 查找节点是否存在
    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False

    @staticmethod
    def reverse(sList):
        #每次确定的时候用头节点就行了，确认的时候用两个==
        if sList._head == None:
            return sList
        # dummy.next始终指向头节点
        dummy = Node(-1)
        # p = dummy.next,p是作为原来的头节点
        p = sList._head
        # q原本在p后面，后成为换完之后的头节点
        q = p.next
        dummy.next = sList._head
        #初始设置是dummy -> p -> q -> null
        while q != None:
            #p.next 本来是指向q, 现在脱钩，指向q的下一个，往后移了一个
            p.next = q.next
            # q.next的箭头指向头节点，q=3, q.next是4，dummy.next= 2
            #换完之后q.next是2
            q.next = dummy.next#
            #q的值是换完后的头节点,赋值给头节点
            #q是3，q.next是2，让头节点指向q
            dummy.next = q
#           换之前，p= 2,p.next =4,q=3
            q = p.next
        # 返回list前需要把 head指出来
        sList._head = dummy.next
        return sList
        
        #总结：记得linklist只能识别头节点，三个数，dummy -> p -> q ，先动p后面的链接，一步步往后挪，后两步，让q的值给头节点，p在q前面


# test method
nd = Node(3)
linkedList = SingleLinkList(nd)
linkedList.append(4)
linkedList.append(5)
linkedList.add(2)
linkedList.travel()
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据
reversedList = SingleLinkList.reverse(linkedList)
reversedList.travel()
# print linked list
# p = reversedList._head
# while p != None:
#     print(p.elem, '->', end='')
#     p = p.next

