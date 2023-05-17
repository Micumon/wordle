gml_file_path = r"Z:\$$01_Winkalk\@Winkalk 2023\088_2023 Dostawcza\ZŁOG\ZDT.ZOPG.4134.2374.2023_9_1_1.gml"


class Plot:
    def __init__(self):
        self.id = ""
        self.name_space = ""
        self.version = ""
        self.__plot_id = ""
        self.__plot_number = ""
        self.KW = ""
        self.border_points_ref = []
        self.precinct_ref = ""

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


class BorderPoint:
    def __init__(self):
        self.id = ""
        self.name_space = ""
        self.version = ""
        self.x = float()
        self.y = float()
        self.__point_id = ""
        self.__point_number = ""
        self.source_number = ""
        self.zrd = ""
        self.pos_error = ""
        self.stb = ""
        self.rzg = ""


    @property
    def point_id(self):
        return self.__point_id

    @point_id.setter
    def point_id(self, ident):
        self.__point_id = str(ident)
        self.__point_number = ident.split(".")[2]

    @property
    def point_number(self):
        return self.__point_number

    @point_number.setter
    def point_number(self, number):
        self.__point_number = str(number)
        point_id = self.__point_id.split(".")
        point_id[2] = str(number)
        self.__point_id = ".".join(point_id)


class PlotPointRef:
    def __init__(self, plot_id="", point_id=""):
        self.plot_id = plot_id
        self.point_id = point_id
        self.__i = 1

    @property
    def id(self):
        return self.plot_id + "_" + self.point_id

    def __getitem__(self, item):
        if item == "plot":
            return self.plot_id
        elif item == "border_point":
            return self.point_id
        else:
            raise KeyError

    def __next__(self):
        if self.__i == 1:
            self.__i += 1
            return self["plot"]
        elif self.__i == 2:
            self.__i += 1
            return self["border_point"]
        else:
            self.__i = 1
            raise StopIteration

    def __iter__(self):
        return self


class DataBase:
    @staticmethod
    def __get_value_from_line(line_str):
        return line_str[line_str.find(">")+1:line_str.find("<", 1)]

    @staticmethod
    def __xlink_parser(line_str, obj):
        return line_str[line_str.find(obj.name_space + ":") + len(obj.name_space) + 1:line_str.find('"/>')]

    def __init__(self):
        self.egib = {"plots": {},
                     "border_points": {},
                     "plot_point_ref": {}}
        self.bdot500 = {}
        self.gesut = {}

    def importer(self, gml_path):
        gml_stream = ""
        try:
            gml_stream = open(gml_path, "rt", encoding="utf-8")
            while line := gml_stream.readline():
                if line == "<gml:featureMember>\n":
                    self.__object_identifier(gml_stream)
        except:
            gml_stream.close()

    def __object_identifier(self, gml_stream):
        while line := gml_stream.readline():
            if line.startswith("<egb:EGB_DzialkaEwidencyjna"):
                self.__plot_object_builder(gml_stream)
            if line.startswith(("<egb:EGB_PunktGraniczny")):
                self.__border_point_object_builder(gml_stream)

    def __ident_number(self, obj, gml_stream):
        while line := gml_stream.readline():
            if line.startswith("<bt:lokalnyId>"):
                obj.id = self.__get_value_from_line(line)
            elif line.startswith("<bt:przestrzenNazw>"):
                obj.name_space = self.__get_value_from_line(line)
            elif line.startswith("<bt:wersjaId>"):
                obj.version = self.__get_value_from_line(line)
            elif line.startswith("</bt:BT_Identyfikator>"):
                break
        return obj

    def __plot_object_builder(self, gml_stream):
        plot = Plot()
        while line := gml_stream.readline():
            if line.startswith("<egb:idIIP>"):
                plot = self.__ident_number(plot, gml_stream)
            elif line.startswith("<egb:idDzialki>"):
                plot.plot_id = self.__get_value_from_line(line)
            elif line.startswith("<egb:numerElektronicznejKW>"):
                plot.KW = self.__get_value_from_line(line)
            elif line.startswith("<egb:punktGranicyDzialki"):
                line = self.__xlink_parser(line, plot)
                reference = PlotPointRef(plot.id, line)
                self.egib["plot_point_ref"].update({reference.id: reference})
            elif line == "</egb:EGB_DzialkaEwidencyjna>\n":
                break
        self.egib["plots"].update({f"{plot.id}": plot})

    def __border_point_object_builder(self, gml_stream):
        border_point = BorderPoint()
        while line := gml_stream.readline():
            if line.startswith("<egb:idIIP>"):
                border_point = self.__ident_number(border_point, gml_stream)
            elif line.startswith("<gml:pos"):
                border_point.x = self.__get_value_from_line(line).split(" ")[0]
                border_point.y = self.__get_value_from_line(line).split(" ")[1]
            elif line.startswith("<egb:idPunktu"):
                border_point.point_id = self.__get_value_from_line(line)
            elif line.startswith("<egb:oznWMaterialeZrodlowym"):
                border_point.source_number = self.__get_value_from_line(line)
            elif line.startswith("<egb:zrodloDanychZRD"):
                border_point.zrd = self.__get_value_from_line(line)
            elif line.startswith("<egb:bladPolozeniaWzgledemOsnowy"):
                border_point.pos_error = self.__get_value_from_line(line)
            elif line.startswith("<egb:kodStabilizacji"):
                border_point.stb = self.__get_value_from_line(line)
            elif line.startswith("<egb:kodRzeduGranicy"):
                border_point.rzg = self.__get_value_from_line(line)
            elif line == "</egb:EGB_PunktGraniczny>\n":
                break
        self.egib["border_points"].update({f"{border_point.id}": border_point})


#reader = DataBase()
#reader.importer(gml_file_path)

#print(reader.egib["border_points"][list(reader.egib["border_points"].keys())[2]].y)
#for r in reader.egib["plots"]:
#    print(reader.egib["plots"][r].plot_id)
#for r in reader.egib["plot_point_ref"]:
#    print()
#for r in reader.egib["border_points"]:
#    print(r)
#def xlink_parser(line_str, obj):
#    return line_str[line_str.find(obj.name_space + ":") + len(obj.name_space) + 1:line_str.find('"/>')]
#a = Plot()
#a.name_space = "PL.PZGiK.197.EGiB"
#b = r'<egb:punktGranicyDzialki xlink:href="urn:pzgik:id:PL.PZGiK.197.EGiB:F445756E-565C-4DA4-A436-6746663C0061"/>'
#print(xlink_parser(b,a))
#def get_value_from_line(line_str):
#    return line_str[line_str.find(">") + 1:line_str.find("<", 1)]


