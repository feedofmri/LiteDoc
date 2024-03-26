import tkinter as tk
from tkinter import Label, TOP, X, simpledialog, Tk, Text
from tkinter.ttk import Combobox
from tkinter import font
import emoji
import tkinter.filedialog
from tkinter import filedialog
from PIL import Image, ImageTk
import emoji

# Functions
    
def change_text_type(event):
    selected_type = text_type_var.get()
    if selected_type == "Heading 1":
        text_box.tag_configure("heading1", font=("Helvetica", 24, "bold"))
        text_box.insert(tk.END, "\nHeading 1\n", "heading1")
    elif selected_type == "Heading 2":
        text_box.tag_configure("heading2", font=("Helvetica", 20, "bold"))
        text_box.insert(tk.END, "\nHeading 2\n", "heading2")
    elif selected_type == "Heading 3":
        text_box.tag_configure("heading3", font=("Helvetica", 16, "bold"))
        text_box.insert(tk.END, "\nHeading 3\n", "heading3")
    elif selected_type == "Subheading":
        text_box.tag_configure("subheading", font=("Helvetica", 14, "italic"))
        text_box.insert(tk.END, "\nSubheading\n", "subheading")
    elif selected_type == "Normal Text":
        text_box.tag_configure("normal", font=("Helvetica", 12))
        text_box.insert(tk.END, "\nNormal Text\n", "normal")

def change_text_color(event):
    selected_color = text_color_var.get()
    text_box.config(fg=selected_color)
    
    
def make_bold():
    text_box.tag_add("bold", "sel.first", "sel.last")
    text_box.tag_configure("bold", font=text_box.cget("font") + " bold")
    
def make_italic():
    text_box.tag_add("italic", "sel.first", "sel.last")
    text_box.tag_configure("italic", font=text_box.cget("font") + " italic")
    
def make_underline():
    text_box.tag_add("underline", "sel.first", "sel.last")
    text_box.tag_configure("underline", font=text_box.cget("font") + " underline")
    
def make_quote():
    text_box.tag_add("quote", "sel.first", "sel.last")
    text_box.tag_configure("quote", font=text_box.cget("font") + " italic", foreground="blue")
    
def make_code():
    text_box.tag_add("code", "sel.first", "sel.last")
    text_box.tag_configure("code", font=("Courier", 12))
    
def make_link():
    selected_text = text_box.get("sel.first", "sel.last")
    url = simpledialog.askstring("Insert Link", "Enter the URL:")
    if url:
        text_box.insert(tk.INSERT, selected_text, ("link", url))
    
    text_box.tag_add("link", "sel.first", "sel.last")
    text_box.tag_configure("link", foreground="blue", underline=True)

    
