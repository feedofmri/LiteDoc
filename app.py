import tkinter as tk
from tkinter import Label, TOP, X
from tkinter.ttk import Combobox
from tkinter import font


# Functions

def change_font(event):
    font_family = font_families[font_type.current()]
    font_size = font_size_ver.get()
    text_box.config(font=(font_family, font_size))
    
def change_font_size(event):
    font_family = font_families[font_type.current()]
    font_size = font_size_ver.get()
    text_box.config(font=(font_family, font_size))
    
def change_font_family(event):
    font_family = font_families[font_type.current()]
    font_size = font_size_ver.get()
    text_box.config(font=(font_family, font_size))
    
def change_text_color(event):
    text_color = text_color_ver.get()
    text_box.config(fg=text_color)
    
def change_text_type(event):
    text_type = text_type_ver.get()
    text_box.config(font=(text_type))
    









# GUI
root = tk.Tk()
root.title("LiteDoc")
root.geometry("1100x600")

root.iconbitmap("images/favicon.ico")

menubar = tk.Menu(root)
root.config(menu=menubar)

# File Menu Icons
new_icon = tk.PhotoImage(file="images/new.png")
open_icon = tk.PhotoImage(file="images/new.png")
save_icon = tk.PhotoImage(file="images/save.png")
save_as_icon = tk.PhotoImage(file="images/save-as.png")
exit_icon = tk.PhotoImage(file="images/exit.png")

# Edit Menu Icons
undo_icon = tk.PhotoImage(file="images/undo.png")
redo_icon = tk.PhotoImage(file="images/redo.png")
cut_icon = tk.PhotoImage(file="images/cut.png")
copy_icon = tk.PhotoImage(file="images/copy.png")
paste_icon = tk.PhotoImage(file="images/paste.png")
find_icon = tk.PhotoImage(file="images/find.png")
select_all_icon = tk.PhotoImage(file="images/select-all.png")

# View Menu Icons
status_bar = tk.PhotoImage(file="images/status-bar.png")
zoom_in = tk.PhotoImage(file="images/zoom-in.png")
zoom_out = tk.PhotoImage(file="images/zoom-out.png")

themes = tk.PhotoImage(file="images/themes.png")

sunrise_serenity = tk.PhotoImage(file="images/sunrise-serenity.png")
ocean_breeze = tk.PhotoImage(file="images/ocean-breeze.png")
golden_glow = tk.PhotoImage(file="images/golden-glow.png")
forest_retreat = tk.PhotoImage(file="images/forest-retreat.png")
rose_quartz = tk.PhotoImage(file="images/rose-quartz.png")

# Tools Menu Icons
word_count = tk.PhotoImage(file="images/word-count.png")
character_count = tk.PhotoImage(file="images/character-count.png")
spell_check = tk.PhotoImage(file="images/spell-check.png")
convert_case = tk.PhotoImage(file="images/convert-case.png")

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", accelerator="Ctrl+N", image=new_icon, compound=tk.LEFT)
file_menu.add_command(label="Open", accelerator="Ctrl+O", image=open_icon, compound=tk.LEFT)
file_menu.add_command(label="Save", accelerator="Ctrl+S", image=save_icon, compound=tk.LEFT)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", image=save_as_icon, compound=tk.LEFT)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q", image=exit_icon, compound=tk.LEFT)

# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", image=undo_icon, compound=tk.LEFT)
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", image=redo_icon, compound=tk.LEFT)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", image=cut_icon, compound=tk.LEFT)
theme_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", image=copy_icon, compound=tk.LEFT)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", image=paste_icon, compound=tk.LEFT)
edit_menu.add_separator()
edit_menu.add_command(label="Find", accelerator="Ctrl+F", image=find_icon, compound=tk.LEFT)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="Ctrl+A", image=select_all_icon, compound=tk.LEFT)

# View Menu
view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Zoom In", accelerator="Ctrl+Shift+I", image=zoom_in, compound=tk.LEFT)
view_menu.add_command(label="Zoom Out", accelerator="Ctrl+Shift+O", image=zoom_out, compound=tk.LEFT)
view_menu.add_separator()

