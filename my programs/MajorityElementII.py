def majorityElement(nums):
    if not nums:
        return []

    # 1st pass: find up to 2 candidates
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # 2nd pass: verify the candidates
    result = []
    if nums.count(candidate1) > len(nums) // 3:
        result.append(candidate1)
    if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:
        result.append(candidate2)

    return result