def insert_emoji():
    # This is a simple example with a predefined list of emojis.
    # You would need to replace this with a custom dialog or another way to select an emoji.
    emojis = [ "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸", "🤩", "🥳", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯", "😳", "🥵", "🥶", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄", "😯", "😦", "😧", "😮", "😲", "🥱", "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "🤡", "💩", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", "😺", "😸", "😹", "😻", "😼", "😽", "🙀", "😿", "😾", "🙈", "🙉", "🙊"]
    #emojis = [ "😀", "😃", "😄"]
    def insert_emoji_and_close(emoji):
        text_box.insert(tk.INSERT, emoji)
        emoji_picker.destroy()

    # Create a new Toplevel window
    emoji_picker = tk.Toplevel(root)
    emoji_picker.title("Select an emoji")

    # Create a Scrollbar and a Canvas
    scrollbar = tk.Scrollbar(emoji_picker)
    canvas = tk.Canvas(emoji_picker, yscrollcommand=scrollbar.set)
    scrollbar.config(command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Frame inside the Canvas
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)

    # Create a button for each emoji
    for i, emoji in enumerate(emojis):
        button = tk.Button(frame, text=emoji, command=lambda emoji=emoji: insert_emoji_and_close(emoji))
        button.grid(row=i // 10, column=i % 10)  # Arrange the buttons in a 10x10 grid

    # Update the scroll region of the Canvas
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox(tk.ALL))

    # Set the size of the emoji picker window
    emoji_picker.geometry("350x350")  # Width x Height
    emoji_picker.iconbitmap("images/favicon.ico")

    # Center the emoji picker window
    emoji_picker.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (emoji_picker.winfo_width() // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (emoji_picker.winfo_height() // 2)
    emoji_picker.geometry(f"+{x}+{y}")

def insert_image():
    global photo
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif"), ("All Files", "*.*")])
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        # Insert the image at the current insertion point
        text_box.image_create(tk.INSERT, image=photo)
        # Move the insertion point to the next line
        text_box.mark_set(tk.INSERT, "insert +1l")
    
def change_font_size(event=None):
    selected_size = font_size.get()
    text_box.config(font=(text_box.cget("font"), int(selected_size)))
    
def change_font(event):
    font_family = font_families[font_type.current()]
    font_size = font_size_var.get()
    text_box.config(font=(font_family, font_size))
    
def undo():
    text_box.edit_undo()
    
def redo():
    text_box.edit_redo()
    
def cut():
    text_box.event_generate("<<Cut>>")
    
def copy():
    text_box.event_generate("<<Copy>>")

def paste():
    text_box.event_generate("<<Paste>>")
    
def find():
    find_text = simpledialog.askstring("Find", "Enter the text to find:")
    if find_text:
        start = text_box.search(find_text, "1.0", stopindex=tk.END)
        if start:
            end = f"{start}+{len(find_text)}c"
            text_box.tag_add("find", start, end)
            text_box.tag_configure("find", background="yellow")
            text_box.mark_set(tk.INSERT, end)
            text_box.see(tk.INSERT)
        else:
            print("Text not found")
            
def select_all():
    text_box.tag_add("sel", "1.0", tk.END)

def zoom_in_text(event=None):
    global font_size
    try:
        new_font_size = int(font_size.get()) + 2
    except ValueError:
        print(f"Invalid font size: {font_size.get()}")
        return
    text_box.config(font=(text_box.cget("font"), new_font_size))

def zoom_out_text(event=None):
    global font_size
    try:
        new_font_size = int(font_size.get()) - 2
    except ValueError:
        print(f"Invalid font size: {font_size.get()}")
        return
    text_box.config(font=(text_box.cget("font"), new_font_size))

def on_ctrl_scroll(event):
    if event.delta > 0:
        zoom_in_text()
    else:
        zoom_out_text()
    
    
def word_count():
    global text_box
    text = text_box.get("1.0", tk.END)
    words = text.split()
    num_words = len(words)
    print(f"Word Count: {num_words}")
    tk.messagebox.showinfo("Word Count", f"Total Words: {num_words}")
    
def character_count():
    global text_box
    text = text_box.get("1.0", tk.END)
    num_characters = len(text)
    print(f"Character Count: {num_characters}")
    tk.messagebox.showinfo("Character Count", f"Total Characters: {num_characters}")
    
def spell_check():
    pass

def convert_case():
    selected_text = text_box.get("sel.first", "sel.last")
    if selected_text.isupper():
        text_box.delete("sel.first", "sel.last")
        text_box.insert("sel.first", selected_text.lower())
    elif selected_text.islower():
        text_box.delete("sel.first", "sel.last")
        text_box.insert("sel.first", selected_text.upper())
    elif selected_text.istitle():
        text_box.delete("sel.first", "sel.last")
        text_box.insert("sel.first", selected_text.upper())
    

def left_align():
    text_box.tag_add("left", "sel.first", "sel.last")
    text_box.tag_configure("left", justify='left')
    
def center_align():
    text_box.tag_add("center", "sel.first", "sel.last")
    text_box.tag_configure("center", justify='center')
    
def right_align():
    text_box.tag_add("right", "sel.first", "sel.last")
    text_box.tag_configure("right", justify='right')
    
def theme_light():
    pass
    
def new_file():
    text_box.delete("1.0", tk.END)
    
def open_file():
    file_path = tk.filedialog.askopenfilename()
    with open(file_path, "r") as file:
        text = file.read()
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)
        
current_file_path = None

def save_file():
    global current_file_path
    if current_file_path is None:
        save_as_file()
    else:
        with open(current_file_path, "w") as file:
            text = text_box.get("1.0", tk.END)
            file.write(text)

