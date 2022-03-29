from Objects import Point


def importer(path):
    with open(path, "r") as f:
        imported_points = f.readlines()
    points = []
    for line in imported_points:
        if len(line) < 3:
            continue
        else:
            line = line.replace("\t", " ")
            line = line.rstrip()
            line = line.lstrip()
            line = line.replace(",", ".")
            while line.find("  ") != -1:
                line = line.replace("  ", " ")
            points.append(line.split(" "))
    for point in points:
        if len(point) == 3:
            point.append("0.00")
    return points


def entities_generator(points, with_z, p_l, t_l, t_h):
    generated = ""
    if with_z:
        for point in points:
            generated += str(point.generate_with_z(p_l, t_l, t_h))
    else:
        for point in points:
            generated += str(point.generate_without_z(p_l, t_l, t_h))
    return generated


def filer(path, path_out):
    points_list = []
    for point in importer(path):
        points_list.append(Point(point))
    with_z_ask = True
    points_layer = "0_pomiar"
    text_layer = "0_pomiar_pikiety"
    text_height = "0.2"
    header = "0\nSECTION\n2\nHEADER\n0\nENDSEC\n"
    tables = "0\nSECTION\n2\nTABLES\n0\nTABLE\n2\nLAYER\n70\n0\n0\nLAYER\n2\n0\n70\n0\n62\n7\n6\nCONTINUOUS\n0\n" \
             "ENDTAB\n0\nENDSEC\n"
    layer_obj = "0\nLAYER\n2\n" + str(points_layer) + "\n70\n0\n62\n7\n6\nCONTINUOUS\n0\nENDTAB\n0\nENDSEC\n"
    layer_text = "0\nLAYER\n2\n" + str(text_layer) + "\n70\n0\n62\n7\n6\nCONTINUOUS\n0\nENDTAB\n0\nENDSEC\n"
    entities = "0\nSECTION\n2\nENTITIES\n"+entities_generator(points_list, with_z_ask, points_layer, text_layer,
                                                              text_height)+"0\nENDSEC\n"
    eof = "0\nEOF"
    out = header+tables+layer_obj+layer_text+entities+eof
    print(out)
    with open(path_out, "w") as f:
        f.write(out)
