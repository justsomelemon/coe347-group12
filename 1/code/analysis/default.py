import os
import scandir
import sys
sys.path.append("/usr/lib/paraview/site-packages")
# sys.path.append('/usr/lib/paraview')
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get current working directory
cwd = os.getcwd()
datapath = cwd+'/../data/'
plotdir =  cwd+'/../../plots/'
makedir = lambda run: os.system("mkdir -p "+plotdir+run+"/ ")
filename = lambda run: datapath+run+'/_.foam'
plotpath = lambda run,number: plotdir+run+"/"+run+'_'+number+'.png'

def plot(run,number,renderView1):
    # save screenshot
    SaveScreenshot(plotpath(run,number), renderView1, ImageResolution=resolution,
        OverrideColorPalette='PrintBackground',
        TransparentBackground=1)

resolution = [800, 600]

if __name__ == '__main__':

    def runDefaultProcessing(run):

        makedir(run)

        # create a new 'OpenFOAMReader'
        a_foam = OpenFOAMReader(FileName=filename(run))
        a_foam.MeshRegions = ['internalMesh']
        a_foam.CellArrays = ['U', 'p']

        # get animation scene
        animationScene1 = GetAnimationScene()
        # update animation scene based on data timesteps
        animationScene1.UpdateAnimationUsingDataTimeSteps()
        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        renderView1.ViewSize = resolution
        # get color transfer function/color map for 'p'
        pLUT = GetColorTransferFunction('p')
        # get opacity transfer function/opacity map for 'p'
        pPWF = GetOpacityTransferFunction('p')
        # show data in view
        a_foamDisplay = Show(a_foam, renderView1)
        # trace defaults for the display properties.
        a_foamDisplay.Representation = 'Surface'
        a_foamDisplay.ColorArrayName = ['POINTS', 'p']
        a_foamDisplay.LookupTable = pLUT
        a_foamDisplay.OSPRayScaleArray = 'p'
        a_foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
        a_foamDisplay.SelectOrientationVectors = 'U'
        a_foamDisplay.ScaleFactor = 0.010000000149011612
        a_foamDisplay.SelectScaleArray = 'p'
        a_foamDisplay.GlyphType = 'Arrow'
        a_foamDisplay.GlyphTableIndexArray = 'p'
        a_foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
        a_foamDisplay.PolarAxes = 'PolarAxesRepresentation'
        a_foamDisplay.ScalarOpacityFunction = pPWF
        a_foamDisplay.ScalarOpacityUnitDistance = 0.01924175606617764
        # reset view to fit data
        renderView1.ResetCamera()
        # show color bar/color legend
        a_foamDisplay.SetScalarBarVisibility(renderView1, True)
        # update the view to ensure updated data information
        renderView1.Update()
        # change representation type
        a_foamDisplay.SetRepresentationType('Surface With Edges')
        # current camera placement for renderView1
        renderView1.CameraPosition = [0.05000000074505806, 0.05000000074505806, 0.27888724573938806]
        renderView1.CameraFocalPoint = [0.05000000074505806, 0.05000000074505806, 0.004999999888241291]
        renderView1.CameraParallelScale = 0.07088723543695315
        renderView1.AxesGrid.Visibility = 1

        #-------------------------------------------------------------------- MAKE PLOTS

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'p'))
        # Hide the scalar bar for this color map if no visible data is colored by it.
        HideScalarBarIfNotNeeded(pLUT, renderView1)
        # rescale color and/or opacity maps used to include current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(True, False)
        # show color bar/color legend
        a_foamDisplay.SetScalarBarVisibility(renderView1, True)
        plot(run,"P",renderView1)


        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'Magnitude'))
        # Hide the scalar bar for this color map if no visible data is colored by it.
        HideScalarBarIfNotNeeded(pLUT, renderView1)
        # rescale color and/or opacity maps used to include current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(True, False)
        # show color bar/color legend
        a_foamDisplay.SetScalarBarVisibility(renderView1, True)
        # get color transfer function/color map for 'U'
        uLUT = GetColorTransferFunction('U')
        plot(run,"U",renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'X'))
        # rescale color and/or opacity maps used to exactly fit the current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(False, False)
        # Update a scalar bar component title.
        UpdateScalarBarsComponentTitle(uLUT, a_foamDisplay)
        plot(run,"U_X",renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'Y'))
        # rescale color and/or opacity maps used to exactly fit the current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(False, False)
        # Update a scalar bar component title.
        UpdateScalarBarsComponentTitle(uLUT, a_foamDisplay)
        plot(run,"U_Y",renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'Z'))
        # rescale color and/or opacity maps used to exactly fit the current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(False, False)
        # Update a scalar bar component title.
        UpdateScalarBarsComponentTitle(uLUT, a_foamDisplay)
        plot(run,"U_Z",renderView1)

        import slice
        slice1 = slice.sliceXY(a_foam,renderView1,pLUT,uLUT,run,"U-glyphs")
        slice.velocityXYPlot(slice1,renderView1,pLUT,run)
        slice.velocityXYContour(slice1,renderView1,pLUT,uLUT,run)
        slice.velocityXYContour(slice1,renderView1,pLUT,uLUT,run,ax=2)
        slice.velocityXYContour(slice1,renderView1,pLUT,uLUT,run,ax=0)

    runs = [f.name for f in scandir.scandir(datapath)]
    for run in runs:
        print("Plotting for Run {}".format(run))
        runDefaultProcessing(run)
