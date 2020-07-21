class SparseArray:
    @staticmethod
    def matching_strings(strings, queries):
        res = [0] * 5
        for i in range(len(queries)):
            for j in range(len(strings)):
                if queries[i] == strings[j]:
                    res[i] += 1

        dict = {}
        for i in range(len(queries)):
            dict[queries[i]] = res[i]

        return dict
