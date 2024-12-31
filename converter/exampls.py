

# def upload_jpg(file, format):
#     """
#     This function converts the `.jpg` and `.jpeg` files into one `.pdf` file.
#     """
#     pdfFile = None
#     merger = PdfMerger()

#     # print(f"Number of files: {len(files)}")
#     # for file in files:
#         # print(file)
#     # print(f"Number of formats: {len(formats)}")

#     # for file, format in zip(files, formats):

#     filename = file.name
#     name, _ = os.path.splitext(filename)

#     try:
#         image = Image.open(file)
#         image.verify() # verify that the image is valid
#         print(f"Valid image formart: {image.format}")
        
#         if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
#             image.load()
#             background = Image.new("RGB", image.size, (255, 255, 255))
#             background.paste(image, mask=image.split()[3])
#             image = background
        
#          # Create a temporary file with a unique name and Save the image as a temporary PDF file.  Add the temporary PDF file to the merger
#         with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp:
#             image.save(temp.name, 'PDF', encoding='latin-1')
#             merger.append(temp.name)
#     except Exception as e:
#         print(f"Error: {e}")


#     # Save the merged PDF file
#     format = format.lower()
#     pdfFile = f"{name}.{format}"
#     # pdfFile = 'output.pdf'
#     merger.write(pdfFile)
#     merger.close()
#     return pdfFile      
#File(open(pdfFile, 'rb'), name=pdfFile)