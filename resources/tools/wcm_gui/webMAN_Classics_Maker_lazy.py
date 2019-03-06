import json

from Tkinter import *
from tkFont import Font

from PIL import Image
from PIL.ImageTk import PhotoImage
from PIL import ImageDraw
from PIL import ImageFont




class Main():

	def __init__(self, main):

		# canvas for image
		self.canvas = Canvas(main, width=canvas_width, height=canvas_height, borderwidth=0, highlightthickness=0)
		self.canvas.pack(fill=BOTH, expand=YES)

		self.vcmd = main.register(self.validate)
		self.vcmd2 = main.register(self.validate)
		self.maxlength = 8

		# setting defaults
		self.state_drive_choice		= 'dev_hdd0'
		self.state_system_choice	= 'PS2'
		self.entry_field_iso_path 	= None


		# images
		self.logo_drives = []
		self.logo_drives.append(PhotoImage(Image.open("logo_drive_hdd.gif")))
		self.logo_drives.append(PhotoImage(Image.open('logo_drive_usb.gif')))

		self.logo_systems = []
		self.logo_systems.append(PhotoImage(Image.open('logo_system_PSP.gif')))
		self.logo_systems.append(PhotoImage(Image.open('logo_system_PSX.gif')))
		self.logo_systems.append(PhotoImage(Image.open('logo_system_PS2.gif')))
		self.logo_systems.append(PhotoImage(Image.open('logo_system_PS3.gif')))

		self.background_images = []
		self.background_images.append(Image.open('background_light_dark_1920_1080.png'))
		self.background_images.append(Image.open('background_mod.png'))
		self.background_images.append(Image.open('background_mod_2.png'))
		self.background_images.append(Image.open('background_mod_3.png'))
		self.background_images.append(Image.open('background_mod_3_blur.png'))
		self.background_images.append(Image.open('background_dark_1920_1080.gif'))
		self.background_images.append(Image.open('background_light_1920_1080.gif'))
		self.background_images.append(Image.open('background_dark_blue_symbols_1920_1080.gif'))
		self.background_images.append(Image.open('background_light_blue_waves_1920_1080.gif'))
		self.background_images.append(Image.open('background_light_blue_symbols_1920_1080.gif'))

		self.image_xmb_icons = Image.open('XMB_icons.png')

		self.image_pic1		= Image.open('../../pkg/PIC1.PNG')
		self.image_pic0		= Image.open('../../pkg/PIC0.PNG')
		self.image_icon0	= Image.open('../../pkg/ICON0.PNG')
		self.image_icon0_crop 	= self.image_icon0.crop((10, 10, self.image_icon0.width - 10, self.image_icon0.height - 10))
		self.ps3_system_logo = Image.open('./ps3_type_logo.png')

		pic1_x_scale		= 1280.0/self.image_pic1.width * scaling
		pic1_y_scale		= 720.0/self.image_pic1.height * scaling
		self.pic0_dimensions 	= (int(pic1_x_scale * self.image_pic0.width), int(pic1_y_scale * self.image_pic0.height))
		self.icon0_dimensions 	= (int(pic1_x_scale * self.image_icon0.width), int(pic1_y_scale * self.image_icon0.height))

		self.pkg_images_img = []
		self.pkg_images_img.append(self.image_pic0)
		self.pkg_images_img.append(self.image_pic1)
		self.pkg_images_img.append(self.image_icon0_crop)


		game_title_test_text = 'Burnout Revenge'
		text_color = 'white'
		game_text_x = 760
		game_text_y = 490
		text_size = 32
		self.draw_text_on_image(self.image_pic1, game_title_test_text, game_text_x, game_text_y, text_size, text_color)

		self.image_pic1.paste(self.image_xmb_icons, (0, 0), self.image_xmb_icons)
		self.image_pic1.paste(self.ps3_system_logo, (1180, 525), self.ps3_system_logo)


		# init defintions
		self.init_main_window_buttons(main)
		self.init_param_sfo_labels(main)

	def init_param_sfo_labels(self, main):
		# Constants
		self.text_title_id	= 'Title id'
		self.text_title 	= 'Title'
		self.text_filename	= 'Filename'
		self.text_iso_path	= 'Path'


		# paddings
		self.height_of_text = 15 #Font(font='Helvetica').metrics('linespace')
		print('self.height_of_text' + str(self.height_of_text))

		self.dark_side_padding = 20
		self.text_box_spacing = 8 * self.dark_side_padding

		# coordinates
		self.main_offset_x_pos = 1400
		self.main_offset_y_pos = 150

		self.title_id_text_x_pos = self.main_offset_x_pos
		self.title_id_text_y_pos = self.main_offset_y_pos + self.height_of_text / 2

		self.title_text_x_pos = self.main_offset_x_pos
		self.title_text_y_pos = self.dark_side_padding + self.title_id_text_y_pos + self.height_of_text

		self.filename_text_x_pos = self.main_offset_x_pos
		self.filename_text_y_pos = self.dark_side_padding + self.title_text_y_pos + self.height_of_text

		self.iso_path_text_x_pos = self.main_offset_x_pos
		self.iso_path_text_y_pos = self.dark_side_padding + self.filename_text_y_pos + self.height_of_text

		self.my_image_number = 0
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_title_id.upper(), 	self.title_id_text_x_pos,	self.title_id_text_y_pos,	25, 'white')
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_title.upper(), 	self.title_text_x_pos,		self.title_text_y_pos, 		25, 'white')
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_filename.upper(), 	self.filename_text_x_pos,	self.filename_text_y_pos,	25, 'white')
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_iso_path.upper(), 	self.iso_path_text_x_pos,	self.iso_path_text_y_pos,	25, 'white')
		self.current_img = self.background_images[self.my_image_number]
		self.current_img = self.background_images[0]
		self.current_img = self.current_img.resize((int(1920 * scaling), int(1080 * scaling)), Image.ANTIALIAS)
		self.current_background = PhotoImage(self.current_img)

		self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.current_background)


		# defintions
		self.entry_field_title_id	= Entry(main, validate='key', validatecommand=(self.vcmd, '%P'))
		self.entry_field_title		= Entry(main)
		self.entry_field_filename 	= Entry(main)
		self.entry_field_iso_path	= Entry(main, state='disabled')


		# system choice buttons
		self.selection_drive_list	= ['dev_hdd0', 'dev_hdd1', 'dev_usb000']	# usb port 'x' should be selected through a list
		self.selection_system_list	= ['PSP', 'PSX', 'PS2', 'PS3']
		self.drive_path 			= self.selection_drive_list[0] 				# drive should be toggled by buttons

		self.button_HDD 	= Button(main, image=self.logo_drives[0], bd=1, command=lambda: self.on_drive_system_filename_choice_button(self.selection_drive_list[0], self.state_system_choice))
		self.button_USB 	= Button(main, image=self.logo_drives[1], bd=1, command=lambda: self.on_drive_system_filename_choice_button(self.selection_drive_list[2], self.state_system_choice))

		self.button_PSP 	= Button(main, image=self.logo_systems[0], bd=1, command=lambda: self.on_drive_system_filename_choice_button(self.state_drive_choice, self.selection_system_list[0]))
		self.button_PSX 	= Button(main, image=self.logo_systems[1], bd=1, command=lambda: self.on_drive_system_filename_choice_button(self.state_drive_choice, self.selection_system_list[1]))
		self.button_PS2 	= Button(main, image=self.logo_systems[2], bd=1, command=lambda: self.on_drive_system_filename_choice_button(self.state_drive_choice, self.selection_system_list[2]))
		self.button_PS3 	= Button(main, image=self.logo_systems[3], bd=1, command=lambda: self.on_drive_system_filename_choice_button(self.state_drive_choice, self.selection_system_list[3]))


		self.save_button = Button(main, text="Save", command=self.on_save_button, bd=1, bg="#FBFCFB")

		# Placements
		self.entry_field_title_id.place(x=int((self.text_box_spacing + self.iso_path_text_x_pos) * scaling), y=int(self.title_id_text_y_pos	* scaling)	, width=200)
		self.entry_field_title.place(	x=int((self.text_box_spacing + self.iso_path_text_x_pos) * scaling), y=int(self.title_text_y_pos	* scaling)	, width=200)
		self.entry_field_filename.place(x=int((self.text_box_spacing + self.iso_path_text_x_pos) * scaling), y=int(self.filename_text_y_pos	* scaling)	, width=200)
		self.entry_field_iso_path.place(x=int((self.text_box_spacing + self.iso_path_text_x_pos) * scaling), y=int(self.iso_path_text_y_pos	* scaling)	, width=200)

		self.button_HDD.place(x=int((self.main_offset_x_pos + 0 * 29) * scaling), y=int(self.main_offset_y_pos - 120))
		self.button_USB.place(x=int((self.main_offset_x_pos + 3 * 29) * scaling), y=int(self.main_offset_y_pos - 120))

		self.button_PSP.place(x=int((self.main_offset_x_pos + 0 * 29) * scaling), y=int(self.main_offset_y_pos - 80))
		self.button_PSX.place(x=int((self.main_offset_x_pos + 3 * 29) * scaling), y=int(self.main_offset_y_pos - 80))
		self.button_PS2.place(x=int((self.main_offset_x_pos + 6 * 29) * scaling), y=int(self.main_offset_y_pos - 80))
		self.button_PS3.place(x=int((self.main_offset_x_pos + 9 * 29) * scaling), y=int(self.main_offset_y_pos - 80))

		self.img_pic1 = self.pkg_images_img[1]
		self.img_pic1 = self.img_pic1.resize((int(1280 * scaling), int(720 * scaling)), Image.ANTIALIAS)

		self.img_pic1 = PhotoImage(self.img_pic1)
		self.pkg_pic1	= Button(main, image=self.img_pic1, highlightthickness=0, bd=0)
		self.pkg_pic1.place(x=10 * scaling, y=245 * scaling)

		self.icon0 = self.pkg_images_img[2]
		self.icon0 = PhotoImage(self.icon0.resize(self.icon0_dimensions, Image.ANTIALIAS))
		self.pkg_icon0		= Button(main, image=self.icon0, highlightthickness = 0, bd=0)

		self.pkg_icon0.place(x=int(285 * scaling), y=int(530 * scaling))


		icon_img = Image.open('../../pkg/ICON0.PNG')
		self.image_pic1.paste(icon_img, (425, 450), icon_img)
		self.image_pic1.save('test.png')

		self.save_button.place(x=self.text_box_spacing + self.iso_path_text_x_pos, y=self.iso_path_text_y_pos + 40)

		####################################################################
		# Adding an onChange -listener on 'entry_field_filename'
		self.generateOnChange(self.entry_field_filename)
		self.entry_field_filename.bind('<<Change>>', self.onEntryChanged)
		####################################################################


	def draw_text_on_image(self, image, text, text_x, text_y, text_size, text_color):
		font = ImageFont.truetype('./fonts/SCE-PS3.ttf', text_size)
		draw = ImageDraw.Draw(image)
		if text_color == None:
			text_outline = 'white'
		return draw.text((text_x, text_y), text, fill=text_color, font=font)

	def draw_text_on_image_w_shadow(self, image, text, text_x, text_y, text_size, text_outline, text_color, shadow_color):
		font = ImageFont.truetype('./fonts/SCE-PS3.ttf', text_size)
		if text_outline == None:
			text_outline = 2
		if text_color == None:
			text_outline = 'white'
		if shadow_color == None:
			shadow_color = 'black'

		draw = ImageDraw.Draw(image)
		for adj in range(text_outline):
			# move right
			draw.text((text_x - adj, text_y), text, font=font, fill=shadow_color)
			# move left
			draw.text((text_x + adj, text_y), text, font=font, fill=shadow_color)
			# move up
			draw.text((text_x, text_y + adj), text, font=font, fill=shadow_color)
			# move down
			draw.text((text_x, text_y - adj), text, font=font, fill=shadow_color)
			# diagnal left up
			draw.text((text_x - adj, text_y + adj), text, font=font, fill=shadow_color)
			# diagnal right up
			draw.text((text_x + adj, text_y + adj), text, font=font, fill=shadow_color)
			# diagnal left down
			draw.text((text_x - adj, text_y - adj), text, font=font, fill=shadow_color)
			# diagnal right down
			draw.text((text_x + adj, text_y - adj), text, font=font, fill=shadow_color)
		return draw.text((text_x, text_y), text, fill=text_color, font=font)



	def init_main_window_buttons(self, main):
		# button to quit
		self.quit_button = Button(main, text="Quit", command=main.quit, bd=1, bg="#FBFCFB")
		self.quit_button.place(x=0, y=0)
		self.quit_button.config(height=1, width=3)

		# button to change image
		self.change_button = Button(main, text="Change", command=self.on_change_button, bd=1, bg="#FBFCFB")
		self.change_button.place(x=45, y=0)

	def on_change_button(self):
		# next image
		self.my_image_number += 1

		print('on change')

		# return to first image
		if self.my_image_number == len(self.background_images):
			self.my_image_number = 0

		# change image
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_title_id,	self.title_id_text_x_pos, 	self.title_id_text_y_pos, 25, 'white')
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_title,		self.title_text_x_pos, 		self.title_text_y_pos, 25, 'white')
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_filename,	self.filename_text_x_pos, 	self.filename_text_y_pos, 25, 'white')
		self.draw_text_on_image(self.background_images[self.my_image_number], self.text_iso_path,	self.iso_path_text_x_pos, 	self.iso_path_text_y_pos, 25, 'white')
		self.current_background = PhotoImage(self.background_images[self.my_image_number])

		self.canvas.itemconfig(self.image_on_canvas, image=self.current_background)

	def on_drive_system_filename_choice_button(self, drive_choice, system_choice):
		current_iso_path 	= self.entry_field_iso_path.get()
		print('DEBUG system_choice: ' + system_choice)
		print('DEBUG drive_choice: ' + drive_choice)

		# If path is empty -> setting default values
		if current_iso_path is '':
			print('DEBUG Path is empty -> setting default values')
			self.state_drive_choice	= drive_choice
			self.state_system_choice = system_choice

			current_iso_path = '/' + self.state_drive_choice + '/' + self.state_system_choice + '/' + self.entry_field_filename.get()
			self.entry_field_iso_path.config(state=NORMAL)
			self.entry_field_iso_path.delete(0, END)
			self.entry_field_iso_path.insert(0, current_iso_path)
			self.entry_field_iso_path.config(state=DISABLED)
			print('DEBUG Default path set -> ' + self.entry_field_iso_path.get())

		# Check if drive of choice already set
		if drive_choice is self.state_drive_choice:
			print('DEBUG ' + '\'' + drive_choice + '\'' + ' already set')
		# Check if system of choice already set
		if system_choice is self.state_system_choice:
			print('DEBUG ' + '\'' + system_choice + '\'' + ' already set')


		# Replace current drive
		if drive_choice not in current_iso_path:
			print('DEBUG drive_choice not in current_iso_path')
			print('DEBUG ' + '\'' + self.state_drive_choice + '\'' + ' changed -> ' + '\'' + drive_choice + '\'')
			current_iso_path = current_iso_path.replace(self.state_drive_choice, drive_choice)
			self.entry_field_iso_path.config(state=NORMAL)
			self.entry_field_iso_path.delete(0, END)
			self.entry_field_iso_path.insert(0, current_iso_path)
			self.entry_field_iso_path.config(state=DISABLED)
			self.state_drive_choice = drive_choice

		# Replace current system
		if system_choice not in current_iso_path:
			print('DEBUG drive_choice not in current_iso_path')
			print('DEBUG ' + '\'' + self.state_system_choice + '\'' + ' changed -> ' + '\'' + system_choice + '\'')
			current_iso_path = current_iso_path.replace(self.state_system_choice, system_choice)
			self.entry_field_iso_path.config(state=NORMAL)
			self.entry_field_iso_path.delete(0, END)
			self.entry_field_iso_path.insert(0, current_iso_path)
			self.entry_field_iso_path.config(state=DISABLED)
			self.state_system_choice = system_choice



	def on_save_button(self):
		# do stuff
		self.validate_title_id()

		self.save_pkg_info_to_json()

	def save_pkg_info_to_json(self):
		with open('../util_resources/params.json.BAK') as f:
			json_data = json.load(f)

		try:
			json_data['title']=str(self.entry_field_title.get())
			json_data['title_id']=self.entry_field_title_id.get()
			json_data['content_id']='UP0001-'+ self.entry_field_title_id.get() + '_00-0000000000000000'
			json_data['iso_filepath']=str(self.entry_field_iso_path.get())

			newFile = open("../util_generated_files/webman_classics_pkg.json", "w")
			json_text = json.dumps(json_data, indent=4, separators=(",", ":"))
			newFile.write(json_text)

		except ValueError:
			print('File write error/PKGLAUNCH not found/titel_id not a string')

	# Ensure title_id doesn't exceed 8 characters
	def validate(self, P):
		if len(P) > self.maxlength:
			# re-activates listener
			main_window.after_idle(lambda: self.entry_field_title_id.config(validate='key'))
			return None  # new value too long
		else:
			print('DEBUG Title ID: ' + P)
			return True

	# Ensures title id is exactly 8 characters during save
	def validate_title_id(self):
		title_id = self.entry_field_title_id.get().upper()
		if len(title_id) < self.maxlength:
			title_id = title_id + 'XXXXXXXX'
			title_id = title_id[0:self.maxlength]

		self.entry_field_title_id.delete(0, END)
		self.entry_field_title_id.insert(0, title_id)



	# Dynamic update of the 'entry_field_filename' into the 'entry_field_iso_path'
	def onEntryChanged(self, event):
		drive = ''
		system = ''
		filename = event.widget.get()

		if self.state_drive_choice is not '':
			drive = '/' + self.state_drive_choice + '/'
		if self.state_drive_choice is not '':
			system = '/' + self.state_system_choice + '/'

		iso_path = drive + system + filename
		iso_path = iso_path.replace('//', '/')

		self.entry_field_iso_path.config(state=NORMAL)
		self.entry_field_iso_path.delete(0, END)
		self.entry_field_iso_path.insert(0, iso_path)
		self.entry_field_iso_path.config(state=DISABLED)

		current_filename = self.entry_field_iso_path.get()
		print("entry_field_iso_path: " + current_filename)

	def generateOnChange(self, obj):
		obj.tk.eval('''
				proc widget_proxy {widget widget_command args} {

					# call the real tk widget command with the real args
					set result [uplevel [linsert $args 0 $widget_command]]

					# generate the event for certain types of commands
					if {([lindex $args 0] in {insert replace delete}) ||
						([lrange $args 0 2] == {mark set insert}) || 
						([lrange $args 0 1] == {xview moveto}) ||
						([lrange $args 0 1] == {xview scroll}) ||
						([lrange $args 0 1] == {yview moveto}) ||
						([lrange $args 0 1] == {yview scroll})} {

						event generate  $widget <<Change>> -when tail
					}

					# return the result from the real widget command
					return $result
				}
				''')
		obj.tk.eval('''
				rename {widget} _{widget}
				interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
			'''.format(widget=str(obj)))

