import csv


class ListKros:
    __headers = []
    __contents = []

    def __init__(self, dir, filename):
        self.__dir = dir
        self.__filename = filename

    def cria_list(self):
        file = open(self.__dir + '/' + self.__filename + '.csv', 'r')

        handle = csv.reader(file)

        for row in handle:
            if handle.line_num == 1:
                self.__headers = list(row)
            else:
                dictio = {}
                i = 0
                for header in self.__headers:
                    dictio[header] = row[i]
                    i += 1
                dictio['nome_class'] = dictio['nome'].replace(" ", "_")
                self.__contents.append(dictio)
        file.close()

    @property
    def headers(self):
        return self.__headers

    @property
    def contents(self):
        return self.__contents


if __name__ == '__main__':
    lista = ListKros('arquivos', 'krosmaster')
    lista.cria_list()
