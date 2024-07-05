import win32com.client
import os

def open_solidworks():
    # Create a connection to SolidWorks
    solidworks = win32com.client.Dispatch("SldWorks.Application")
    return solidworks

def close_solidworks(solidworks):
    solidworks.ExitApp()

def rebuild_assemblies(assembly_paths):
    # Open SolidWorks and get the application object
    sw_app = open_solidworks()

    index = 0

    for assembly_path in assembly_paths:
            

        # Open the assembly document
        assembly = sw_app.OpenDoc(assembly_path, 2)  # 2 means assembly type
        
        if not assembly:
            print("Error: Unable to open the assembly file at {}".format(assembly_path))

        # Rebuild the assembly
        assembly.ForceRebuild3(True)  # True to force a rebuild

        assembly.SaveAs(assembly_path)

        sw_app.CloseDoc(assembly_path)

        index += 1

    # Close SolidWorks
    close_solidworks(sw_app)
