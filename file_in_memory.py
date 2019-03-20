import io
from PIL import Image
import img2pdf
import base64
import zipfile


# Imagem tif em bytes
name_img = 'EXEMPLO_TIF.tif'
varbinary = io.open(name_img, 'rb').read()

# Convertendo para BytesIO para a leitura de seus metadados
image_data = Image.open(io.BytesIO(varbinary))
num_pages = image_data.n_frames

# Imprimindo o número  de páginas
print('NUMERO DE PAGINAS: ', num_pages)

# Convertendo o arquivo tif em PDF
convert_pdf = img2pdf.convert(varbinary)

zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
    for file_name, data in [('1.pdf', io.BytesIO(convert_pdf))]:
        zip_file.writestr(file_name, data.getvalue())
# Imprime o zip em bytes
print(zip_buffer.getvalue())

# Para salvar o arquivo localmente
# with open('1.zip', 'wb') as f:
#    f.write(zip_buffer.getvalue())

zip_base64 = base64.encodebytes(zip_buffer.getvalue())
print(zip_base64)