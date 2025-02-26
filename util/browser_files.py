from tkinter import Tk, filedialog

def select_files_and_dirs():
    """Opens file dialogs to select the required files and directories."""
    root = Tk()
    root.withdraw()  # Hide the root window

    root.title("Select Folder Containing All Images")
    root.update()
    data_dir = filedialog.askdirectory(title="Select Folder Containing All Images")

    root.title("Select CSV File with Image Group Mappings")
    root.update()
    csv_file = filedialog.askopenfilename(title="Select CSV File with Image Group Mappings", filetypes=[("CSV Files", "*.csv")])

    root.title("Save Filtered CSV As")
    root.update()
    filtered_csv = filedialog.asksaveasfilename(title="Save Filtered CSV As", defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

    root.title("Select Folder for Filtered Images")
    root.update()
    filtered_dir = filedialog.askdirectory(title="Select Folder for Filtered Images")

    root.title("Select Folder for Processed Images")
    root.update()
    final_output_dir = filedialog.askdirectory(title="Select Folder for Processed Images")

    root.title("Select Folder to Store Before/After Comparisons")
    root.update()
    enhanced_dir = filedialog.askdirectory(title="Select Folder to Store Before/After Comparisons")
    
    return data_dir, csv_file, filtered_csv, filtered_dir, final_output_dir, enhanced_dir
