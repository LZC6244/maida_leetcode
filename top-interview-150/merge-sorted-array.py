# -*- encoding: utf-8 -*-
from typing import List

"""
题目：88. 合并两个有序数组
地址：https://leetcode.cn/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution(object):
    @staticmethod
    def merge(nums_1: List[int], m: int, nums_2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        思路：使用双指针、利用两个列表已排序特点
        """
        print(
            f'*' * 50 + \
            f'\n传入： nums_1 = {nums_1}\tm = {m}' + \
            f'\n传入： nums_2 = {nums_2}\tn = {n}\n' + \
            f'*' * 50,
        )

        nums_1_index = nums_2_index = 0
        tmp_list = list()
        while nums_1_index < m or nums_2_index < n:
            if nums_1_index == m:
                tmp_list.append(nums_2[nums_2_index])
                nums_2_index += 1
            elif nums_2_index == n:
                tmp_list.append(nums_1[nums_1_index])
                nums_1_index += 1
            elif nums_1[nums_1_index] > nums_2[nums_2_index]:
                tmp_list.append(nums_2[nums_2_index])
                nums_2_index += 1
            else:
                tmp_list.append(nums_1[nums_1_index])
                nums_1_index += 1

        nums_1[:] = tmp_list
        print('排序结束')
        print(
            f'*' * 50 + \
            f'\nnums_1 最终为 {nums_1}\n' + \
            f'*' * 50,
        )


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(
        nums_1=nums1,
        nums_2=nums2,
        m=3,
        n=3
    )

    nums1 = [1]
    nums2 = []
    Solution().merge(
        nums_1=nums1,
        nums_2=nums2,
        m=1,
        n=0
    )

    nums1 = [0]
    nums2 = [1]
    Solution().merge(
        nums_1=nums1,
        nums_2=nums2,
        m=0,
        n=1
    )

    # nums1 = [1, 0]
    # nums2 = [2]
    # Solution().merge(
    #     nums_1=nums1,
    #     nums_2=nums2,
    #     m=1,
    #     n=1
    # )
    #
    # nums1 = [2, 0]
    # nums2 = [1]
    # Solution().merge(
    #     nums_1=nums1,
    #     nums_2=nums2,
    #     m=1,
    #     n=1
    # )
