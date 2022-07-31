class NumArray:

    def __init__(self, nums: List[int]):
        def build(value, tree_left, tree_right):
            if tree_left == tree_right:
                tree[value] = nums[tree_left]
            else:
                tree_middle = (tree_left + tree_right)//2
                build(2*value, tree_left, tree_middle)
                build(2*value+1, tree_middle+1, tree_right)
                tree[value] = tree[2*value] + tree[2*value+1]
                
        n = len(nums)
        tree = [0]*(4*n)
        build(1, 0, n-1)
        self.n, self.tree = n, tree

    def update(self, index: int, val: int) -> None:
        def real_update(value, tree_left, tree_right, pos, new_val):
            if tree_left == tree_right:
                self.tree[value] = new_val
            else:
                tree_middle = (tree_left + tree_right)//2
                if pos <= tree_middle:
                    real_update(2*value, tree_left, tree_middle, pos, new_val)
                else:
                    real_update(2*value+1, tree_middle+1, tree_right, pos, new_val)
                self.tree[value] = self.tree[2*value] + self.tree[2*value+1]
        real_update(1, 0, self.n-1, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        def real_sum(value, tree_left, tree_right, left, right):
            if left > right:
                return 0
            if tree_left == left and tree_right == right:
                return self.tree[value]
            tree_middle = (tree_left + tree_right)//2
            return (real_sum(2*value, tree_left, tree_middle, left, min(right, tree_middle)) + 
                   real_sum(2*value+1, tree_middle+1, tree_right, max(left, tree_middle+1), right))
        return real_sum(1, 0, self.n - 1, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)