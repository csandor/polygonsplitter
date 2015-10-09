"""
Splitting polygons into equal area parts
"""
from qgis.core import (QgsFeature, QgsGeometry,
                       QgsVectorLayer, QgsMapLayerRegistry,
                       QgsField,QgsPoint)
from PyQt4.QtCore import QVariant
from qgis.utils import iface
import math

#this is required for the qgis script runner plugin
def run_script(iface):
    #global lineLayer
    #lineLayer = QgsVectorLayer("LineString?crs=3785", "split_line", "memory")
    eqsplit_inst = EqSplitPolygon(iface)
    eqsplit_inst.splitSelected(15,5,"v",True)
    #QgsMapLayerRegistry.instance().addMapLayer(lineLayer)

class EqSplitPolygon:
    #def __init__(self,iface):
    def __init__(self):
        self.debug=False
        pass

    def splitSelected(self,targetArea,granulFactor,method="h",splitEven=True):
        global recurs
        recurs=0;
        layer = iface.mapCanvas().currentLayer()
        if layer:
            #Gets layer CRS for new layer
            crs=layer.crs().description()
            if self.debug: print "Starting, Layer crs: " + crs
            # Create a new memory layer and add an area attribute
            polyLayer = QgsVectorLayer("MultiPolygon?crs="+crs, "split_poly", "memory")
            polyLayer.dataProvider().addAttributes( [ QgsField("area", QVariant.Double) ] )
            #QgsMapLayerRegistry.instance().addMapLayer(polyLayer)
            allFeatures=False
            if not layer.selectedFeatures():
                layer.invertSelection();
                allFeatures=True
            #save original target area
            origTargetArea=targetArea
            # Loop though all the selected features
            for feature in layer.selectedFeatures():
                geom = feature.geometry()
                if self.debug: print "Starting Number of original geoms: ",str(len(geom.asGeometryCollection()))
                if self.debug: print "Starting Number of part to split into: ",str(geom.area()/targetArea)
                div=round(geom.area()/origTargetArea)
                if div<1:
                    div=1
                if splitEven:
                    targetArea=geom.area()/div
                    if self.debug: print "Spliteven selected. modifying target area to:", targetArea
                if div>1:
                    granularity=round(granulFactor*geom.area()/targetArea)
                    if self.debug: print "Granularity: ",granularity
                    #Figure out direction to start with from cutting method
                    #If alternating, start horizontally
                    if method=="a":
                        firstDirection="h"
                    else:
                        firstDirection=method
                    self.alternatingSlice(geom,polyLayer,targetArea,granularity,firstDirection,method)
                else:
                    self.addGeomToLayer(geom,polyLayer)
            polyLayer.updateExtents()
            #if self.debug: print recurs
            QgsMapLayerRegistry.instance().addMapLayer(polyLayer)
            if allFeatures:
                layer.invertSelection();


    def alternatingSlice(self,geom,polyLayer,targetArea,granularity,direction,method):
        """
        Slice a poly in alternating directions
        """
        global recurs
        recurs+=1
        if self.debug: print "******************************"
        if self.debug: print "Slicing, No of part: ",str(recurs)
        if self.debug: print "Slicing, Granularity remaining: ", str(granularity)
        bbox=[geom.boundingBox().xMinimum(),geom.boundingBox().yMinimum(),geom.boundingBox().xMaximum(),geom.boundingBox().yMaximum()]
        if direction=="h":
            step=(bbox[2]-bbox[0])/granularity
            pointer=bbox[0]
        else:
            step=(bbox[3]-bbox[1])/granularity
            pointer=bbox[1]
        totalArea=0
        slices=0
        #save the original geom
        tempGeom=QgsGeometry(geom)
        #start slicing until targetArea is reached
        while totalArea<targetArea*0.999:
            pointer+=step
            if direction=="h":
                startPt=QgsPoint(pointer,bbox[1])
                endPt=QgsPoint(pointer,bbox[3])
                (multiGeom,tempGeom)=self.cutPoly(tempGeom,startPt,endPt)
            else:
                startPt=QgsPoint(bbox[0],pointer)
                endPt=QgsPoint(bbox[2],pointer)
                (tempGeom,multiGeom)=self.cutPoly(tempGeom,startPt,endPt)
            if multiGeom!=None:
                totalArea+=multiGeom.area();
            slices+=1
        if self.debug: print "Slicing, Slices: ", str(slices)
        #do the real cutting when reached targetArea and add "left" feature to layer
        if self.debug: print "Cutting with line, Cutline:", startPt,",",endPt
        if direction=="h":
            (multiGeom,geom)=self.cutPoly(geom,startPt,endPt,True)
            if multiGeom:
                if self.debug: print "After split, Parts to the left:",str(len(multiGeom.asGeometryCollection()))
            if geom:
                if self.debug: print "After split, Parts to the right:",str(len(geom.asGeometryCollection()))
        else:
            (geom,multiGeom)=self.cutPoly(geom,startPt,endPt,True)
            if geom:
                if self.debug: print "After split, Parts above:",str(len(geom.asGeometryCollection()))
            if multiGeom:
                if self.debug: print "After split, Parts under:",str(len(multiGeom.asGeometryCollection()))
        self.addGeomToLayer(multiGeom,polyLayer)
        #self.addGeomToLayer(QgsGeometry.fromPolyline([startPt,endPt]),lineLayer)
        if geom:
            if geom.area()>targetArea:
                if (method=="v") or ((method=="a") and (direction=="h")):
                    self.alternatingSlice(geom,polyLayer,targetArea,granularity-slices,"v",method)
                else:
                    self.alternatingSlice(geom,polyLayer,targetArea,granularity-slices,"h",method)
            else:
                self.addGeomToLayer(geom,polyLayer)

    def cutPoly(self,geom,startPt,endPt,debug=False):
        """
        Cut a geometry by a 2 point line
        return geoms left of line and right of line
        """
        #if we have disjoint Multi geometry as geom to split we need to iterate over its parts
        splittedGeoms=[]
        leftFragments=[]
        rightFragments=[]
        #if self.debug: print "Number of geoms when slicing: ",str(len(geom.asGeometryCollection()))
        for geomPart in geom.asGeometryCollection():
            #split the actual part by cut line defined by startPt,endPt
            (res,splittedGeomsPart,topo)=geomPart.splitGeometry([startPt,endPt],False)
            splittedGeoms+=splittedGeomsPart
            #Add the remaining geomPart to the rightFragments or letfFragments
            #depending on distance
            d=self.signedDistCentroidFromLine(geomPart,startPt,endPt)
            if d>0:
                rightFragments.append(geomPart)
            else:
                leftFragments.append(geomPart)
            #if self.debug: print j,splittedGeoms

        for fragment in splittedGeoms:
            """
            calculate signed distance of centroid of fragment and the splitline
            if signed distance is below zero, the point is to the left of the line
            if above zero the point is to the right of the line
            """
            d=self.signedDistCentroidFromLine(fragment,startPt,endPt)
            #if debug==True:
                #if self.debug: print d

            if d>0:
                rightFragments.append(fragment)
            else:
                leftFragments.append(fragment)

        #if self.debug: print "Left frags:",len(leftFragments),"Right frags:",len(rightFragments)
        leftGeom=self.buildMultiPolygon(leftFragments)
        rightGeom=self.buildMultiPolygon(rightFragments)
        return leftGeom,rightGeom

    def buildMultiPolygon(self,polygonList):
        """
        Build multi polygon feature from a list of polygons
        """
        geomlist=[]
        for geom in polygonList:
            # Cut 'MULTIPOLYGON(*) if we got one'
            if geom.exportToWkt()[:12]=="MULTIPOLYGON":
                geomWkt=geom.exportToWkt()[13:len(geom.exportToWkt())-1]
            else:
                # Cut 'POLYGON' if we got one
                geomWkt=geom.exportToWkt()[7:]
            geomlist.append(str(geomWkt))
        multiGeomWKT="MULTIPOLYGON("
        multiGeomWKT +=",".join(geomlist)
        multiGeomWKT+=")"
        #if self.debug: print multiGeomWKT
        multiGeom=QgsGeometry.fromWkt(multiGeomWKT)
        return multiGeom

    def addGeomToLayer(self,geom,layer):
        """
        Add a geometry to a layer as a new feature
        No attributes are set
        """
        fet = QgsFeature()
        fet.setGeometry(geom)
        area=geom.area()#/1000000
        if self.debug: print "Area of geom added to layer:", str(area)
        layer.dataProvider().addFeatures([fet])
        layer.dataProvider().changeAttributeValues({fet.id(): { 0: area}});
        layer.updateExtents()

    def signedDistCentroidFromLine(self,geom,startPt,endPt):
        #calculate signed distance of centroid of fragment and the splitline
        v1=endPt[0]-startPt[0]
        v2=endPt[1]-startPt[1]
        A=v2
        B=-v1
        C=-v2*startPt[0]+v1*startPt[1]
        centr=geom.centroid().boundingBox()
        return (A*centr.xMinimum()+B*centr.yMinimum()+C)/math.sqrt(A**2+B**2)
