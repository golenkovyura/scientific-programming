class list_divider(list):
    def __truediv__(self, k):
        ans = []
        if type(k) is not int:
            raise TypeError()
        elif k <= 0:
            raise ValueError()
        else:
            start = 0
            end = 1
            c = 0
            v = 1
            y = 0
            u = 1
            for _ in range(k):
                ans.append([])
            if len(self) % k == 0:
                for i in ans:
                    i.extend(self[start * (len(self) // k):(len(self) // k) * end])
                    start += 1
                    end += 1
            else:
                ost = len(self) % k
                s = 0
                for i in ans:
                    if ost != 0:
                        i.extend(self[c * (len(self) // k + 1):(len(self) // k + 1) * v])
                        c += 1
                        v += 1
                        ost -= 1
                    s += len(i)
                    if len(i) == 0:
                        i.extend(self[s + y * (len(self) // k):s + u * (len(self) // k)])
                        y += 1
                        u += 1
            return ans
