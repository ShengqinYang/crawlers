class myclass():
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_key(self):
        hash_ = dict(zip(self.nums, range(len(self.nums))))
        for i in range(len(self.nums)):
            cha = self.target - self.nums[i]
            if hash_.get(cha):
                print(self.nums[i], hash_.get(cha))
                return self.nums[i], hash_.get(cha)


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9


    # te = myclass(nums, target).find_key()
    # print(te)
    def n():
        hash_ = dict(zip(nums, range(len(nums))))
        print(hash_)
        for i in range(len(nums)):
            cha_va = target - nums[i]
            if hash_.get(cha_va) and i != hash_.get(cha_va):
                return (i, hash_.get(cha_va))
    print(n())
