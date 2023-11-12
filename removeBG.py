from rembg import remove
from PIL import Image
input_path ='ps.jpg' 
output_path ='ps.png' 
input = Image.open(input_path)
output = remove(input)
output.save(out_path)
