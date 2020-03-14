list_colors = [ "black","brown","red","orange","yellow","green","blue","violet","grey","white"]
def value(colors):
    return int(str(list_colors.index(colors[0]))+str(list_colors.index(colors[1])))
