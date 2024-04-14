from tkinter import *
from tkinter.ttk import Style
from customtkinter import *
from image import *
from video import *
from audio import *

#Handle function
def chooseInputFile(textbox):
    filename = filedialog.askopenfilename()
    textbox.delete("0.0", "end")
    textbox.insert("0.0", filename)

def updateOptionState():
    if option.get() == 1:  # Watermark Image choosen
        watermarkTextInput.configure(state="disabled", cursor="arrow")
        watermarkImageInput.configure(state="normal")
        optionFileBtn.configure(state="normal", fg_color="#3c8cd4")
    elif option.get() == 2:  # Watermark Text choosen
        watermarkTextInput.configure(state="normal")
        watermarkImageInput.configure(state="disabled", cursor="arrow")
        optionFileBtn.configure(state="disabled", fg_color="grey")  # Sửa đổi kiểu dáng của nút

def watermarkProcess():
    if (tabview._current_name == "Image"):
        pass
    elif (tabview._current_name == "Video"):
        pass
    elif (tabview._current_name == "Audio"):
        pass

#GUI
app = CTk()
# font_style = CTkFont(family='Montserrat', size=12, weight='bold')

app.geometry("800x600")
app.minsize(800, 600)
set_appearance_mode("light")
app.title("TMC Watermark")


tabview = CTkTabview(master=app)
tabview.pack(fill="both", expand=1)  # Thêm padding để căn chỉnh từ lề trái và lề trên

tabview.add("Image")
tabview.add("Video")
tabview.add("Audio")

#Image Tab
#Choose Input File
label = CTkLabel(master=tabview.tab("Image"), text="Input File", font=('Montserrat', 18, 'bold'))
label.place(relx=0.15, rely=0.05, anchor="w")

