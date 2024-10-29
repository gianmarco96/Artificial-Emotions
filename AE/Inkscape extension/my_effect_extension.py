# import inkex
# import os

# class ImportExtension(inkex.EffectExtension):
#     def add_arguments(self, pars):
#         pars.add_argument("--import-file", type=str, help="Path to the file to import")

#     def effect(self):
#         import_file = self.options.import_file
#         if not os.path.exists(import_file):
#             inkex.errormsg(f"The file {import_file} does not exist.")
#             return

#         file_ext = os.path.splitext(import_file)[1].lower()

#         if file_ext == '.svg':
#             self.import_svg(import_file)
#         else:
#             inkex.errormsg(f"Unsupported file type: {file_ext}")

#     def import_svg(self, import_file):
#         # Load the SVG file content
#         # svg = inkex.EffectElement.parse(import_file)
#         svg = inkex.load_svg(import_file)
        
#         # Insert the imported SVG into the current document
#         self.document.getroot().append(svg.getroot())
        
#         inkex.utils.debug(f"Successfully imported {import_file}")

# if __name__ == '__main__':
#     ImportExtension().run()

import inkex
import os
import base64

class ImportExtension(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--import-file", type=str, help="Path to the file to import")

    def effect(self):
        import_file = self.options.import_file
        
        folder_path = "C:\\Users\\amrcmeu\\Documents\\AE\\appScripts\\static\\imgs"
        
        #List all items in the specified folder
        imgs = os.listdir(folder_path)
        
        #Count the number of items
        num_imgs = len(imgs)
        if num_imgs < 100:
            import_file = folder_path + "\\img_" + str(num_imgs) + ".PNG"
        elif num_imgs < 1000 and num_imgs > 99:
            import_file = folder_path + "\\img_h" + str(num_imgs) + ".PNG"
        else:
            import_file = folder_path + "\\img_t" + str(num_imgs) + ".PNG"
            

        # Can delete below!!!!!
        if not os.path.exists(import_file):
            inkex.errormsg(f"The file {import_file} does not exist.")
            return

        file_ext = os.path.splitext(import_file)[1].lower()

        if file_ext == '.svg':
            self.import_svg(import_file)
        elif file_ext in ['.png', '.jpg', '.jpeg']:
            self.embed_image(import_file)
        else:
            inkex.errormsg(f"Unsupported file type: {file_ext}")

    def import_svg(self, import_file):
        # Load the SVG file content
        svg = inkex.load_svg(import_file)
        
        # Insert the imported SVG into the current document
        self.document.getroot().append(svg.getroot())
        
        inkex.utils.debug(f"Successfully imported {import_file}")

    def embed_image(self, import_file):
        # Read the image file and encode it as base64
        with open(import_file, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

        # Determine the MIME type
        mime_type = "image/png" if import_file.endswith(".png") else "image/jpeg"

        # Create a new image element and embed the image data
        image = inkex.Image()
        image.set('x', '15.5')
        image.set('y', '58')
        image.set('width', 180)
        image.set('height', 180)
        image.set('xlink:href', f"data:{mime_type};base64,{encoded_image}")

        #  # Append the image to the current layer
        # layer.append(elem)

        # Insert the image into the current document
        self.document.getroot().append(image)

        #inkex.utils.debug(f"Successfully embedded {import_file}")

if __name__ == '__main__':
    ImportExtension().run()
