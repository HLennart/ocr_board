import winclip32
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from PIL import ImageGrab
import tempfile


# get our image from the clipboard
img = ImageGrab.grabclipboard()
if not img: 
    raise IOError('no image in clipboard ¯\_(ツ)_/¯')
# if we found a image get the text from it and put it back into the clipboard

# Create a directory that kills itself later => when exactly actually ? :shrug: TODO
temp_directory = tempfile.TemporaryDirectory()
# Create a path for our temporarily existing image
temp_location = temp_directory.name + '/tempfile'
# Then we save our image in that temporary folder
img.save(temp_location,'PNG')
# here we set our tesseract.exe path => TODO add that shit to our exe

pytesseract.pytesseract.tesseract_cmd = r"tesseract.exe"
# use tesseract to get the text from our image and store it    
interpreted_text = pytesseract.image_to_string(temp_location)
# winclip32.UNICODE_STD_TEXT is the textformat in which our text is stored back into the clipboard
object_format_output = winclip32.UNICODE_STD_TEXT

winclip32.set_clipboard_data(object_format_output, interpreted_text)

print(interpreted_text)

    