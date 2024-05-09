# -*- encoding: utf-8 -*-

"""
题目：88. 合并两个有序数组
地址：https://leetcode.cn/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
"""


def merge_stored_array(nums_1: list, nums_2: list, m: int, n: int):
    if n <= 0:
        return
    if m <= 0:
        nums_1.pop()
        nums_1 += nums2
        print(f'nums_1 is {nums_1}')
        return


    nums_1_index = nums_2_index = 0
    # for i in range(m):
    #     if nums_1[i]>=nums_2[0]:
    #         nums_1_index=i
    #         break
    # nums_1.insert(nums_1_index+1, nums_2[0])
    # for j in range(1,n):

    while nums_1_index < m+n or nums_2_index < n:
        if nums_2[nums_2_index] >= nums_1[nums_1_index]:
            # 再加个while继续对比后面的
            nums_1.insert(nums_1_index+1, nums_2[nums_2_index])
            print(f'nums_1 排序中间过程值：{nums_1}')
            nums_1_index += 2
            nums_2_index += 1
            nums_1.pop()

        else:
            nums_1_index += 1

    print('hhhh')


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    merge_stored_array(
        nums_1=nums1,
        nums_2=nums2,
        m=3,
        n=3
    )

    # nums1 = [0]
    # nums2 = [1]
    # merge_stored_array(
    #     nums_1=nums1,
    #     nums_2=nums2,
    #     m=0,
    #     n=1
    # )

    print(f'nums1 is {nums1}')
