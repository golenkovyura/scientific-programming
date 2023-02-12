class score_filter:
    def __init__(self, min_score, max_score): # конструктор класса
        self.min_score = min_score
        self.max_score = max_score
        self.answer = []


    def fit(self, x, y, iterable): # основной метод программы
        for i in range(1, len(x)):
            x[i] += x[i - 1]
        for j in range(1, len(y)):
            y[j] += y[j - 1]
        for k, l in iterable:
            condition = x[k] * y[l] / (x[len(x) - 1] * y[len(y) - 1])
            if self.min_score < condition and self.max_score > condition:
                self.answer.append((k, l))

    def __iter__(self):
        for x in self.answer:
            yield x

    def __len__(self):
        q = len(self.answer)
        return q
