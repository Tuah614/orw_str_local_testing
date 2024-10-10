from Autodesk.Revit.DB import *

LEVELCOUNTS = 4
layers_per_level  = [3 , 3 , 3 , 4]
panel_marks = ["021", "022", "023", "024", "025", "026", "027", "028", "029", "030"]
panel_lengths = [50, 50, 50, 50, 50, 35, 50, 50, 50, 50]
panel_types = ["B1","B1", "C1", "C1", "C1", "C1", "B1", "B1", "B1", "B1"]

print(len(panel_marks), len(panel_lengths), len(panel_types))

lp_points = []
original_point = XYZ(0, 0, 0)
X_distance = 0
Y_distance = 0
for m, mark, length in zip(range(len(panel_marks), panel_marks, panel_lengths)):
    if m == 0:
        lp_X = original_point.X
    else:
        X_distance = X_distance + length
        lp_X = original_point.X + X_distance
    lp_header_point = XYZ(lp_X, original_point.Y, original_point.Z)

    lp_columns = []
    for i, j in zip(range(LEVELCOUNTS), layers_per_level):
        if i == 0:
            lp_columns.append(lp_header_point)
        else:
            Y_multiplier = layers_per_level[i - 1]
            Y_distance = Y_distance + (6 * Y_multiplier)
            new_point = XYZ(lp_header_point.X,
                            lp_header_point.Y - Y_distance,
                            lp_header_point.Z)
            lp_columns.append(new_point)
