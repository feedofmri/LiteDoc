import tkinter as tk
import tkinter as tk


root = tk.Tk()
root.title("LiteDoc")
root.geometry("1000x600")

root.iconbitmap("images/favicon.ico")

menubar = tk.Menu(root)
root.config(menu=menubar)

new_icon = tk.PhotoImage(file="images/new.png")
open_icon = tk.PhotoImage(file="images/new.png")
save_icon = tk.PhotoImage(file="images/save.png")
save_as_icon = tk.PhotoImage(file="images/save-as.png")
exit_icon = tk.PhotoImage(file="images/exit.png")

undo_icon = tk.PhotoImage(file="images/undo.png")
redo_icon = tk.PhotoImage(file="images/redo.png")
cut_icon = tk.PhotoImage(file="images/cut.png")
copy_icon = tk.PhotoImage(file="images/copy.png")
paste_icon = tk.PhotoImage(file="images/paste.png")
find_icon = tk.PhotoImage(file="images/find.png")
select_all_icon = tk.PhotoImage(file="images/select-all.png")

status_bar = tk.PhotoImage(file="images/status-bar.png")
zoom_in = tk.PhotoImage(file="images/zoom-in.png")
zoom_out = tk.PhotoImage(file="images/zoom-out.png")

themes = tk.PhotoImage(file="images/themes.png")

sunrise_serenity = tk.PhotoImage(file="images/sunrise-serenity.png")
ocean_breeze = tk.PhotoImage(file="images/ocean-breeze.png")
golden_glow = tk.PhotoImage(file="images/golden-glow.png")
forest_retreat = tk.PhotoImage(file="images/forest-retreat.png")
rose_quartz = tk.PhotoImage(file="images/rose-quartz.png")

word_count = tk.PhotoImage(file="images/word-count.png")
character_count = tk.PhotoImage(file="images/character-count.png")
spell_check = tk.PhotoImage(file="images/spell-check.png")
convert_case = tk.PhotoImage(file="images/convert-case.png")

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", accelerator="Ctrl+N", image=new_icon, compound=tk.LEFT)
file_menu.add_command(label="Open", accelerator="Ctrl+O", image=open_icon, compound=tk.LEFT)
file_menu.add_command(label="Save", accelerator="Ctrl+S", image=save_icon, compound=tk.LEFT)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", image=save_as_icon, compound=tk.LEFT)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q", image=exit_icon, compound=tk.LEFT)

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

view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Zoom In", accelerator="Ctrl+Shift+I", image=zoom_in, compound=tk.LEFT)
view_menu.add_command(label="Zoom Out", accelerator="Ctrl+Shift+O", image=zoom_out, compound=tk.LEFT)
view_menu.add_separator()

theme_menu.add_radiobutton(label="Sunrise Serenity", compound=tk.LEFT, image=sunrise_serenity)
theme_menu.add_radiobutton(label="Ocean Breeze", compound=tk.LEFT, image=ocean_breeze)
theme_menu.add_radiobutton(label="Golden Glow", compound=tk.LEFT, image=golden_glow)
theme_menu.add_radiobutton(label="Forest Retreat", compound=tk.LEFT, image=forest_retreat)
theme_menu.add_radiobutton(label="Rose Quartz", compound=tk.LEFT, image=rose_quartz)
view_menu.add_cascade(label="Themes", menu=theme_menu)
view_menu.add_checkbutton(label="Status Bar", compound=tk.LEFT)


tools_menu = tk.Menu(menubar, tearoff=0)
tools_menu.add_command(label="Word Count", image=word_count, compound=tk.LEFT)
tools_menu.add_command(label="Character Count", image=character_count, compound=tk.LEFT)
tools_menu.add_command(label="Spell Check", image=spell_check, compound=tk.LEFT)
tools_menu.add_command(label="Convert Case", image=convert_case, compound=tk.LEFT)



menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Edit", menu=edit_menu)
menubar.add_cascade(label="View", menu=view_menu)
menubar.add_cascade(label="Tools", menu=tools_menu)


root.mainloop()