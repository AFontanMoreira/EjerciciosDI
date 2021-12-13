import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class CaixaDeBotons(Gtk.Grid):
    def __init__(self):
        super().__init__()

        btnBoton1 = Gtk.Button(label="Boton 1")
        btnBoton2 = Gtk.Button(label="Boton 2")
        btnBoton3 = Gtk.Button(label="Boton 3")
        btnBoton4 = Gtk.Button(label="Boton 4")
        btnBoton5 = Gtk.Button(label="Boton 5")
        btnBoton6 = Gtk.Button(label="Boton 6")

        self.add(btnBoton1)
        self.attach(btnBoton2, 1, 0, 2, 1)
        self.attach_next_to(btnBoton3, btnBoton1, Gtk.PositionType.BOTTOM, 1, 2)
        self.attach(btnBoton4, 1, 1, 2, 1)
        self.attach_next_to(btnBoton5, btnBoton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.attach_next_to(btnBoton6, btnBoton5, Gtk.PositionType.RIGHT, 1, 1)


if __name__ == "__main__":
    CaixaDeBotons()
    Gtk.main()