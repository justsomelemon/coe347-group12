import numpy as np
import default
from paraview.simple import *
import paraview.servermanager as sm
# disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

origin = [0.5, 0, 0]


def sliceXY(a_foam, renderView1, pLUT, uLUT, run, number):
    # create a new 'Slice'
    slice1 = Slice(Input=a_foam)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = origin
    slice1.SliceType.Normal = [0.0, 0.0, 1.0]

    # show data in view
    slice1Display = Show(slice1, renderView1)
    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.ColorArrayName = ['POINTS', 'p']
    slice1Display.LookupTable = pLUT
    slice1Display.OSPRayScaleArray = 'p'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'U'
    slice1Display.ScaleFactor = 0.01
    slice1Display.SelectScaleArray = 'p'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'p'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'

    # hide data in view
    Hide(a_foam, renderView1)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # change representation type
    slice1Display.SetRepresentationType('Surface With Edges')
    # hide data in view
    Hide(slice1, renderView1)

    return slice1


def velocityXYPlot(slice1, renderView1, pLUT, run):
    # create a new 'Glyph'
    glyph1 = Glyph(Input=slice1,
                   GlyphType='Arrow')
    glyph1.Scalars = ['POINTS', 'p']
    glyph1.Vectors = ['POINTS', 'U']
    # glyph1.ScaleFactor = 0.005
    glyph1.GlyphTransform = 'Transform2'
    # show data in view
    glyph1Display = Show(glyph1, renderView1)
    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, False)
    # update the view to ensure updated data information
    renderView1.Update()
    # set scalar coloring
    ColorBy(glyph1Display, ('POINTS', 'GlyphVector', 'Magnitude'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1)
    # rescale color and or opacity maps used to include current data range
    glyph1Display.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)
    # change representation type
    glyph1Display.SetRepresentationType('Surface')
    glyph1Display.Opacity = 1.0
    # set scalar coloring
    renderView1.Background = [0.0, 0.0, 0.0]

    glyph1Display = Show(glyph1, renderView1)
    default.plot(run, "U-glyphs", renderView1)

    Delete(glyph1)
    del glyph1
    glyph1Display.SetScalarBarVisibility(renderView1, False)
    Delete(glyph1Display)
    del glyph1Display


def velocityXYContour(slice1, renderView1, pLUT, uLUT, run, ax=1, n=100):
    # info = sm.Fetch(slice1)

    # #options for component: -1, 0, 1 and 2 => Mag, X, Y, Z
    # component = -1
    ids = ['', '_X', '_Y', '_Z']
    id2s = ['Magnitude', 'X', 'Y', 'Z']
    id = ids[ax]
    id2 = id2s[ax]
    component = ax-1

    # cdi = slice1.GetDataInformation().GetCompositeDataInformation()
    # for i in range(cdi.GetNumberOfChildren()):
    #     print 'Block Name: ', cdi.GetName(i)
    #     data = cdi.GetDataInformation(i).GetCellDataInformation()
    #     for j in range(data.GetNumberOfArrays()):
    #         array = data.GetArrayInformation(j)
    #         arrayName = array.GetName()
    #         dataRange = array.GetComponentRange(component)
    #         print arrayName, dataRange
    ranges = slice1.PointData.GetArray("U").GetComponentRange(component)
    # print(ranges)
    # create a new 'Contour'
    contour1 = Contour(Input=slice1)
    contour1.ContourBy = ['POINTS', 'U'+id]
    contour1.Isosurfaces = np.linspace(ranges[0], ranges[1], n).tolist()
    contour1.PointMergeMethod = 'Uniform Binning'
    # get color transfer function/color map for 'p'
    pLUT = GetColorTransferFunction('p')
    # show data in view
    contour1Display = Show(contour1, renderView1)
    # hide data in view
    Hide(slice1, renderView1)
    # show color bar/color legend
    contour1Display.SetScalarBarVisibility(renderView1, True)
    # update the view to ensure updated data information
    renderView1.Update()
    # set scalar coloring
    ColorBy(contour1Display, ('CELLS', 'U', id2))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    contour1Display.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    contour1Display.SetScalarBarVisibility(renderView1, True)
    UpdateScalarBarsComponentTitle(uLUT, contour1Display)
    default.plot(run, "U-"+id2+"_contour", renderView1)

    Delete(contour1)
    del contour1
    contour1Display.SetScalarBarVisibility(renderView1, False)
    Delete(contour1Display)
    del contour1Display


def velocityXYStream(a_foam, renderView1, pLUT, uLUT, run, ax=0, n=200):
    ids = ['', '_X', '_Y', '_Z']
    id2s = ['Magnitude', 'X', 'Y', 'Z']
    id = ids[ax]
    id2 = id2s[ax]
    component = ax-1

    # create a new 'Stream Tracer'
    streamTracer1 = StreamTracer(Input=a_foam,
                                 SeedType='High Resolution Line Source')
    # Properties modified on streamTracer1.SeedType
    streamTracer1.SeedType.Resolution = 100
    # Properties modified on streamTracer1
    streamTracer1.MaximumStreamlineLength = 100
    # show data in view
    streamTracer1Display = Show(streamTracer1, renderView1)
    # trace defaults for the display properties.
    streamTracer1Display.Representation = 'Surface'
    # hide data in view
    Hide(a_foam, renderView1)
    # show color bar/color legend
    streamTracer1Display.SetScalarBarVisibility(renderView1, True)
    # update the view to ensure updated data information
    renderView1.Update()
    # reset view to fit data
    renderView1.ResetCamera()
    # set scalar coloring
    ColorBy(streamTracer1Display, ('POINTS', 'U', id2))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    streamTracer1Display.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    streamTracer1Display.SetScalarBarVisibility(renderView1, True)
    # Properties modified on streamTracer1.SeedType
    streamTracer1.SeedType.Point1 = [2, 4.0, 0]
    streamTracer1.SeedType.Point2 = [2, -4.0, 0]
    # update the view to ensure updated data information
    renderView1.Update()
    # Rescale transfer function
    uLUT.RescaleTransferFunction(1.31913544397e-06, 1.0)
    # get opacity transfer function/opacity map for 'U'
    uPWF = GetOpacityTransferFunction('U')
    # Rescale transfer function
    uPWF.RescaleTransferFunction(1.31913544397e-06, 1.0)
    # reset view to fit data
    renderView1.ResetCamera()
    # Properties modified on streamTracer1.SeedType
    streamTracer1.SeedType.Resolution = n
    # update the view to ensure updated data information
    renderView1.Update()

    default.plot(run, "U-"+id2+"_streamlines", renderView1)

    # destroy streamTracer1
    Delete(streamTracer1)
    del streamTracer1
    streamTracer1Display.SetScalarBarVisibility(renderView1, False)
    Delete(streamTracer1Display)
    del streamTracer1Display
