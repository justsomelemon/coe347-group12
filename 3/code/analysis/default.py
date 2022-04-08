from utils import *
from paraview.simple import *
import os
import sys
import re
sys.path.append("/usr/lib/paraview/site-packages")
# sys.path.append('/usr/lib/paraview')
# import the simple module from the paraview
# disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


def plot(run, number, renderView1):
    # save screenshot
    SaveScreenshot(plotpath(run, number), renderView1, ImageResolution=resolution,
                   OverrideColorPalette='PrintBackground',
                   TransparentBackground=0)


resolution = [1000, 800]

if __name__ == '__main__':

    def runDefaultProcessing(run):

        makedir(run)

        # create a new 'OpenFOAMReader'
        a_foam = OpenFOAMReader(FileName=filename(run))
        a_foam.MeshRegions = ['internalMesh']
        a_foam.CellArrays = ['T', 'U', 'p', 'rho']

        # get animation scene
        animationScene1 = GetAnimationScene()
        # update animation scene based on data timesteps
        animationScene1.UpdateAnimationUsingDataTimeSteps()
        animationScene1.GoToLast()
        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')
        # uncomment following to set a specific view size
        renderView1.ViewSize = resolution
        # get color transfer function/color map for 'p'
        pLUT = GetColorTransferFunction('p')
        pLUT.ApplyPreset('Cool to Warm (Extended)', True)
        # get color transfer function/color map for 'U'
        uLUT = GetColorTransferFunction('U')
        uLUT.ApplyPreset('Cool to Warm (Extended)', True)
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
        a_foamDisplay.SetRepresentationType('Surface')
        # current camera placement for renderView1
        # renderView1.CameraPosition = [
        #     0.05000000074505806, 0.05000000074505806, 0.27888724573938806]
        # renderView1.CameraFocalPoint = [
        #     0.05000000074505806, 0.05000000074505806, 0.004999999888241291]
        renderView1.CameraParallelScale = 4
        renderView1.InteractionMode = '2D'
        renderView1.AxesGrid.Visibility = 1

        # -------------------------------------------------------------------- MAKE PLOTS

        # set scalar coloring
        # ColorBy(a_foamDisplay, ('CELLS', 'cellNormals', 'Magnitude'))
        a_foamDisplay.RescaleTransferFunctionToDataRange(True, False)
        a_foamDisplay.SetRepresentationType('Surface With Edges')
        plot(run, "MESH", renderView1)

        renderView1.ResetCamera()
        renderView1.Update()

        # set scalar coloring
        renderView1.CameraParallelScale = 1
        # ColorBy(a_foamDisplay, ('CELLS', 'cellNormals', 'Magnitude'))
        a_foamDisplay.RescaleTransferFunctionToDataRange(True, False)
        a_foamDisplay.SetRepresentationType('Surface With Edges')
        plot(run, "MESH2", renderView1)

        renderView1.ResetCamera()
        renderView1.Update()

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'p'))
        # Hide the scalar bar for this color map if no visible data is colored by it.
        HideScalarBarIfNotNeeded(pLUT, renderView1)
        # rescale color and/or opacity maps used to include current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(True, False)
        # show color bar/color legend
        a_foamDisplay.SetRepresentationType('Surface')
        a_foamDisplay.SetScalarBarVisibility(renderView1, True)
        plot(run, "P", renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'Magnitude'))
        # Hide the scalar bar for this color map if no visible data is colored by it.
        HideScalarBarIfNotNeeded(pLUT, renderView1)
        # rescale color and/or opacity maps used to include current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(True, False)
        # show color bar/color legend
        a_foamDisplay.SetScalarBarVisibility(renderView1, True)

        plot(run, "U", renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'X'))
        # rescale color and/or opacity maps used to exactly fit the current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(False, False)
        # Update a scalar bar component title.
        UpdateScalarBarsComponentTitle(uLUT, a_foamDisplay)
        plot(run, "U_X", renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'Y'))
        # rescale color and/or opacity maps used to exactly fit the current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(False, False)
        # Update a scalar bar component title.
        UpdateScalarBarsComponentTitle(uLUT, a_foamDisplay)
        plot(run, "U_Y", renderView1)

        # set scalar coloring
        ColorBy(a_foamDisplay, ('CELLS', 'U', 'Z'))
        # rescale color and/or opacity maps used to exactly fit the current data range
        a_foamDisplay.RescaleTransferFunctionToDataRange(False, False)
        # Update a scalar bar component title.
        UpdateScalarBarsComponentTitle(uLUT, a_foamDisplay)
        plot(run, "U_Z", renderView1)
        a_foamDisplay.SetScalarBarVisibility(renderView1, False)

        # create a new 'Calculator'
        calculator1 = Calculator(Input=a_foam)
        # Properties modified on calculator1
        calculator1.ResultArrayName = 'a'
        calculator1.Function = 'sqrt(1.4*p/rho)'
        calculator1.AttributeMode = 'Cell Data'
        # show data in view
        calculator1Display = Show(calculator1, renderView1)
        # trace defaults for the display properties.
        calculator1Display.Representation = 'Surface'
        # set scalar coloring
        ColorBy(calculator1Display, ('CELLS', 'a'))
        aLUT = GetColorTransferFunction('a')
        aLUT.ApplyPreset('erdc_blue2cyan_BW', True)
        # Hide the scalar bar for this color map if no visible data is colored by it.
        UpdateScalarBarsComponentTitle(aLUT, calculator1Display)
        # rescale color and/or opacity maps used to include current data range
        calculator1Display.RescaleTransferFunctionToDataRange(True, False)
        # show color bar/color legend
        calculator1Display.SetScalarBarVisibility(renderView1, True)
        plot(run, "a", renderView1)
        Hide(calculator1, renderView1)

        # create a new 'Calculator'
        calculator2 = Calculator(Input=a_foam)
        # Properties modified on calculator1
        calculator2.ResultArrayName = 'Mach'
        calculator2.Function = 'mag(U)/sqrt(1.4*p/rho)'
        calculator2.AttributeMode = 'Cell Data'
        # show data in view
        calculator2Display = Show(calculator2, renderView1)
        # trace defaults for the display properties.
        calculator2Display.Representation = 'Surface'
        # set scalar coloring
        ColorBy(calculator2Display, ('CELLS', 'Mach'))
        aLUT = GetColorTransferFunction('Mach')
        aLUT.ApplyPreset('erdc_blue2cyan_BW', True)
        # Hide the scalar bar for this color map if no visible data is colored by it.
        UpdateScalarBarsComponentTitle(aLUT, calculator2Display)
        # rescale color and/or opacity maps used to include current data range
        calculator2Display.RescaleTransferFunctionToDataRange(True, False)
        # show color bar/color legend
        calculator2Display.SetScalarBarVisibility(renderView1, True)
        plot(run, "Mach", renderView1)
        Hide(calculator2, renderView1)

        import slice
        slice1 = slice.sliceXY(a_foam, renderView1,
                               pLUT, uLUT, run, "U-glyphs")
        # slice.velocityXYPlot(slice1, renderView1, pLUT, run)
        slice.velocityXYContour(slice1, renderView1, pLUT, uLUT, run)
        slice.velocityXYContour(slice1, renderView1, pLUT, uLUT, run, ax=2)
        slice.velocityXYContour(slice1, renderView1, pLUT, uLUT, run, ax=0)
        slice.pressureContour(slice1, renderView1, pLUT, uLUT, run)

        slice.velocityXYStream(a_foam, renderView1, pLUT, uLUT, run)
        slice.velocityXYStream(a_foam, renderView1, pLUT, uLUT, run, ax=1)
        slice.velocityXYStream(a_foam, renderView1, pLUT, uLUT, run, ax=2)

    allruns = os.listdir(datapath)
    runs = []
    for run in allruns:
        if 'run_' in run:
            runs.append(run)
    for run in runs:
        print("Plotting for Run {}".format(run))
        runDefaultProcessing(run)
