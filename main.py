from func_timeout import func_set_timeout

class Solution:
    def find_one_pair(self, stones, diff):
        """
            Question B
            :type stones: List[float]
            :type diff: float
            :rtype: tuple if exist else -1
            time complexity: O(N)
            space complexity: O(N)
        """
        if diff < 0:
            diff *= -1
        weights_dict = {}
        n = len(stones)
        for i in range(n):
            if stones[i] <= 0:
                continue
            if stones[i] not in weights_dict:
                if stones[i] - diff > 0:
                    weights_dict[stones[i] - diff] = i
                weights_dict[stones[i] + diff] = i
            else:
                return weights_dict[stones[i]], i
        return -1

    def find_all_pairs(self, stones, diff):
        """
            Question C
            :type stones: List[float]
            :type diff: float
            :rtype: List[tuple] if exist else -1
            time complexity: O(N)
            space complexity: O(N)
        """
        if diff < 0:
            diff *= -1
        weights_dict = {}
        ans = []
        n = len(stones)
        for i in range(n):
            if stones[i] <= 0:
                continue
            if stones[i] not in weights_dict:
                if stones[i] - diff > 0:
                    weights_dict[stones[i] - diff] = [i]
                weights_dict[stones[i] + diff] = [i]
            else:
                for pair in weights_dict[stones[i]]:
                    ans.append((pair, i))
                if stones[i] - diff > 0:
                    if (stones[i] - diff) not in weights_dict:
                        weights_dict[stones[i] - diff] = [i]
                    else:
                        weights_dict[stones[i] - diff].append(i)
                if (stones[i] - diff) not in weights_dict:
                    weights_dict[stones[i] + diff].append(i)
                else:
                    weights_dict[stones[i] + diff] = [i]
        return ans if ans else -1

    def case1(self, mode):
        '''
        normal case
        :type mode: one or all
        :return: None
        '''
        stones = [1, 3, 4, 9, 17, 25]
        diff = 2
        answer = (0, 1)
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) == answer)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert (sorted(res) == [answer])

    def case2(self, mode):
        '''
        stone pair exist
        :return: None
        '''
        stones = [0.5, 6.54, 20.5987, 1.5679, 0.998, 10.5978, 5.5446, 5.5455]
        diff = 5.0455
        answer = (0, 7)
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) == answer)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert (sorted(res) == [answer])

    def case3(self, mode):
        '''
        stone pair not exist
        :return: None
        '''
        stones = [0.5, 6.54, 20.5987, 1.5679, 0.998, 10.5978, 5.5446, 5.5455]
        diff = 100
        answer = -1
        if mode == "one":
            assert (self.find_one_pair(stones, diff) == answer)
        elif mode == "all":
            assert (self.find_all_pairs(stones, diff) == answer)

    def case4(self, mode):
        '''
        stone pair exist when weight difference is 0
        :return: None
        '''
        stones = [0.5, 6.54, 6.8, 1.5679, 0.998, 10.5978, 6.8, 5.5446, 5.5455]
        diff = 0
        answer = (2, 6)
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) == answer)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert (sorted(res) == [answer])

    def case5(self, mode):
        '''
            stone pair exist when weight difference is 0
            :return: None
        '''
        stones = [0.5, 6.54, 6.8, 1.5679, 0.998, 10.5978, 5.5446, 5.5455]
        diff = 0
        answer = -1
        if mode == "one":
            assert (self.find_one_pair(stones, diff) == answer)
        elif mode == "all":
            assert (self.find_all_pairs(stones, diff) == answer)

    def case6(self, mode):
        '''
        exist more than one possible stone pair
        :return: None
        '''
        stones = [0.5, 1, 6.8, 1.5, 0.998, 10.5978, 2, 5.5455]
        diff = 0.5
        answers = [(0, 1), (1, 3), (3, 6)]
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) in answers)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert len(res) == 3
            assert (tuple(sorted(pair)) in answers for pair in res)

    def case7(self, mode):
        '''
        weight difference is lower than 0
        :return: None
        '''
        stones = [0.5, 1, 6.8, 1.5, 0.998, 10.5978, 2, 5.5455]
        diff = -0.5
        answers = [(0, 1), (1, 3), (3, 6)]
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) in answers)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert len(res) == 3
            assert (tuple(sorted(pair)) == answers for pair in res)

    def case8(self, mode):
        '''
        some stones are not valid
        :return: None
        '''
        stones = [0.5, -1, 6.8, 1.5, -0.998, 10.5978, 2, -5.5455]
        diff = 0.5
        answer = (3, 6)
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) == answer)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert (sorted(res) == [answer])

    @func_set_timeout(3)
    def case9(self, mode):
        '''
        lots of stones but no exist stone pair
        :return: None
        '''
        stones = [i for i in range(1000000)]
        diff = 0
        answer = -1
        if mode == "one":
            assert (self.find_one_pair(stones, diff) == answer)
        elif mode == "all":
            assert (self.find_all_pairs(stones, diff) == answer)

    @func_set_timeout(3)
    def case10(self, mode):
        '''
            lots of stones with exist stone pairs
            :return: None
        '''
        stones = [i for i in range(1000000)]
        diff = 1
        answers = [(i, i + 1) for i in range(1, 1000000 - 1)]
        if mode == "one":
            res = self.find_one_pair(stones, diff)
            assert (tuple(sorted(res)) in answers)
        elif mode == "all":
            res = self.find_all_pairs(stones, diff)
            assert len(res) == 1000000 - 2
            assert (tuple(sorted(pair)) == answers for pair in res)

    def test_one_pair(self):
        '''
        test all one-pair cases
        :return: None
        '''
        self.case1("one")
        self.case2("one")
        self.case3("one")
        self.case4("one")
        self.case5("one")
        self.case6("one")
        self.case7("one")
        self.case8("one")
        self.case9("one")
        self.case10("one")

    def test_all_pairs(self):
        '''
            test all all-pairs cases
            :return: None
        '''
        self.case1("all")
        self.case2("all")
        self.case3("all")
        self.case4("all")
        self.case5("all")
        self.case6("all")
        self.case7("all")
        self.case8("all")
        self.case9("all")
        self.case10("all")

    def test(self):
        '''
            test all cases
            :return: None
        '''
        try:
            self.test_one_pair()
            self.test_all_pairs()
            print("all tests passed!!!")
        except:
            print("Sorry, not all tests passed")


if __name__ == '__main__':
    solution = Solution()
    solution.test()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
