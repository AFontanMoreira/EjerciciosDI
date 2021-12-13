import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("primerEjercicio.glade")

        fiestra = builder.get_object("primerEjercicio")
        self.btnVerde = builder.get_object("btnVerde")
        self.btnRojo = builder.get_object("btnRojo")
        self.btnMorado = builder.get_object("btnMorado")

        sinais = {"on_primerEjercicio_destroy": Gtk.main_quit,
                  "on_btnVerde_clicked": self.onbtnVerdeclicked,
                  "on_btnRojo_clicked": self.onbtnRojoclicked,
                  "on_btnMorado_clicked": self.onbtnMoradoclicked
                  }
        builder.connect_signals(sinais)

        fiestra.show_all()

    def onbtnVerdeclicked(self, boton):
        print("verde")

    def onbtnRojoclicked(self, boton):
        boton.modify_bg(Gtk.STATE_NORMAL, Gtk.gdk.color_parse("red"))

    def onbtnMoradoclicked(self, boton):
        print("morado")

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
