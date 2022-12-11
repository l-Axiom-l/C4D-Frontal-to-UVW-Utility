import c4d

def main():
    #Gets all Objects with ax_ in the Name
    things = doc.GetObjects()
    importantThings = list(filter(lambda x: "ax_" in x.GetName(), things))
    for obj in importantThings:
        doUVWThing(obj)
    #obj = doc.SearchObject("Kugel")
    
    #Debug Things
    print(importantThings)

#Does the Process of Changing the Projection and UVW Tag    
def doUVWThing(obj):
    #Gets the Texture Tag
    tag = obj.GetTag(c4d.Ttexture,nr=0)
    #Changes the Texture Projection Mode to Frontal
    tag[c4d.TEXTURETAG_PROJECTION] = 4
    #Removes the old UVW Tag
    obj.KillTag(c4d.Tuvw,nr=0)
    #Generates a new UWV Tag
    uvw = c4d.utils.GenerateUVW(obj, obj.GetMg(), tag, obj.GetMg(), doc.GetRenderBaseDraw())
    #Adds the new UVW Tag to the Object
    obj.InsertTag(uvw, pred=tag)
    #Changes Projection to UWW
    tag[c4d.TEXTURETAG_PROJECTION] = 6
    
    #Debug Things
    print(uvw)
    print(tag[c4d.TEXTURETAG_PROJECTION])
