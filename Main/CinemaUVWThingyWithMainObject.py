import c4d

def main():
    #Gets all Objects with ax_ in the Name
    things = doc.GetObjects()
    
    #Get first generation of children objects
    for ob in things:
        children = ob.GetChildren()
        things = things + list(filter(lambda x: "ax_" in c.GetName(), children))
    
    main = list(filter(lambda x: "axmain_" in x.GetName(), things))[0]
    importantThings = list(filter(lambda x: "ax_" in x.GetName(), things))
    for obj in importantThings:
        doUVWThing(obj, main.GetTag(c4d.Ttexture, nr=0))
    #obj = doc.SearchObject("Kugel")
    
    #Debug Things
    print(importantThings)

#Does the Process of Changing the Projection and UVW Tag    
def doUVWThing(obj, tag):
    #Gets the Texture Tag
    #tag = obj.GetTag(c4d.Ttexture,nr=0)
    #Gets the camera for the mapping
    cam = doc.SearchObject("Kamera_Tex")
    #Changes the Texture Projection Mode to Camera and configures it
    tag[c4d.TEXTURETAG_PROJECTION] = 8
    tag[c4d.TEXTURETAG_CAMERA] = cam
    tag[c4d.TEXTURETAG_CAMERA_FILMASPECT] = 1.7778 
    #Removes the old UVW Tag
    obj.KillTag(c4d.Tuvw,nr=0)
    #Generates a new UWV Tag
    uvw = c4d.utils.GenerateUVW(obj, obj.GetMg(), tag, obj.GetMg(), doc.GetRenderBaseDraw())
    #Adds the new UVW Tag to the Object
    obj.InsertTag(uvw, obj.GetTag(c4d.Ttexture))
    #Changes Projection to UWW
    tag[c4d.TEXTURETAG_PROJECTION] = 6
    
    #Debug Things
    print(uvw)
    print(tag[c4d.TEXTURETAG_PROJECTION])
