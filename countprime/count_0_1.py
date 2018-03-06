from collections import OrderedDict


class prime_count():
    def __init__(self):
        self.prime_dict = OrderedDict()
        with open('../primetxt/prime_number_in_binary_notation.txt', 'r') as f:
            for row in f:
                self.prime_dict[int(row.strip(), 2)] = list(row.strip()) 

    def count_01(self, p_dict):
        zero_counter = 0
        one_counter = 0
        is_one = 0
        
        for val in p_dict.values():
            for num in val:
                if int(num) == 0 and is_one == 1:
                    zero_counter += 1

                else:
                    is_one = 1
                    one_counter += 1

        one_counter = one_counter - len(p_dict)
        return [zero_counter, one_counter]


if __name__ == "__main__":
    prime = prime_count()
    d = prime.prime_dict
    res = prime.count_01(d)
    print("0 ... " + str(res[0]) + "\t 1 ... " + str(res[1]))
