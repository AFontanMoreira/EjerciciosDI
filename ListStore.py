import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio


class Aplicacion(Gtk.Window):
    def __init__(self):
        super().__init__(title="Ex de uso de Gtk ListStore")
        self.set_border_width(5)

        modelo = Gtk.ListStore(int, str)

        modelo.append(1, "Manuel")
        modelo.append(2, "Angel")
        modelo.append(3, "Marcos")
        modelo.append(19, "Alexander")
        modelo.append(8, "Joel")
        modelo.append(4, "Britza")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        cmbNomes = Gtk.ComboBox.new_with_model(modelo)
        cmbNomes.connect("changed",self.on_cmbNomes_changed)
        cmbNomes.set_entry_text_column(1)
        caixaV.pack_start(cmbNomes,False,False,0)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbNomes_changed(self,combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            id_fila, nome =modelo [fila][:2]

if __name__ == "__main__":
    Aplicacion()
    Gtk.main()
