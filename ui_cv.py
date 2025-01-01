import os

# UI dosyalarının bulunduğu dizini belirtin
ui_directory = "ui"

# Python dosyalarının kaydedileceği dizini belirtin
output_directory = "ui"

# UI dosyalarını dönüştürmek için pyuic5 komutunu kullanın
for filename in os.listdir(ui_directory):
    if filename.endswith(".ui"):
        ui_file = os.path.join(ui_directory, filename)
        output_file = os.path.join(
            output_directory, os.path.splitext(filename)[0] + ".py"
        )
        os.system(f"pyuic5 {ui_file} -o {output_file}")

print("UI dosyaları dönüştürüldü.")
