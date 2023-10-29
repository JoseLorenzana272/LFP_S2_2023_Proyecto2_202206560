
from jinja2 import Template
import customtkinter
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
from graphviz import Digraph
from Lexico import *
from Sintactico import *
import subprocess
from deep_translator import GoogleTranslator
from Lexico import instruccion, lista_lexemas

traductor = GoogleTranslator(source='en', target='es')
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Analizador Léxico')
        self.geometry(f"{1300}x{590}")
        self.file_name = None

        # Ventana
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # Panel Superior
        self.top_frame = customtkinter.CTkFrame(self, height=60)
        self.top_frame.pack(side='top', fill='x')

        original_image = Image.open("img/icons8-dragon-ball-legends-200.png")
        resized_image = original_image.resize((600, 300))  # Cambia el tamaño a 300x300

        # Label Espacio
        img = customtkinter.CTkImage(dark_image=resized_image)
        self.labelespacio = customtkinter.CTkLabel(self.top_frame, text='Proyecto 2 - 202206560', font=('Poppins', 20),
                                                   image=img, compound='right')
        self.labelespacio.pack(side='left', fill='both', expand=True)



        #img abrir
        img = customtkinter.CTkImage(dark_image=Image.open("img/icons8-enlace-externo-48.png"))

        # Botón Abrir
        self.open_button = customtkinter.CTkButton(self.top_frame, text='Abrir   ', width=120, fg_color='#158f00', hover_color='#0c4f00', command=self.abrir_archivo, image=img, compound='left')
        self.open_button.pack(side='left', padx=10, pady=10)

        #img analizarah bien

        img = customtkinter.CTkImage(dark_image=Image.open("img/icons8-analyse-48.png"))

        # Botón Analizar
        self.analize_button = customtkinter.CTkButton(self.top_frame, text='Analizar', width=120, fg_color='#158f00', hover_color='#0c4f00', image=img, compound='left', command=self.analizar)
        self.analize_button.pack(side='left', padx=10, pady=10)

        # img logo
        img = customtkinter.CTkImage(dark_image=Image.open("img/icons8-reports-58.png"))
        self.labelImg = customtkinter.CTkLabel(self.top_frame, image=img, text='')
        self.labelImg.pack(side='left', padx=10, pady=10)

        # ComBox Archivo
        opciones = ['Reporte de Errores', 'Reporte de Tokens', 'Árbol de Derivación']
        self.file_combobox = customtkinter.CTkComboBox(self.top_frame, width=150, values=opciones, state='readonly', command=self.sobre_combobox)
        self.file_combobox.pack(side='left', padx=10, pady=10)
        self.file_combobox.set('Reportes')

        #img salir
        self.img = customtkinter.CTkImage(dark_image=Image.open("img/icons8-salida-50.png"))

        # Botón Salir
        self.exit_button = customtkinter.CTkButton(self.top_frame, text='Salir    ', width=120, hover_color='#420105', command=self.salir, image=self.img, compound='left')
        self.exit_button.pack(side='left', padx=10, pady=10)
        self.exit_button.configure(fg_color='#810a0a')

        # Panel Texto Centrado
        self.center_frame = customtkinter.CTkFrame(self, width=800, height=500)
        self.center_frame.pack(anchor="center", padx=10, pady=50)

        self.label_vacio = customtkinter.CTkLabel(self.center_frame, text=' ', font=('Courier New', 13))
        self.label_vacio.pack(side='left', fill='both', expand=True)

        # Canvas que muestre los núemros de línea
        self.line_number_canvas = customtkinter.CTkCanvas(self.center_frame, width=35, bg='#323332')
        self.line_number_canvas.pack(side='left', fill='y')
        self.line_number_canvas.configure(highlightthickness=0)


        # Area de Texto
        self.text_area = customtkinter.CTkTextbox(self.center_frame, width=600, height=650, font=('Courier New', 13))
        self.text_area.pack(side='left', fill='both', expand=True, padx=(0, 100))  # Agrega espacio a la derecha

        self.text_area.bind("<Key>", self.update_line_numbers)
        self.text_area.bind("<MouseWheel>", self.update_line_numbers)
        self.text_area.bind("<Button-4>", self.update_line_numbers)
        self.text_area.bind("<Button-5>", self.update_line_numbers)

        # Canvas que muestre '>>>'
        self.prompt_canvas = customtkinter.CTkCanvas(self.center_frame, width=35, bg='#323332')
        self.prompt_canvas.pack(side='left', fill='y')
        self.prompt_canvas.configure(highlightthickness=0)

        # Area de Texto
        self.text_area2 = customtkinter.CTkTextbox(self.center_frame, width=500, height=650, font=('Courier New', 12))
        self.text_area2.pack(side='left', fill='both', expand=True)

        def update_prompts(event=None):
            self.prompt_canvas.delete("all")
            i = self.text_area2.index("@0,0")
            while True:
                dline = self.text_area2.dlineinfo(i)
                if dline is None:
                    break
                y = dline[1]
                line_height = dline[3]
                y += line_height // 2  # Ajusta la posición vertical
                self.prompt_canvas.create_text(2, y, anchor="nw", text='>>>', font=('Courier New', 11), fill='white')
                i = self.text_area2.index(f"{i}+1line")

        self.text_area2.bind('<KeyRelease>', update_prompts)
        self.text_area2.bind("<Key>", update_prompts)
        self.text_area2.bind("<MouseWheel>", update_prompts)
        self.text_area2.bind("<Button-4>", update_prompts)
        self.text_area2.bind("<Button-5>", update_prompts)

    def update_line_numbers(self, event=None):
        self.line_number_canvas.delete("all")
        i = self.text_area.index("@0,0")
        while True:
            dline = self.text_area.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            line_height = dline[3]
            y += line_height // 2  # Ajusta la posición vertical
            self.line_number_canvas.create_text(2, y, anchor="nw", text=i.split(".")[0], font=('Courier New', 11),
                                                fill='white')
            i = self.text_area.index(f"{i}+1line")



    def salir(self):
        self.destroy()

    def abrir_archivo(self):
        print('Abrir')
        try:
            self.file_name = filedialog.askopenfilename(filetypes=[("BizData Files", "*.bizdata")])
            with open(self.file_name, "r", encoding='UTF-8') as file:
                content = file.read()
                self.text_area.insert('1.0', content)
        except Exception as e:
            messagebox.showinfo('Error', 'Hubo un error al intentar abrir el archivo', icon='error')

    def analizar(self):
        code = self.text_area.get("1.0", "end-1c")
        imprimir_consola = ''
        try:
            # Ejecuta el análisis léxico
            instrucciones_lexico = instruccion(code)
            lista_instrucciones = []
            while True:
                instrucciones_lenguaje = instrucciones_sintactico(instrucciones_lexico)
                if instrucciones_lenguaje:
                    lista_instrucciones.append(instrucciones_lenguaje)
                else:
                    break

            # Ejecutar instrucciones
            valores = []
            registros_dict = {}  # Almacena los registros como diccionarios

            for elemento in lista_instrucciones:
                if isinstance(elemento, DeclaracionClaves):
                    print(elemento.ejecutarT())
                    valores = elemento.ejecutarT()  # Obtén la lista de valores
                elif isinstance(elemento, DeclaracionRegistros):
                    registros_separados = ()
                    registros = elemento.ejecutarT()  # Obtén la lista de registros
                    for registro in registros:
                        registro_dict = {}  # Almacena un registro como diccionario
                        for i, valor in enumerate(registro):
                            registro_dict[valores[i]] = valor  # Usa el nombre del campo como clave
                        codigo = registro_dict.get('codigo')
                        if codigo is not None:
                            registros_dict[codigo] = registro_dict

                        # Imprimir el diccionario actual

                elif isinstance(elemento, Contar):
                    total_registros = elemento.ejecutarT(registros_dict)  # Pasa el diccionario de registros como argumento
                    imprimir_consola += f"\n{total_registros}\n"
                elif isinstance(elemento, Promedio):
                    clave = elemento.clave
                    promedio_resultado = elemento.ejecutarT(registros_dict)

                    imprimir_consola += f'{promedio_resultado}'
                elif isinstance(elemento, Datos):
                    print(elemento.ejecutarT(registros_dict))
                    datos = elemento.ejecutarT(registros_dict)
                    imprimir_consola += f'\n{datos}'
                elif isinstance(elemento, Max):
                    clave = elemento.clave
                    valor_maximo = elemento.ejecutarT(registros_dict)

                    imprimir_consola += f'\n{valor_maximo}'
                elif isinstance(elemento, Min):
                    clave = elemento.clave
                    valor_minimo = elemento.ejecutarT(registros_dict)

                    imprimir_consola += f'\n{valor_minimo}'
                elif isinstance(elemento, Sumar):
                    clave = elemento.clave
                    valor_suma = elemento.ejecutarT(registros_dict)

                    imprimir_consola += f'\n{valor_suma}'
                elif isinstance(elemento, ContarSi):  # Asume que aquí detectas una instrucción contarsi
                    # Obtiene la clave y el número de elemento
                    clave = elemento.clave
                    numero = elemento.numero
                    resultado = elemento.contar(registros_dict)

                    imprimir_consola += f'\n{resultado}'

                elif isinstance(elemento, Reporte):
                    titulo = elemento.titulo  # Asume que ExportarReporte tiene un atributo 'titulo'
                    data = [list(registro.values()) for registro in registros_dict.values()]
                    keys = list(registros_dict[1].keys())

                    # Generar el archivo HTML con los datos
                    template = Template("""<!DOCTYPE html>
                    <html>
                    <head>
                        <title>{{ titulo }}</title>
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                    </head>
                    <body>
                        <div class="container mt-5">
                            <h1 class="text-center">{{ titulo }}</h1>
                            <table class="table table-bordered">
                                <thead class="thead-dark">
                                    <tr>
                                        {% for key in keys %}
                                            <th>{{ key }}</th>
                                        {% endfor %}
                                    </tr>
                                </thead>
                                <tbody>
                                    {% for row in data %}
                                        <tr>
                                            {% for value in row %}
                                                <td>{{ value }}</td>
                                            {% endfor %}
                                        </tr>
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </body>
                    </html>""")

                    rendered_html = template.render(titulo=titulo, keys=keys, data=data)

                    # Guardar el HTML en un archivo
                    with open("reporte.html", "w") as html_file:
                        html_file.write(rendered_html)
                    webbrowser.open("reporte.html")

                elif isinstance(elemento, Imprimir):
                    imprimir_consola += elemento.ejecutarT()
                elif isinstance(elemento, ImprimirLn):
                    imprimir_consola += elemento.ejecutarT()


            # Muestra el resultado en la consola de salida
            self.text_area2.configure(state='normal')
            self.text_area2.delete(1.0, "end-1c")
            self.text_area2.insert("end-1c", imprimir_consola)
            self.text_area2.configure(state='disabled')
            messagebox.showinfo("Análisis exitoso", "El código se analizó exitosamente.")

        except Exception as e:
            error_esp = traductor.translate(str(e))
            messagebox.showerror('Error',f"Ocurrió un error al analizar el código: {error_esp}")
            print("Ocurrió un error al analizar el código: ", e)

    def run_analysis(self, code):
        # Aquí puedes realizar el análisis del código, por ejemplo, usando subprocess
        try:
            # Ejemplo: Ejecutar un comando de consola y capturar la salida
            result = subprocess.check_output(["python", "-c", code], universal_newlines=True, stderr=subprocess.STDOUT)
            return result
        except subprocess.CalledProcessError as e:
            return f"Error: {e.returncode}\n{e.output}"
        except Exception as e:
            return f"Error inesperado: {str(e)}"

    def sobre_combobox(self, event):
        code = self.text_area.get("1.0", "end-1c")
        lista_lexemas = instruccion(code)
        if self.file_combobox.get() == 'Reporte de Errores':
            messagebox.showinfo('Reporte de Errores', 'Se generó el reporte de errores')
        elif self.file_combobox.get() == 'Reporte de Tokens':
            data = []
            for lexema in lista_lexemas:
                lexema_info = f'Lexema: {lexema.lexema}, Tipo: {lexema.tipo}, Fila: {lexema.getFila()}, Columna: {lexema.getColumna()}'
                data.append([lexema.lexema, lexema.tipo, lexema.getFila(), lexema.getColumna()])
                print(lexema_info)

            template = Template("""<!DOCTYPE html>
                                <html>
                                <head>
                                    <title>{{ titulo }}</title>
                                    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                                </head>
                                <body>
                                    <div class="container mt-5">
                                        <h1 class="text-center">{{ titulo }}</h1>
                                        <table class="table table-bordered">
                                            <thead class="thead-dark">
                                                <tr>
                                                    {% for key in keys %}
                                                        <th>{{ key }}</th>
                                                    {% endfor %}
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {% for row in data %}
                                                    <tr>
                                                        {% for value in row %}
                                                            <td>{{ value }}</td>
                                                        {% endfor %}
                                                    </tr>
                                                {% endfor %}
                                            </tbody>
                                        </table>
                                    </div>
                                </body>
                                </html>""")

            rendered_html = template.render(titulo='Reporte de Tokens', keys=['Lexema', 'Tipo', 'Fila', 'Columna'], data=data)
            with open("reporte_tokens.html", "w") as html_file:
                html_file.write(rendered_html)
            webbrowser.open("reporte_tokens.html")



if __name__ == "__main__":
    app = App()
    app.mainloop()