import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:
    def __init__(self):
        wndFiestra = Gtk.Window()
        wndFiestra.set_title("Segunda")


        caixaV = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        print(dir (caixaV.props))
        caixaV.props.border_width = 15
        wndFiestra.add(caixaV)

        self.txtNome = Gtk.Entry()
        self.txtNome.set_text("Escriba aqui su nombre")
        self.txtNome.connect("activate", self.ontxtNomeActivated)
        caixaV.pack_end (self.txtNome, True, False, 6)

        self.lblSaludo = Gtk.Label()
        self.lblSaludo.set_text("Escribe tu nombre")
        caixaV.pack_end(self.lblSaludo,True,True,6)

        self.btnSaludo = Gtk.Button()
        self.btnSaludo.set_label("Saludo")
        self.btnSaludo.connect("clicked",self.onbtnSaludoClicked)
        caixaV.pack_end(self.btnSaludo,False,False,6)

        wndFiestra.connect ("destroy", Gtk.main_quit)
        wndFiestra.show_all()

    def onbtnSaludoClicked(self, boton):
        self.saudo()

    def ontxtNomeActivated(self,control):
        self.saudo()

    def saudo(self):
        nome = self.txtNome.get_text()
        self.lblSaludo.set_text("Hola" + nome)
if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