# Themes
theme_menu.add_radiobutton(label="Sunrise Serenity", compound=tk.LEFT, image=sunrise_serenity)
theme_menu.add_radiobutton(label="Ocean Breeze", compound=tk.LEFT, image=ocean_breeze)
theme_menu.add_radiobutton(label="Golden Glow", compound=tk.LEFT, image=golden_glow)
theme_menu.add_radiobutton(label="Forest Retreat", compound=tk.LEFT, image=forest_retreat)
theme_menu.add_radiobutton(label="Rose Quartz", compound=tk.LEFT, image=rose_quartz)
view_menu.add_cascade(label="Themes", menu=theme_menu)
view_menu.add_checkbutton(label="Status Bar", compound=tk.LEFT)

# Tools Menu
tools_menu = tk.Menu(menubar, tearoff=0)
tools_menu.add_command(label="Word Count", image=word_count, compound=tk.LEFT)
tools_menu.add_command(label="Character Count", image=character_count, compound=tk.LEFT)
tools_menu.add_command(label="Spell Check", image=spell_check, compound=tk.LEFT)
tools_menu.add_command(label="Convert Case", image=convert_case, compound=tk.LEFT)

# Add Menus to Menubar
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="View", menu=view_menu)
menubar.add_cascade(label="Tools", menu=tools_menu)


# Top Bar
top_bar = Label(root)
top_bar.pack(side=TOP, fill=X, padx=5, pady=5)


text_type = Combobox(top_bar)
text_type.grid(row=0, column=0, padx=(5, 5))


separator1 = Label(top_bar, text="|", foreground = 'gray')
separator1.grid(row=0, column=1)


text_color = Combobox(top_bar, width=5)
text_color.grid(row=0, column=2, padx=(5, 5))

separator2 = Label(top_bar, text="|", foreground = 'gray')
separator2.grid(row=0, column=3)


bold_icon = tk.PhotoImage(file="images/bold.png")
bold_button = tk.Button(top_bar, image=bold_icon, command=lambda: print("Bold"))
bold_button.grid(row=0, column=4, padx=(5, 5))

underline_icon = tk.PhotoImage(file="images/underline.png")
underline_button = tk.Button(top_bar, image=underline_icon, command=lambda: print("Underline"))
underline_button.grid(row=0, column=5, padx=(5, 5))

italic_icon = tk.PhotoImage(file="images/italic.png")
italic_button = tk.Button(top_bar, image=italic_icon, command=lambda: print("Italic"))
italic_button.grid(row=0, column=6, padx=(5, 5))

font_size_ver = tk.StringVar()
font_size = Combobox(top_bar, textvariable=font_size_ver, values=[8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72], width=3, state='readonly')
font_size.current(4)
font_size.grid(row=0, column=7, padx=(5, 5))


separator3 = Label(top_bar, text="|", foreground = 'gray')
separator3.grid(row=0, column=8)

left_align_icon = tk.PhotoImage(file="images/left-align.png")
left_align_button = tk.Button(top_bar, image=left_align_icon, command=lambda: print("Left Align"))
left_align_button.grid(row=0, column=9, padx=(5, 5))

center_align_icon = tk.PhotoImage(file="images/center-align.png")
center_align_button = tk.Button(top_bar, image=center_align_icon, command=lambda: print("Center Align"))
center_align_button.grid(row=0, column=10, padx=(5, 5))

right_align_icon = tk.PhotoImage(file="images/right-align.png")
right_align_button = tk.Button(top_bar, image=right_align_icon, command=lambda: print("Right Align"))
right_align_button.grid(row=0, column=11, padx=(5, 5))


separator4 = Label(top_bar, text="|", foreground = 'gray')
separator4.grid(row=0, column=12)


font_families = font.families()
font_family_ver = tk.IntVar()
font_type = Combobox(top_bar, textvariable=font_family_ver, values=font_families, width=20, state='readonly')
font_type.current(font_families.index('Poppins'))
font_type.grid(row=0, column=13, padx=(5, 5))


text_frame = tk.Frame(root)
text_frame.pack(fill='both', padx=80, pady=30, expand=True, side='left', anchor='nw')

# Text Box
text_box = tk.Text(text_frame, wrap='word', undo=True, font=('Poppins', 12), padx=50, pady=50, relief='flat')
text_box.pack(fill='both', side='left', expand=True)

# Scrollbar
scroll = tk.Scrollbar(text_frame, command=text_box.yview, relief='flat')
scroll.pack(side='right', fill='y', anchor='ne')

text_box.config(yscrollcommand=scroll.set)
scroll.config(command=text_box.yview)




root.mainloop()