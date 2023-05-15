gml_file_path = r"Z:\$$01_Winkalk\@Winkalk 2023\088_2023 Dostawcza\ZŁOG\ZDT.ZOPG.4134.2374.2023_9_1_1.gml"

try:
    gml = open(gml_file_path, "rt", encoding="utf-8")


    class Plot:
        def __init__(self):
            self.id = ""
            self.name_space = ""
            self.version = ""
            self.__plot_id = ""
            self.__plot_number = ""
            self.KW = ""
            self.border_points_ref = []

        @property
        def plot_id(self):
            return self.__plot_id

        @plot_id.setter
        def plot_id(self, ident):
            self.__plot_id = str(ident)
            self.__plot_number = ident.split(".")[2]

        @property
        def plot_number(self):
            return self.__plot_number

        @plot_number.setter
        def plot_number(self, number):
            self.__plot_number = str(number)
            plot_id = self.__plot_id.split(".")
            plot_id[2] = str(number)
            self.__plot_id = ".".join(plot_id)

        def __str__(self):
            return str(self.id)

        @staticmethod
        def hello():
            print("hello")


    class DbEGB:
        @staticmethod
        def __get_value_from_line(line_str):
            return line_str[line_str.find(">")+1:line_str.find("<", 1)]

        def __init__(self, gml_stream):
            self.db = {"plots": {}}
            while line := gml_stream.readline():
                if line == "<gml:featureMember>\n":
                    self.__object_identifier(gml_stream)

        def __object_identifier(self, gml_stream):
            while line := gml_stream.readline():
                if line.startswith("<egb:EGB_DzialkaEwidencyjna"):
                    self.__plot_object_builder(gml_stream)

        def __plot_object_builder(self, gml_stream):
            plot = Plot()

            while line := gml_stream.readline():
                if line.startswith("<bt:lokalnyId>"):
                    plot.id = self.__get_value_from_line(line)
                elif line.startswith("<bt:przestrzenNazw>"):
                    plot.name_space = self.__get_value_from_line(line)
                elif line.startswith("<bt:wersjaId>"):
                    plot.version = self.__get_value_from_line(line)
                elif line.startswith("<egb:idDzialki>"):
                    plot.plot_id = self.__get_value_from_line(line)
                elif line.startswith("<egb:numerElektronicznejKW>"):
                    plot.KW = self.__get_value_from_line(line)
#                elif line.startswith("<egb:punktGranicyDzialki"):
#                    while line.startswith("<egb:punktGranicyDzialki"):
#                        line = line.strip().replace("<egb:punktGranicyDzialki xlink:href=\"urn:pzgik:id:")




                elif line == "</egb:EGB_DzialkaEwidencyjna>\n":
                    break
            self.db["plots"].update({f"{plot.plot_id}": plot})









    reader = DbEGB(gml)

#    for r in reader.db["plots"]:
#        print(reader.db["plots"][r])
finally:
    gml.close()

