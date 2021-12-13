
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("saludo.glade")

        fiestra = builder.get_object("fiestraPrincipal")
        self.txtNome = builder.get_object("txtNome")
        self.btnSaludo = builder.get_object("btnSaludo")
        self.lblSaludo = builder.get_object("lblSaludo")

        sinais = {"on_fiestraPrincipal_destroy": Gtk.main_quit,
                  "on_btnSaludo_clicked": self.onbtnSaludoClicked,
                  "on_txtNome_activated": self.ontxtNomeActivated}
        builder.connect_signals(sinais)

        fiestra.show_all()

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