def save_as_file():
    global current_file_path
    file_path = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        current_file_path = file_path
        with open(file_path, "w") as file:
            text = text_box.get("1.0", tk.END)
            file.write(text)
        

# GUI
root = tk.Tk()
root.title("LiteDocs")
root.geometry("1100x600")
root.iconbitmap("images/favicon.ico")

# File Menu Icons
new_icon = tk.PhotoImage(file="images/new.png")
open_icon = tk.PhotoImage(file="images/open.png")
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
zoom_in = tk.PhotoImage(file="images/zoom-in.png")
zoom_out = tk.PhotoImage(file="images/zoom-out.png")

# Tools Menu Icons
word_count = tk.PhotoImage(file="images/word-count.png")
character_count = tk.PhotoImage(file="images/character-count.png")
spell_check = tk.PhotoImage(file="images/spell-check.png")
convert_case = tk.PhotoImage(file="images/convert-case.png")

menubar = tk.Menu(root)
root.config(menu=menubar)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", accelerator="Ctrl+N", image=new_icon, compound=tk.LEFT, command=new_file)
file_menu.add_command(label="Open", accelerator="Ctrl+O", image=open_icon, compound=tk.LEFT, command=open_file)
file_menu.add_command(label="Save", accelerator="Ctrl+S", image=save_icon, compound=tk.LEFT, command=save_file)
file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", image=save_as_icon, compound=tk.LEFT, command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit, accelerator="Ctrl+Q", image=exit_icon, compound=tk.LEFT)
menubar.add_cascade(label="File", menu=file_menu)

# Edit Menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", image=undo_icon, compound=tk.LEFT, command=undo)
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", image=redo_icon, compound=tk.LEFT, command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X", image=cut_icon, compound=tk.LEFT, command=cut)
edit_menu.add_command(label="Copy", accelerator="Ctrl+C", image=copy_icon, compound=tk.LEFT, command=copy)
edit_menu.add_command(label="Paste", accelerator="Ctrl+V", image=paste_icon, compound=tk.LEFT, command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Find", accelerator="Ctrl+F", image=find_icon, compound=tk.LEFT, command=find)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", accelerator="Ctrl+A", image=select_all_icon, compound=tk.LEFT, command=select_all)
menubar.add_cascade(label="Edit", menu=edit_menu)

# View Menu
view_menu = tk.Menu(menubar, tearoff=0)
view_menu.add_command(label="Zoom In", accelerator="", image=zoom_in, compound=tk.LEFT, command=zoom_in_text)
view_menu.add_command(label="Zoom Out", accelerator="", image=zoom_out, compound=tk.LEFT, command=zoom_out_text)
menubar.add_cascade(label="View", menu=view_menu)

# Tools Menu
tools_menu = tk.Menu(menubar, tearoff=0)
tools_menu.add_command(label="Word Count", image=word_count, compound=tk.LEFT, command=word_count)
tools_menu.add_command(label="Character Count", image=character_count, compound=tk.LEFT, command=character_count)
tools_menu.add_command(label="Spell Check", image=spell_check, compound=tk.LEFT, command=spell_check)
tools_menu.add_command(label="Convert Case", image=convert_case, compound=tk.LEFT, command=convert_case)
menubar.add_cascade(label="Tools", menu=tools_menu)

# Top Bar
top_bar = Label(root)
top_bar.pack(side=TOP, fill=X, padx=5, pady=5)

text_type_var = tk.StringVar()
text_type_values = ["Heading 1", "Heading 2", "Heading 3", "Subheading", "Normal Text", "Quote", "Code"]
text_type = Combobox(top_bar, textvariable=text_type_var, values=text_type_values, width=12, state='readonly')
text_type.current(4)
text_type.grid(row=0, column=0, padx=(5, 5))
text_type.bind("<<ComboboxSelected>>", change_text_type)

separator = tk.Label(top_bar, text=" | ", foreground="grey")
separator.grid(row=0, column=1)

text_color_var = tk.StringVar()
text_color = Combobox(top_bar, textvariable=text_color_var, values=["black", "red", "green", "blue"], width=5)
text_color.current(0)
text_color.grid(row=0, column=2, padx=(5, 5))
text_color.bind("<<ComboboxSelected>>", change_text_color)

