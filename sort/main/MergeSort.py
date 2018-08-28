# coding: utf-8
class MergeSort(object):

    def __init__(self, list):
        self.list = list
        self.len = len(self.list)


    def mergeAsc(self, first, second):
        '''
        合并两个有序序列为一个有序序列（升序）
        1、从两个序列的第1个数开始比较，谁小谁放在merge_list中，一直循环比较
        2、若有序列还有数存在，则这个序列的剩余数直接插到merge_list后
        :param first:  第1个序列
        :param second: 第2个序列
        :return:
        '''
        merge_list = []
        first_len = len(first)
        second_len = len(second)
        i = 0
        j = 0
        while(i < first_len and j < second_len):
            if first[i] < second[j]:
                merge_list.append(first[i])
                i = i + 1
            else:
                merge_list.append(second[j])
                j = j + 1

        while(i < first_len):
            merge_list.append(first[i])
            i = i + 1

        while(j < second_len):
            merge_list.append(second[j])
            j = j + 1

        return merge_list


    def mergeDesc(self, first, second):
        merge_list = []
        first_len = len(first)
        second_len = len(second)
        i = 0
        j = 0
        while(i < first_len and j < second_len):
            if first[i] > second[j]:
                merge_list.append(first[i])
                i = i + 1
            else:
                merge_list.append(second[j])
                j = j + 1
        while(i < first_len):
            merge_list.append(first[i])
            i = i + 1

        while(j < second_len):
            merge_list.append(second[j])
            j = j + 1

        return merge_list

    def sort(self, list):
        if len(list) <= 1:
            return list
        mid = len(list)//2
        left = self.sort(list[:mid])
        right = self.sort(list[mid:])
        return self.mergeAsc(left, right)
        # return self.mergeDesc(left, right)


if __name__ == "__main__":
    list = [50, 10, 90, 30, 70, 40, 80, 60, 20]
    list = [10, 7, 5, 3, 2, 1, 4, 6, 8, 9]
    merge = MergeSort(list)
    merge_list = merge.sort(merge.list)
    print(merge_list)
