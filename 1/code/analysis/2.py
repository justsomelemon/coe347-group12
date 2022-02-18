#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
slice1 = FindSource('Slice1')

# create a new 'Contour'
contour1 = Contour(Input=slice1)
contour1.ContourBy = ['POINTS', 'p']
contour1.Isosurfaces = [0.240919828414917]
contour1.PointMergeMethod = 'Uniform Binning'

# find source
a_foam = FindSource('_.foam')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [741, 546]

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# show data in view
contour1Display = Show(contour1, renderView1)
# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['CELLS', 'p']
contour1Display.LookupTable = pLUT
contour1Display.OSPRayScaleArray = 'p'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'U'
contour1Display.ScaleFactor = 0.004093817621469498
contour1Display.SelectScaleArray = 'p'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'p'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'U_X']

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(contour1Display, ('CELLS', 'U', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# set scalar coloring
ColorBy(contour1Display, ('CELLS', 'U', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
contour1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(uLUT, contour1Display)