def dpi_awerness():
	if 'linux' not in sys.platform:
		import ctypes
		# Query DPI Awareness (Windows 10 and 8)
		awareness = ctypes.c_int()
		errorCode = ctypes.windll.shcore.GetProcessDpiAwareness(0, ctypes.byref(awareness))
		print(awareness.value)

		# Set DPI Awareness  (Windows 10 and 8)
		errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(4)
		# the argument is the awareness level, which can be 0, 1 or 2:
		# for 1-to-1 pixel control I seem to need it to be non-zero (I'm using level 2)

		# Set DPI Awareness  (Windows 7 and Vista)
		success = ctypes.windll.user32.SetProcessDPIAware()

		# behaviour on later OSes is undefined, although when I run it on my Windows 10 machine, it seems to work with effects identical to SetProcessDpiAwareness(1)


main_window = Tk()
main_window.resizable(0, 0)
main_window.geometry("+%d+%d" % (0, 0))
# changing the title of our master widget
main_window.title('webMAN Classics Maker UI')
# icon upper left corner

if "linux" in sys.platform:
	main_window.iconbitmap('@../../images/webman_icon.xbm')
	# scaling = 1
	scaling = 1280.0 / 1920.0

else:
	print('not linux')
	main_window.iconbitmap('../../images/webman.ico')
	# scaling = 1
	scaling = 1280.0 / 1920.0


canvas_width = int(1920* scaling)
canvas_height = int(1080* scaling)
main_window_width = int(1920* scaling)
main_window_height = int(1080* scaling)




Main(main_window)

main_window.mainloop()
