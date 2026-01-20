from reportlab.pdfgen        import canvas
from reportlab.lib.pagesizes import A4


class ToPDF:
    def __init__(self, data, game_name, filename):
        self.data = data
        self.game_name = game_name
        self.filename = filename

        self.c = None
        self.text_object = None

        self.width, self.height = A4
        self.x_axis = 0
        self.y_axis = 0

    def generate(self):
        self.c = canvas.Canvas(self.filename, pagesize=A4)
        self._config_page()
        self._draw_title()
        self._insert_data()
        self.c.save()

    def _config_page(self):
        around = 230

        self.x_axis = (self.width - around) / 2
        self.y_axis = self.height - 50

    def _draw_title(self):
        # Guardamos el estado de la fuente actual
        self.c.setFont("Helvetica-Bold", 16)

        # Calcula el centro
        self.c.drawCentredString(self.width / 2, self.height - 50, self.game_name)

        # Dibujamos una línea debajo del título
        self.c.setLineWidth(1)
        self.c.line(100, self.height - 60, self.width - 100, self.height - 60)

    def _insert_data(self):
        self.text_object = self.c.beginText(self.x_axis, self.y_axis - 50)
        self.text_object.setFont("Courier", 12)

        for i, item in enumerate(self.data):
            index = i + 1
            date  = item["date"]
            score = item["score"]

            line = f"{index:>3}. {date:<20} - {score:>8}"
            self.text_object.textLine(line)

            # Si se acaba una pagina, salta a la siguiente
            if self.text_object.getY() < 50:
                self.c.drawText(self.text_object)
                self.c.showPage()

                self.text_object = self.c.beginText(self.x_axis, self.y_axis)
                self.text_object.setFont("Courier", 12)

        self.c.drawText(self.text_object)