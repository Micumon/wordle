class Point:
    def __init__(self, point):
        self.number = "1\n" + str(point[0]) + "\n"
        self.x = "10\n" + str(point[2]) + "\n"
        self.y = "20\n" + str(point[1]) + "\n"
        self.z = "30\n" + str(point[3]) + "\n"

    def generate_with_z(self, p_layer, t_layer, t_h):
        section_str = "0\nPOINT\n8\n" + str(p_layer) + "\n" + self.x + self.y + self.z + "0\nTEXT\n8\n"
        section_str = section_str + str(t_layer) + "\n" + self.x + self.y + self.z + "40\n" + str(t_h) + "\n"
        section_str = section_str + self.number
        return section_str

    def generate_without_z(self, p_layer, t_layer, t_h):
        section_str = "0\nPOINT\n8\n" + str(p_layer) + "\n" + self.x + self.y + "30\n0.000\n" + "0\nTEXT\n8\n"
        section_str = section_str + str(t_layer) + "\n" + self.x + self.y + "30\n0.000\n" + "40\n" + str(t_h) + "\n"
        section_str = section_str + self.number
        return section_str
