
from fpdf import FPDF 

class PDF(FPDF):
    def header(self) -> None:
        self.set_font(family='Helvetica', size=40)
        self.cell(w=210, h=30, text='CS50 Shirtificate', align='c') 
        self.image(
            'pickture/shirtificate.png',
            x=5,
            y=50,
            w=200,
            keep_aspect_ratio=True,
        )

    def add_text_on_shirt(self, text_input='XXXX took CS50') -> None:
        self.set_font(family='Helvetica', size=24)
        self.set_text_color(255, 255, 255) 
        self.text(x=(210 - self.get_string_width(f'{text_input} took CS50')) / 2, y=120, text=f'{text_input} took CS50')

    
        
user_input = input('Name: ')

pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.add_text_on_shirt(user_input)
pdf.output('final.pdf')





