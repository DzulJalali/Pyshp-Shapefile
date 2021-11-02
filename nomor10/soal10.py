import shapefile
w=shapefile.Writer("soal10")
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("ngek","satu")

w.poly([[[1,6],[7,6], [7,9],[1,9], [1,6]]])
w.close()