separator = tk.Label(top_bar, text=" | ", foreground="grey")
separator.grid(row=0, column=3)

bold_icon = tk.PhotoImage(file="images/bold.png")
bold_button = tk.Button(top_bar, image=bold_icon, command=make_bold)
bold_button.grid(row=0, column=4, padx=(5, 5))

underline_icon = tk.PhotoImage(file="images/underline.png")
underline_button = tk.Button(top_bar, image=underline_icon, command=make_underline)
underline_button.grid(row=0, column=5, padx=(5, 5))

italic_icon = tk.PhotoImage(file="images/italic.png")
italic_button = tk.Button(top_bar, image=italic_icon, command=make_italic)
italic_button.grid(row=0, column=6, padx=(5, 5))

quote_icon = tk.PhotoImage(file="images/quote.png")
quote_button = tk.Button(top_bar, image=quote_icon, command=make_quote)
quote_button.grid(row=0, column=7, padx=(5, 5))

code_icon = tk.PhotoImage(file="images/code.png")
code_button = tk.Button(top_bar, image=code_icon, command=make_code)
code_button.grid(row=0, column=8, padx=(5, 5))

separator = tk.Label(top_bar, text=" | ", foreground="grey")
separator.grid(row=0, column=9)

link_icon = tk.PhotoImage(file="images/link.png")
link_button = tk.Button(top_bar, image=link_icon, command=make_link)
link_button.grid(row=0, column=14, padx=(5, 5))

emoji_icon = tk.PhotoImage(file="images/emoji.png")
emoji_button = tk.Button(top_bar, image=emoji_icon, command=insert_emoji)
emoji_button.grid(row=0, column=15, padx=(5, 5))

image_icon = tk.PhotoImage(file="images/image.png")
image_button = tk.Button(top_bar, image=image_icon, command=insert_image)
image_button.grid(row=0, column=16, padx=(5, 5))

separator = tk.Label(top_bar, text=" | ", foreground="grey")
separator.grid(row=0, column=17)

font_size_var = tk.StringVar()
font_size = Combobox(top_bar, textvariable=font_size_var, values=[8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72], width=3, state='readonly')
font_size.current(4)
font_size.grid(row=0, column=18, padx=(5, 5))
font_size.bind("<<ComboboxSelected>>", change_font_size)

font_families = font.families()
font_family_var = tk.StringVar()
font_type = Combobox(top_bar, textvariable=font_family_var, values=font_families, width=20, state='readonly')
font_type.current(font_families.index('Poppins'))
font_type.grid(row=0, column=19, padx=(5, 5))
font_type.bind("<<ComboboxSelected>>", change_font)

text_frame = tk.Frame(root)
text_frame.pack(fill='both', padx=80, pady=30, expand=True, side='left', anchor='nw')

# Text Box
text_box = tk.Text(text_frame, wrap='word', undo=True, font=('Helvetica', 12), padx=50, pady=50, relief='flat')
text_box.pack(fill='both', side='left', expand=True)

# Scrollbar
scroll = tk.Scrollbar(text_frame, command=text_box.yview, relief='flat')
scroll.pack(side='right', fill='y', anchor='ne')

text_box.config(yscrollcommand=scroll.set)

text_box.bind("<Control-MouseWheel>", on_ctrl_scroll)

left_align_icon = tk.PhotoImage(file="images/left-align.png")
left_align_button = tk.Button(top_bar, image=left_align_icon, command=left_align)
left_align_button.grid(row=0, column=10, padx=(5, 5))

center_align_icon = tk.PhotoImage(file="images/center-align.png")
center_align_button = tk.Button(top_bar, image=center_align_icon, command=center_align)
center_align_button.grid(row=0, column=11, padx=(5, 5))

right_align_icon = tk.PhotoImage(file="images/right-align.png")
right_align_button = tk.Button(top_bar, image=right_align_icon, command=right_align)
right_align_button.grid(row=0, column=12, padx=(5, 5))

separator = tk.Label(top_bar, text=" | ", foreground="grey")
separator.grid(row=0, column=13)
                        

root.mainloop()

