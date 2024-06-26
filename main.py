import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QAbstractItemView, QVBoxLayout, QPushButton, QLabel, QLineEdit, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 1200, 700)
    win.setWindowTitle("Label maker")
    win.setWindowIcon(QIcon("icon.jpg"))

    central_widget = QWidget(win)
    win.setCentralWidget(central_widget)

    # Crear el layout principal
    main_layout = QHBoxLayout(central_widget)

    # Columna izquierda
    left_layout = QVBoxLayout()
    
    lbl_titulo = QLabel("Titulo:")
    left_layout.addWidget(lbl_titulo)
    
    txt_titulo = QLineEdit()
    txt_titulo.setFixedHeight(45)
    txt_titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
    left_layout.addWidget(txt_titulo)

    lbl_lote = QLabel("Lote:")
    left_layout.addWidget(lbl_lote)
    
    txt_lote = QLineEdit()
    left_layout.addWidget(txt_lote)

    lbl_fecha = QLabel("Fecha:")
    left_layout.addWidget(lbl_fecha)
    
    txt_fecha = QLineEdit()
    left_layout.addWidget(txt_fecha)

    lbl_kgs = QLabel("Kgs:")
    left_layout.addWidget(lbl_kgs)
    
    txt_kgs = QLineEdit()
    left_layout.addWidget(txt_kgs)

    # Añadir txt_contiene (selector múltiple)
    lbl_contiene_text = "Contiene:"
    lbl_contiene = QLabel(lbl_contiene_text)
    left_layout.addWidget(lbl_contiene)

    txt_contiene = QListWidget()
    txt_contiene.setSelectionMode(QAbstractItemView.MultiSelection)
    txt_contiene.setMaximumHeight(100)
    
    contiene_items = ["Componente 1", "Componente 2", "Componente 3", "Componente 4", "Componente 5"]
    for contiene_item in contiene_items:
        contiene_list_item = QListWidgetItem(contiene_item)
        txt_contiene.addItem(contiene_list_item)
    
    left_layout.addWidget(txt_contiene)

    # Añadir txt_UNnumber (campo de texto)
    lbl_UNnumber_text = "UN Number:"
    lbl_UNnumber = QLabel(lbl_UNnumber_text)
    left_layout.addWidget(lbl_UNnumber)

    txt_UNnumber = QLineEdit()
    left_layout.addWidget(txt_UNnumber)

    # Columna derecha
    right_layout = QVBoxLayout()
    
    lbl_precauciones_text = "Precauciones:"
    lbl_precauciones = QLabel(lbl_precauciones_text)
    right_layout.addWidget(lbl_precauciones)

    txt_precauciones = QListWidget()
    txt_precauciones.setSelectionMode(QAbstractItemView.MultiSelection)
    
    items = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
    for item in items:
        list_item = QListWidgetItem(item)
        txt_precauciones.addItem(list_item)
    
    right_layout.addWidget(txt_precauciones)

    # Añadir segundo selector múltiple para imágenes
    lbl_img_text = "Imágenes:"
    lbl_img = QLabel(lbl_img_text)
    right_layout.addWidget(lbl_img)

    txt_img = QListWidget()
    txt_img.setSelectionMode(QAbstractItemView.MultiSelection)
    
    img_items = ["Imagen 1", "Imagen 2", "Imagen 3", "Imagen 4", "Imagen 5"]
    for img_item in img_items:
        img_list_item = QListWidgetItem(img_item)
        txt_img.addItem(img_list_item)
    
    right_layout.addWidget(txt_img)




    
    # LOGICA--------------------------------------------------------------------------------------------------------------------

    def clicked(parent):
        print("button clicked")
        
        #doc = Document()
        
        #p = doc.add_paragraph()
        #r = p.add_run()
        #r.add_text('Good Morning every body,This is my ')
        #r.add_picture('icon.jpg',width=Inches(4.0), height=Inches(.7))
        #r.add_text(' do you like it?')
        #p1 = doc.add_paragraph("First Paragraph.")
        #p2 = doc.add_paragraph("Second Paragraph.")

        #table = doc.add_table(rows=3, cols=2)
        #table.cell(0,0).text = "0,0"
        #table.cell(0,1).text = "0,1"
        #table.cell(1,0).text = "1,0"
        #table.cell(1,1).text = "1,1"
        #doc.save('tabletest.docx')

        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Information)
        msg.setText("Datos guardados correctamente.")
        msg.setWindowTitle("Guardar")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        

        
    def loadClicked():
        print("load clicked")
        #print(txt_titulo.text() + " " + txt_lote.text())
        document = Document("og.docx")
        #document.paragraphs[0].text = "YEAH"
        #print(document.paragraphs[0].text)
        #fullText = []
        #for para in document.paragraphs:
        #    print("hi")
        #    fullText.append(para.text)
        #print('\n'.join(fullText))
        table = document.tables[0]

        titlerun = table.cell(1,0).add_paragraph().add_run()
        font = titlerun.font
        font.name = "Arial Black"
        font.size = Pt(18)
        titlerun.add_text(txt_titulo.text())

        # second part
        titlerun2 = table.cell(1,0).add_paragraph().add_run()
        font2 = titlerun2.font
        font2.name = "Arial"
        font2.size = Pt(7)
        titlerun2.add_text(txt_lote.text())
        print("done")

        document.save("out.docx")


        # Añadir botones Save y Load a la columna izquierda
    btn_save = QPushButton("Save")
    btn_save.clicked.connect(lambda: clicked(win))
    left_layout.addWidget(btn_save)

    btn_load = QPushButton("Load")
    btn_load.clicked.connect(loadClicked)
    left_layout.addWidget(btn_load)

        # Agregar los layouts izquierdo y derecho al layout principal
    main_layout.addLayout(left_layout)
    main_layout.addLayout(right_layout)

    win.show()
    sys.exit(app.exec_())
    


window()