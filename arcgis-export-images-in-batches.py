import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

mxd = arcpy.mapping.MapDocument("CURRENT")
for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    dirName = mxd.dataDrivenPages.pageRow.getValue(mxd.dataDrivenPages.pageNameField.name)

    file_path = r"D:/1/" + str(dirName)
    isExists = os.path.exists(file_path)
    if not isExists:
        os.makedirs(file_path)
		
	image_path = file_path + "/影像图.jpg"
	arcpy.mapping.ExportToJPEG(mxd, image_path, resolution = 300)
del mxd