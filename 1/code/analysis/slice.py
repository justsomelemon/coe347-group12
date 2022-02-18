from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()
import default

def sliceXY(a_foam,renderView1,pLUT,uLUT,run,number):
    # create a new 'Slice'
    slice1 = Slice(Input=a_foam)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [0.05, 0.05, 0.005]
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

def velocityVectorPlot(slice1,renderView1,pLUT,run):
    # create a new 'Glyph'
    glyph1 = Glyph(Input=slice1,
        GlyphType='Arrow')
    glyph1.Scalars = ['POINTS', 'p']
    glyph1.Vectors = ['POINTS', 'U']
    glyph1.ScaleFactor = 0.005
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
    default.plot(run,"U-glyphs",renderView1)

    Delete(glyph1)
    del glyph1
    glyph1Display.SetScalarBarVisibility(renderView1, False)
    Delete(glyph1Display)
    del glyph1Display
    

def velocityXContour(slice1,renderView1,pLUT,uLUT,run):
    # create a new 'Contour'
    contour1 = Contour(Input=slice1)
    contour1.ContourBy = ['POINTS', 'U_X']
    contour1.Isosurfaces = [0.240919828414917]
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
    ColorBy(contour1Display, ('CELLS', 'U', 'X'))
    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1)
    # rescale color and/or opacity maps used to include current data range
    contour1Display.RescaleTransferFunctionToDataRange(True, False)
    # show color bar/color legend
    contour1Display.SetScalarBarVisibility(renderView1, True)
    UpdateScalarBarsComponentTitle(uLUT, contour1Display)
    default.plot(run,"U-X_contour",renderView1)