inputTextbox = CTkTextbox(master=tabview.tab("Image"), width=550, height=1, wrap="none")
inputTextbox.place(relx=0.15, rely=0.15, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Image"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(inputTextbox))
fileBtn.place(relx=0.85, rely=0.05, anchor="e")

#Options
optionLabel = CTkLabel(master=tabview.tab("Image"), text="Option", font=('Montserrat', 18, 'bold'))
optionLabel.place(relx=0.15, rely=0.25, anchor="w")

option = IntVar()

watermarkImage = CTkRadioButton(master=tabview.tab("Image"), text="Watermark Image", corner_radius=8, variable= option, value=1, font=('Montserrat', 14, 'bold'), command=updateOptionState)
watermarkImage.place(relx=0.15, rely=0.35, anchor="w")

watermarkImageInput = CTkTextbox(master=tabview.tab("Image"), width=350, height=1, wrap="none")
watermarkImageInput.place(relx=0.4, rely=0.35, anchor="w")

optionFileBtn = CTkButton(master=tabview.tab("Image"), text="Choose File...", width=100,corner_radius=8, command=lambda: chooseInputFile(watermarkImageInput))
optionFileBtn.place(relx=0.85, rely=0.25, anchor="e")

watermarkText = CTkRadioButton(master=tabview.tab("Image"), text="Watermark Text", corner_radius=8, variable= option, value=2, font=('Montserrat', 14, 'bold'), command=updateOptionState)
watermarkText.place(relx=0.15, rely=0.45, anchor="w")

watermarkTextInput = CTkTextbox(master=tabview.tab("Image"), width=350, height=1, wrap="none")
watermarkTextInput.place(relx=0.4, rely=0.45, anchor="w")


#position
positionLabel = CTkLabel(master=tabview.tab("Image"), text="Postion", font=('Montserrat', 18, 'bold'))
positionLabel.place(relx=0.15, rely=0.55, anchor="w")

vPositionLabel = CTkLabel(master=tabview.tab("Image"), text="Vertical", font=('Montserrat', 16, 'bold'))
vPositionLabel.place(relx=0.3, rely=0.55, anchor="w")

hPositionLabel = CTkLabel(master=tabview.tab("Image"), text="Horizontal", font=('Montserrat', 16, 'bold'))
hPositionLabel.place(relx=0.3, rely=0.65, anchor="w")

vCombobox = CTkComboBox(master=tabview.tab("Image"), values=["Left", "Center", "Right"])
vCombobox.place(relx=0.5, rely=0.55, anchor="w")
hCombobox = CTkComboBox(master=tabview.tab("Image"), values=["Top", "Center", "Bottom"])
hCombobox.place(relx=0.5, rely=0.65, anchor="w")

#Choose Output File
label = CTkLabel(master=tabview.tab("Image"), text="Output File", font=('Montserrat', 18, 'bold'))
label.place(relx=0.15, rely=0.75, anchor="w")

outputTextbox = CTkTextbox(master=tabview.tab("Image"), width=550, height=1, wrap="none")
outputTextbox.place(relx=0.15, rely=0.85, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Image"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(outputTextbox))
fileBtn.place(relx=0.85, rely=0.75, anchor="e")

exportBtn = CTkButton(master=tabview.tab("Image"), text="➡", width=100 ,corner_radius=8,font=('Montserrat', 24), command=watermarkProcess)
exportBtn.place(relx=0.85, rely=0.95, anchor="e")


# Video Tab
#Choose Input File
label = CTkLabel(master=tabview.tab("Video"), text="Input File", font=('Montserrat', 18, 'bold'))
label.place(relx=0.15, rely=0.05, anchor="w")

inputTextbox = CTkTextbox(master=tabview.tab("Video"), width=550, height=1, wrap="none")
inputTextbox.place(relx=0.15, rely=0.15, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Video"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(inputTextbox))
fileBtn.place(relx=0.85, rely=0.05, anchor="e")


#Options
optionLabel = CTkLabel(master=tabview.tab("Video"), text="Option", font=('Montserrat', 18, 'bold'))
optionLabel.place(relx=0.15, rely=0.25, anchor="w")

option = IntVar()

watermarkImage = CTkRadioButton(master=tabview.tab("Video"), text="Watermark Image", corner_radius=8, variable= option, value=1, font=('Montserrat', 14, 'bold'), command=updateOptionState)
watermarkImage.place(relx=0.15, rely=0.35, anchor="w")

watermarkImageInput = CTkTextbox(master=tabview.tab("Video"), width=350, height=1, wrap="none")
watermarkImageInput.place(relx=0.4, rely=0.35, anchor="w")

optionFileBtn = CTkButton(master=tabview.tab("Video"), text="Choose File...", width=100,corner_radius=8, command=lambda: chooseInputFile(watermarkImageInput))
optionFileBtn.place(relx=0.85, rely=0.25, anchor="e")

watermarkText = CTkRadioButton(master=tabview.tab("Video"), text="Watermark Text", corner_radius=8, variable= option, value=2, font=('Montserrat', 14, 'bold'), command=updateOptionState)
watermarkText.place(relx=0.15, rely=0.45, anchor="w")

watermarkTextInput = CTkTextbox(master=tabview.tab("Video"), width=350, height=1, wrap="none")
watermarkTextInput.place(relx=0.4, rely=0.45, anchor="w")


#position
positionLabel = CTkLabel(master=tabview.tab("Video"), text="Postion", font=('Montserrat', 18, 'bold'))
positionLabel.place(relx=0.15, rely=0.55, anchor="w")

vPositionLabel = CTkLabel(master=tabview.tab("Video"), text="Vertical", font=('Montserrat', 16, 'bold'))
vPositionLabel.place(relx=0.3, rely=0.55, anchor="w")

hPositionLabel = CTkLabel(master=tabview.tab("Video"), text="Horizontal", font=('Montserrat', 16, 'bold'))
hPositionLabel.place(relx=0.3, rely=0.65, anchor="w")

vCombobox = CTkComboBox(master=tabview.tab("Video"), values=["Left", "Center", "Right"])
vCombobox.place(relx=0.5, rely=0.55, anchor="w")
hCombobox = CTkComboBox(master=tabview.tab("Video"), values=["Top", "Center", "Bottom"])
hCombobox.place(relx=0.5, rely=0.65, anchor="w")

#Choose Output File
label = CTkLabel(master=tabview.tab("Video"), text="Output File", font=('Montserrat', 18, 'bold'))
label.place(relx=0.15, rely=0.75, anchor="w")

outputTextbox = CTkTextbox(master=tabview.tab("Video"), width=550, height=1, wrap="none")
outputTextbox.place(relx=0.15, rely=0.85, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Video"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(outputTextbox))
fileBtn.place(relx=0.85, rely=0.75, anchor="e")

exportBtn = CTkButton(master=tabview.tab("Video"), text="➡", width=100 ,corner_radius=8,font=('Montserrat', 24), command=watermarkProcess)
exportBtn.place(relx=0.85, rely=0.95, anchor="e")

#Audio Tab
#Choose Input File
label = CTkLabel(master=tabview.tab("Audio"), text="Input File", font=('Montserrat', 18, 'bold'))
label.place(relx=0.15, rely=0.05, anchor="w")

inputTextbox = CTkTextbox(master=tabview.tab("Audio"), width=550, height=1, wrap="none")
inputTextbox.place(relx=0.15, rely=0.15, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Audio"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(inputTextbox))
fileBtn.place(relx=0.85, rely=0.05, anchor="e")

#Watermark Audio
watermarkAudio = CTkLabel(master=tabview.tab("Audio"), text="Watermark Audio", font=('Montserrat', 18, 'bold'))
watermarkAudio.place(relx=0.15, rely=0.25, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Audio"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(watermarkAudioInput))
fileBtn.place(relx=0.85, rely=0.25, anchor="e")

watermarkAudioInput = CTkTextbox(master=tabview.tab("Audio"), width=550, height=1, wrap="none")
watermarkAudioInput.place(relx=0.15, rely=0.35, anchor="w")

#Choose Output File
label = CTkLabel(master=tabview.tab("Audio"), text="Output File", font=('Montserrat', 18, 'bold'))
label.place(relx=0.15, rely=0.45, anchor="w")

outputTextbox = CTkTextbox(master=tabview.tab("Audio"), width=550, height=1, wrap="none")
outputTextbox.place(relx=0.15, rely=0.55, anchor="w")

fileBtn = CTkButton(master=tabview.tab("Audio"), text="Choose File...", width=100 ,corner_radius=8, command=lambda: chooseInputFile(outputTextbox))
fileBtn.place(relx=0.85, rely=0.45, anchor="e")
exportBtn = CTkButton(master=tabview.tab("Audio"), text="➡", width=100 ,corner_radius=8,font=('Montserrat', 24), command=watermarkProcess)
exportBtn.place(relx=0.85, rely=0.65, anchor="e")
app.mainloop()